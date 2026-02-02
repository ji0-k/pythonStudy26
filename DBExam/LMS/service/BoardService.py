from LMS.common.Session import Session


class BoardService:
    @classmethod
    def run(cls):
        if not Session.is_login():
            print("로그인 후 이용")
            return
        while True :
            cls.list_board()
            print("1. 게시물 등록")
            print("2. 상세보기 (수정/삭제)")
            print("0. 돌아가기")

            sel = input(">>>")
            if sel == "1":
                cls.write_board()
            elif sel == "2":
                cls.view_board()
            elif sel == "0":
                break
            else :
                return


    @classmethod #클래스 레벨에서 실행되는 메서드(객체생성없이 호출 간으)
    def list_board(cls):
        # 헤더 출력 꾸밈
        print("\n" + "=" * 60)
        print(f"{'번호':<5} | {'제목':<25} | {'작성자':<10} | {'작성일'}")
        print("-" * 60)

        # DB에 연결한 객체 가져와 conn에 넣음
        conn=Session.get_connection()
        #Session: DB 접속 정보(호스트, 아이디, 비밀번호 등)를 관리하고 있는 클래스나 객체입니다.
        #.get_connection(): 미리 설정된 정보를 바탕으로 **"실제 MySQL 서버에 접속하라"**는 명령을 내리는 메서드입니다
        # conn: 접속이 성공하면 서버와 나 사이의 **'연결 통로(Connection 객체)'**가 생성되는데,
        #       이걸 conn이라는 변수에 담아서 보관하는 것
        try:
            with conn.cursor() as cursor: #쿼리를 실행할 커서 생성

                # 조인JOIN 쿼리 핵심부분
                sql = """
                      SELECT b.*, m.name 
                      FROM boards b
                               JOIN members m ON b.member_id = m.id
                      ORDER BY b.id DESC \
                      """
                # SELECT b.*, m.name : 게시판(b)의 모든 정보와 회원(m)의 이름만 가져와라
                # From boards b : 게시판 테이블 메인으로 사용하며 b라 부르겠다
                # join members m : 회원 테이블 가져와 옆에 붙이고 m이라 부르겠다
                # on b.member_id = m.id : 게시판의 작성자번호와 회원의 고유번호가 같은것끼리 매칭
                # order by b.id DESC \ : 최신글이 위로, 번호내림차순 정렬.
                cursor.execute(sql) #쿼리실행
                datas = cursor.fetchall() # 조회된 모든 행(row)을 리스트로 가져옴

                for data in datas: # 가져온 데이터 한줄씩 반복하며 출력
                    # 날짜 형식 처리 (YYYY-MM-DD 형식으로 출력)
                    date_str = data['created_at'].strftime('%Y-%m-%d')
                    print(f"{data['id']:<5} | {data['title']:<25} | {data['name']:<10} | {date_str}")
        finally:
            conn.close() #작업이 끝나면 DB연결을 닫음(메모리관리)
        print("=" * 60)


    @classmethod #게시물 등록
    def write_board(cls):
        print("\n[게시글작성]")
        title = input ("제목 : ")
        content = input("내용 : ")

        #DB연결
        conn = Session.get_connection()
        try: #정상적인 로직
            with conn.cursor() as cursor :
                # sql실행 ,member_id는 Session에서 가져옴
                sql = """
                      insert into boards (member_id, title, content) 
                      values (%s, %s, %s)
                      """

                cursor.execute(sql, (Session.login_member.id, title, content))
                # Session.login_member객체에서 현재 로그인한 id(FK)가져와 연결
                # boards 테이블의 member_id필드는 members테이블의 id 참조

                # 데이터 확정 (insert,update,del 시 필수)
                conn.commit()
                print("[게시글 등록 완료]")

        except Exception as e: # 에러상황
            conn.rollback() # 다시 되돌리기
            print(f"게시글 등록 오류 발생 : {e}")
        finally : # 어쨋든 마지막엔 반드시 닫기
            conn.close() #연결 닫기


    @classmethod #게시물 상세보기 수정 삭제
    def view_board(cls):
        target_id = input("조회할글번호 : ")
        conn= Session.get_connection()
        try:
            with conn.cursor() as cursor:
                sql = """
                      select b.*, m.uid 
                      from boards b 
                      join members m 
                      on b.member_id = m.id
                      where b.id = %s 
                      and b. active = 1
                      """
                cursor.execute(sql, (target_id,))
                row = cursor.fetchone()

                if not row :
                    print("존재하지않는 게시글입니다")
                    return

                print(f"\n[{row['id']}] 제목: {row['title']}")
                print(f"작성자: {row['uid']} | 작성일: {row['created_at']}")
                print("-" * 40)
                print(row['content'])
                print("-" * 40)
                if Session.is_login() and Session.login_member.id == row['member_id']:
                    print("★ 본인 글입니다: [1]수정 [2]삭제 [0]목록")
                    choice = input("선택 >> ")
                    if choice == "1":
                        cls.update_board(row['id'])
                    elif choice == "2":
                        cls.delete_board(row['id'])
                else:
                    input("엔터를 누르면 목록으로 돌아갑니다.")
        finally:
            conn.close()
S

        pass

    @classmethod
    def update_board(cls, param):
        pass

    @classmethod
    def delete_board(cls, param):
        pass