# 회원 관리 CRUD 사용자 지정 함수
# C : 회원 가입
# R : [관리자] 회원리스트, 회원암호변경,블랙리스트로 생성 권한부여
# r : 로그인 id 와 pw를 활용하여 로그인 상태 유지 session
# U : 회원 정보 수정
# D : 회원 탈퇴 , 회원 비활성화

# 사용 할 변수
# 전역 변수(global) -> py 파일 안에서 전체 적으로 사용 되는 변수
# 지역 변수(local) -> while, if, for def 안에서 사용되는 변수

run = True # while에서 전체적으로 사용되는 변수 (프로그램 구동)
session = None #로그인한 사용자의 리스트 인덱스 기억용, 로그인 상태 유지

#프로그램에서 사용될 리스트 들 (더미 데이터)
# sns = [1,2,3] # 회원 번호s , 회원 삭제 및 추가시 번호가 흔들릴 수 있음(일단 인덱스)
ids = ["kkw","lhj","ljj"] # 로그인 아이디s
pws = ["1234","5678","8888"] # 암호s
names = ["김기원","임효정","이재정"] # 이름s
adds = ["주소1","주소2","주소3"] # 주문 후 배송주소
emails = ["a@.1","a@.2","a@.3"] # 주문완료 메일 전송
roles = ["admin","manager","user"] # 사용자 권한 , admin,manager,user)
active = [True,True,True] # 회원 사용중인지(True), 탈퇴(False), 중지(False), 블랙리스트(False) 상태
#관리자, 매니저 권한 비밀번호  pws = []
#차후에는 파일 처리로 변환 예정

# 프로그램에서 사용될 함수들

#=========기능에대한 함수============
def member_add() : # 회원 가입용 함수
    print("회원가입을 시작합니다")
    new_id = input("아이디 입력 : ")
    if new_id in ids: # True일때 , 기존 id있을때
        print("이미 존재하는 아이디")
        print("다시 시도해 주세요 ")
        return
    else : # 기존 없는 id일때
        new_pw = input("비밀번호 입력 : ")
        new_name = input("이름 입력 : ")
        new_add = input("주소 입력 : ")
        new_email = input("이메일 입력 : ")
        member_role_menu()
        role_set = input("권한 선택 : ")
        if role_set == "1" :
            new_role = "admin"
        elif role_set == "2" :
            print()
        else :
            new_role = "user"
        print(f"""
입력된 정보를 확인하세요 
이름 : {new_name}
아이디 :{new_id} / 비밀번호 : {new_pw}
주소 : {new_add} / 이메밀 :{new_email}
회원유형 : {new_role}
""")
        save_select = input("이 정보로 가입하려면 y : ")
        if save_select == "y" :
            ids.append(new_id)
            ids.append(new_pw)
            ids.append(new_name)
            ids.append(new_add)
            ids.append(new_email)
            ids.append(new_role)
            ids.append(True) # 일단 초기 가입시 활성화 상태로 바로
            print("회원 가입을 완료하였습니다.")


            #로그인 함수 만들어 넣기

        else :
            print("회원 가입을 중단하였습니다\n다시시도해주세요")
            return


def member_login() : # 가입된 id/pw 로그인 처리 후 session에 넣어 상태유지
    print("로그인에 진입하셨습니다.")

    global session # 맨 위에 전역변수로 지정한 내용 활용

    if session is not None : # 로그인 세션이 비어있지않으면 = 값이 있으면 = 로그인 상태이면
        # is not None 싱글톤이라는 객체가 있는지, 주소가 있는 값일때
        # != None 숫자 비교시 이퀄이나는 값으로 사용
        print("이미 로그인 상태 입니다.")
        print(f"로그인 사용자는 {names[session]}입니다")
        return
    else :
        user_id = input("ID : ")
        if user_id in ids :
            idx = ids.index(user_id) # 아이디 있으면 인덱스가져오기
            if not active[idx] : #회원 상태 확인
                print("비활성화/차단된 계정입니다.")
                return
            else : # True 상태 이면 pw와 일지 하는지
                user_pw  = input("Pw : ")
                if user_pw == pws[idx] : #입력받은 PW가 ID와같은 주소의 PW가 일치하는지
                    session = idx #로그인상태!
                    #글로벌 영역 변수 세션값이 있는 상태가 됨 (로그인 사용자의 인덱스)
                    print(f"{names[idx]}님 로그인 되었습니다.")
                else :
                    print("일치하지않는 PW, 암호확인")
                    return
        else :
            print("존재하지않는 ID")


    # 로그인에 필요한 기능 넣음
    print("로그인에 성공하였습니다.")

def member_logout() : #회원 로그아웃 상태로 변경
    print("로그아웃 하시겠습니까?")
    #로그인 상태인지 확인 후 로그아웃
    print("로그아웃 되었습니다.")

def member_admin() : # 관리자 로그인 상태에서 실행 기능
    print("관리자 모드 실행")
    # 다른 사용자 암호변경
    # 회원 상태 변경 , 블랙리스트, 중지, 탈퇴
    # 권한부여 -> 사용자 권한 변경
    print("관리자 모드 종료")

def member_modify() : # 회원정보 수정 user
    print("회원정보 수정에 진입")
    #로그인 상태인지 확인
    #자신의 정보 확인
    #자신 정보 수정
    print("회원정보 수정 완료")

def member_delete() : # 회원 탈퇴 또는 휴면 처리
    print("회원 상태변경 / 탈퇴 에 진입하였습니다")
#----------------------------------------------------

#==========메뉴 함수=======================
def member_main_menu() :
    print("""
========회원 관리 시스템=========
1. 회원가입
2. 로그인/로그아웃
3. 회원 정보 보기/수정
4. 회원 상태/탈퇴
-----------------------------
0. 프로그램 종료
==============================
""")

def member_role_menu() :
    print(f"""
-------회원 권한을 선택하세요------
1. 관리자
2. 매니저
3. 일반회원
-------------------------------
""")


def member_inout_menu() : #로그인아웃
    #로그아웃 상태이면 -> 로그인 진입
    print("로그인 하시겠습니까?")
    #로그인 상태이면 -> 로그아웃 진입
    print("로그아웃 하시겠습니까?")

def member_profile_menu() :
    print()





#===========주실행문==============d
while run : #주 실행코드
    member_main_menu()
    select = input("원하는 메뉴 번호 입력 : ")
    if select == "1" :
        member_add()
    elif select == "2" :
        member_inout_menu()
        member_login()
    elif select == "3" :
        member_modify()
    elif select == "4" :
        member_delete()
    elif select == "0" :
        print("프로그램을 종료합니다")
        run = False
    else :
        print("잘못된 접근")
        continue



