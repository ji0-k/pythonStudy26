from LMS.common import Session  # 로그인한 멤버객체
from LMS.domain.Score import Score  # 성적 객체


class ScoreService:
    @classmethod
    def load(cls):  # 접속 테스트용
        conn = Session.get_connection()
        # 세션객체에 있는 db연결 메서드를 실행하고 conn변수에 넣음
        try:
            with conn.cursor() as cursor:
                # 커서객체는 DB연결 성공시 연결정보를 가지고 있는
                cursor.execute("select count(*) as cnt from scores")
                # execute = sql문 실행
                count = cursor.fetchone()['cnt']
                # 실행 결과를 1개가져온다.
                print(f"시스템 : 현재 등록된 성적 수는 {count}개 입니다.")
        except Exception as e:
            print(f"MemberService.login() 오류발생: {e}")
        finally:
            conn.close()  # DB 연결 정보 닫는다

    @classmethod
    def run(cls):  # 성적처리용 주 메서드
        cls.load()
        if not Session.is_login():
            print("로그인 후 이용")
            return

        member = Session.login_member
        while True:
            print("\n====성적관리 시스템====")
            # 1. 관리자 / 매니저 메뉴
            if member.role in ("admin", "manage"):  # 관리자만 메뉴 보임
                print("1. 학생 성적 입력/수정")
            # 2. 공통메뉴
            print("2. 내성적조회")
            # 3. 관리자 전용메뉴
            if member.role == "admin":
                print("3. 전체 성적 현황(JOIN)")
            print("0. 뒤로가기")

            sel = input(">>>")
            if sel == "1" and member.role in ("admin", "manage"):
                cls.add_score()
            elif sel == "2":
                cls.view_my_score()
            elif sel == "3" and member.role in "admin":
                cls.view_all()
            elif sel == "0":
                break
            else:
                print("잘못된접근")
                return

    @classmethod
    def add_score(cls):
        target_uid = input("성적 입력할 학생 아이디(uid): ")
        conn = Session.get_connection()
        try:
            with conn.cursor() as cursor:
                # 1. 학생 존재 확인
                cursor.execute("SELECT id, name FROM members WHERE uid = %s", (target_uid,))
                student = cursor.fetchone()

                if not student:
                    print(f"'{target_uid}' 학생을 찾을 수 없습니다.")
                    return

                # 2. 점수 입력
                kor = int(input("국어: "))
                eng = int(input("영어: "))
                math = int(input("수학: "))

                # 3. Score 객체를 생성 (여기서 파이썬의 @property가 계산됨)
                temp_score = Score(member_id=student['id'], kor=kor, eng=eng, math=math)

                # 4. DB 저장 (객체의 프로퍼티 값을 SQL에 전달)
                cursor.execute("SELECT id FROM scores WHERE member_id = %s", (student['id'],))

                if cursor.fetchone():
                    # UPDATE 로직
                    sql = """
                          UPDATE scores
                          SET kor=%s,
                              eng=%s,
                              math=%s,
                              total=%s,
                              avg=%s,
                              grade=%s
                          WHERE member_id = %s
                          """
                    # 객체의 프로퍼티(temp_score.total 등)를 사용합니다.
                    cursor.execute(sql, (
                        temp_score.kor, temp_score.eng, temp_score.math,
                        temp_score.total, temp_score.avg, temp_score.grade,
                        student['id']
                    ))
                else:
                    # INSERT 로직
                    sql = """
                          INSERT INTO scores (member_id, kor, eng, math, total, avg, grade)
                          VALUES (%s, %s, %s, %s, %s, %s, %s) 
                          """
                    cursor.execute(sql, (
                        student['id'], temp_score.kor, temp_score.eng, temp_score.math,
                        temp_score.total, temp_score.avg, temp_score.grade
                    ))

                conn.commit()
                print(f"{student['name']} 학생의 성적 저장 완료 (객체 계산 방식)")
        finally:
            conn.close()

    @classmethod
    def view_my_score(cls):
        member = Session.login_member  # 로그인한 member객체
        conn = Session.get_connection()  # DB연결 객체
        try:
            with conn.cursor() as cursor:  # 연결성공시 TRUE
                # 로그인한 사람의 PK(id)로 성적 조회
                sql = "SELECT * FROM scores WHERE member_id = %s"
                cursor.execute(sql, (member.id,))
                data = cursor.fetchone()  # member의 DB정보가 date에담김

                if data:  # data가있으면
                    s = Score.from_db(data)  # dict타입의 객체를 s에 넣음
                    # 도메인 클래스의 __init__에는 uid 정보가 없으므로 세션 정보를 활용해 출력
                    cls.print_score(s, member.uid)  # 콘솔에 보기 좋게 출력
                else:
                    print("등록된 성적이 없습니다.")
        finally:
            conn.close()

    @classmethod
    def view_all(cls):
        print("\n[전체 성적 목록 - JOIN 결과]")
        conn = Session.get_connection()
        try:
            with conn.cursor() as cursor:
                # members와 scores를 JOIN하여 아이디(uid)와 성적을 함께 가져옴
                sql = """
                      SELECT m.uid, s.* 
                      FROM scores s 
                               JOIN members m ON s.member_id = m.id 
                      """
                cursor.execute(sql)
                datas = cursor.fetchall() #모든값

                for data in datas:
                    s = Score.from_db(data)
                    cls.print_score(s, data['uid'])
        finally:
            conn.close()

    @classmethod
    def print_score(cls, s, uid):  # 개인 성적 출력과 전체 성적 출력도 가능(메서드: 동작 -> 재활용가능)
        # 도메인 모델(score)에 계산 로직이 있으므로 s.score....그대로사용)
        print(
            f"ID:{uid:<10}|"
            f"국어:{s.kor:>3} 영어 :{s.eng:>3} 수학:{s.math:>3}|"
            f"총점:{s.total:>3} 평균:{s.avg:>3} | 등급 {s.grade:>3}"
        )
