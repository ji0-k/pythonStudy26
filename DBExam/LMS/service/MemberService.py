# Member 객체에 CRUD
# DB연결
# 로그인
# 로그아웃
# 회원가입
# 정보수젇
# 회원탈퇴 및 비활성화


from LMS.common import Session
from LMS.domain import Member

class MemberService : # 여기서는 self주소가 아닌 , cls로 활용, 초기값 메서드 없다
    @classmethod
    def load(cls):
        conn = Session.get_connection() # lms db를 가져와 conn에 넣음
        try :
            with conn.cursor() as cursor : # cursor : SQL 쿼리를 실행하고 결과를 가져오는 객체
                cursor.execute("SELECT COUNT(*) AS cnt FROM members")
                count = cursor.fetchone()['cnt']
                #              fetchone(): 쿼리 결과의 첫 번째 행을 딕셔너리로 반환, count이니까 무조건 1개 반환
                #             .fetchall() 여러개의 결과가 나올때 : read all
                #             .fetchmany(3) 3개의 결과만 보고싶을때 (처음 상위 3개)
                print(f"m. data : {count}")
        except :
            print("MemberService.load()오류")
        finally: #항상출력
            print("DB connection")
            conn.close()

    @classmethod
    def login(cls): #로그인
        uid = input("Enter Member ID : ")
        password = input("Enter Member Password : ")

        conn = Session.get_connection() #DB읽기
        try :
            with conn.cursor() as cursor : # DB객체
                sql = "SELECT * FROM members WHERE uid = %s AND password = %s" #보여라 아이디, 비밀번호 둘다 일치하는경우
                # DB접근을 한번에 끝내야 하기때문에 웬만하면 묶어서
                cursor.execute(sql, (uid, password)) # 쿼리 실행해서 cursor에 반환
                row = cursor.fetchone()
                # fetchone uid는 유일하니까 있으면 1개 없으면 0, row 1/0 = True/False
                if row :
                    member = Member.from_db(row)
                    # row 1이면 True이니까 member에 저장됨

                    if not member.active :
                        print("not active")
                        return

                    Session.login(member)
                    print(f"{member.name},login success [{member.role}]")
                else :
                    print("ID PW 불일치")
        except: #예외상황
            print("MemberService.login()오류")
        finally:
            print("DB connection")
            conn.close()

    @classmethod
    def logout(cls):
        if not Session.is_login():
            print("비로그인")

        Session.logout()
        print("success logout")

    @classmethod
    def signup(cls):
        uid = input("Enter Member ID : ")
        conn = Session.get_connection()
        try :
            with conn.cursor() as cursor :
                check_sql = "SELECT id FROM members WHERE uid = %s"
                cursor.execute(check_sql, (uid,))
                if cursor.fetchone() :
                    print("이미 존재 ID")
                    return
                password = input("Enter Member Password : ")
                name = input("Enter Your Name : ")
                insert_sql = "insert into members (uid, password, name) VALUES(%s,%S,%S)"
                conn.commit()
                print("success signup, please login")
        except Exception as e:
            conn.rollback() # 둘중 하나라도 안되면 되돌려보낸다
            # 트랜젝션 : with안에 2개이상의 sql문이 둘다 True일때 commit()하고
            # 둘중 하나라도 안되면 되돌려보낸다
            print(f"회원가입 오류 : {e}")
        finally:
            conn.close()

    @classmethod
    def modify(cls):  # 회원 수정 메서드
        if not Session.is_login():
            print("로그인 후 이용 가능합니다.")
            return

        member = Session.login_member
        print(f"내정보 확인 : {member.name} / {member.password} / {member.id} ")
        print("\n[내 정보 수정]\n1. 이름 변경  2. 비밀번호 변경  3.회원 비활성 및 탈퇴  0. 취소")
        sel = input("선택: ")

        new_name = member.name
        new_pw = member.password

        if sel == "1":
            new_name = input("새 이름: ")
        elif sel == "2":
            new_pw = input("새 비밀번호: ")
        elif sel == "3":
            print("회원 중지 및 탈퇴를 진행합니다.")
        else:
            return

        conn = Session.get_connection()
        try:
            with conn.cursor() as cursor:
                sql = "UPDATE members SET name = %s, password = %s WHERE id = %s"
                cursor.execute(sql, (new_name, new_pw, member.id))
                conn.commit()

                #메모리(세션) 정보도 동기화
                member.name = new_name
                member.password = new_pw
                print("정보 수정 완료")
        finally :
            conn.close()

















