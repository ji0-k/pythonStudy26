# 회원관리용 더미데이터를 파일(메모장)로 저장하여 관리해보자.

# 회원관리 curd를 사용자 지정 함수로 만들어 보자.
# c : 회원가입
# r : 회원리스트 관리자인경우 회원암호 변경, 블랙리스트로생성, 권한 부여
# r : 로그인 id와 pw를 활용하여 로그인 상태 유지 session
# u : 회원정보 수정
# d : 회원탈퇴, 회원비활성화

# 프로그램에서 사용될 변수들
# 전역변수(global) -> py 파일 안에서 전체적으로 사용되는 변수
# 지역변수(local) -> while, if, for, def안에서 사용되는 변수
run = True  # while 에서 전체적으로 사용되는 변수(프로그램 구동)
session = None  # 로그인상태 저장용 -> 로그인한 사용자의 리스트 인덱스 기억용
FILE_NAME = "members.txt" # 회원 정보를 저장할 메모장 파일명
members =[] # 현재 비어잇음 , .txt파일에 있는 내용을 가져와 리스트 처리함
# members 구조 :
#[아이디, 비밀번호, 이름, 권한, 활성화여부]
#["kkw", "1234", "김기원", "admin", "True"]
#kkw|1234|김기원|admin|True 로 메모장에 저장될 예정임



# 프로그램에서 사용될 리스트 들 (더미 데이터)
# sns = [1, 2, 3] # 회원번호 들 회원삭제및 추가시 번호가 흔들릴 수 있음(인덱스만!)
# ids = [] # 로그인 아이디 들
# pws = [] # 암호 들
# names = []  # 사용자 명
# roles = []  # 사용자 권한 (admin, manager, user)
# active = [] # 회원사용중, 탈퇴, 중지, 블랙리스트 등...
# 차후에는 파일처리로 변환 할 예정

# 파일 처리용 함수용
#--------------------------save_members 함수
def save_members():
    """
    members 리스트 내용을 members.txt 파일에 저장
    """
    with open(FILE_NAME, "w", encoding = "utf-8") as f: # 올 대문자상태이면 상수처리 , 웬만하면 변경 하면 안되는것들
        #        상수   덮어쓰기        한글처리용        파일객체
        # 하나하나 저장이아니라 전부 가져와서 한번에 저장하는 메서드
        # so , 읽기(덮기) 모드인 "w"f로 표현
        # "a= 추가용"
        # 메모리에 있는 리스트를 | 로 연결하여 한줄로 저장
        for member in members:
            line = f"{member[0]}|{member[1]}|{member[2]}|{member[3]}|{member[4]}"
            #              kkw|        1234|      김기원|      admin|      True  로 출력
            f. write(line)
#--------------------------save_members() 함수 종료

def road_members():
    """
    members.txt 파일을 읽어서 members 리스트에 저장
    """

# 프로그램에서 사용될 함수들
def member_add():
    # 회원가입용 함수
    print("member_add 함수로 진입합니다.")
    # 회원가입에 필요한 기능을 넣음
    uid = input("ID : ")
    #아이디 중복검사
    for member in members : #line = f"{member.txt[0]}|{member.txt[1]}|{member.txt[2]}|{member.txt[3]}|{member.txt[4]}"
                              #              kkw|        1234|      김기원|      admin|      True
        if member[0] == uid: #
            print("이미존재아이디")
            return # else가 꼭 필요없는 문 , 바로 return
    pw = input("PW : ")
    name = input("NAME : ")
    print("1. admin 2.manager 3.user")
    roleSelect = input("권한 선택 >>>")
    role = "user" #잘못 입력해도 user 권한으로 기본값
    if roleSelect == "1" :
        role = "admin"
    elif roleSelect == "2" :
        role = "manger"
        #else 생략하고 3이나 아무거나 입력시 바로 일반회원
        #-----------------입력종료
        print(f"아이디 : {uid}, 이름 : {uid}")
        print(f"권한 :  {uid}")
    #-----------------입력값 확인
    save_True = input("저장하려면 y :")
    if save_True == "y":
        #저장 시작
        members.append([uid, pw, name, role, True]) #리스트로 만들어줌
        save_members() #f리스트를 파일에 저장
        print("회원가입완료")

    print("member_add 함수를 종료합니다.")


# 회원가입용 함수 종료

def member_login():
    # 가입된 회원을 확인하여 로그인 처리 후 session 변수에 인덱스를 넣음
    print("member_login 함수로 진입합니다.")
    # 로그인에 필요한 기능을 넣음

    print("member_login 함수를 종료합니다.")


# 회원로그인용 함수 종료

def member_admin():
    # 관리자가 로그인 했을 경우 할수 있는 기능을 작성
    print("member_admin 함수로 진입합니다.")
    # 다른 사용자 암호 변경 코드

    # 블랙리스트로 변환 -> active를 False

    # 권한 부여 -> 사용자의 권한roles를 변경 (manage <-> user)

    print("member_admin 함수로 종료합니다.")


# 관리자가 사용자 변경사항 함수 종료

def member_logout():
    # 회원 로그아웃으로 상태 변경 -> session 값을 None으로 변경
    print("member_logout 함수로 진입합니다.")
    # 로그인 상태인지를 확인하고 session을 None으로 변경

    print("member_logout 함수를 종료합니다.")


# 로그아웃 함수를 종료

def member_modify():
    # 회원 정보 수정
    print("member_modify 함수로 진입합니다.")
    # 로그인 상태인지를 확인하고 자산의 정보를 확인하고 수정한다.

    print("member_modify 함수를 종료합니다.")


# 회원정보 수정 종료

def member_delete():
    # 회원 탈퇴 또는 회원 유휴등 처리
    print("member_delete 함수로 진입합니다.")
    # 로그인 상태인지를 확인하고 탈퇴는 pop, 유휴(active=False)

    print("member_delete 함수를 종료합니다.")


# 회원탈퇴 종료

# --------------------- 기능에 대한 함수 생성 끝----------------

def main_menu():
    print(f"""
    ==== 엠비씨아카데미 회원관리 프로그램입니다======
    1. 회원가입    2. 로그인     3. 로그아웃
    4. 회원정보수정      5. 회원탈퇴
    9. 프로그램 종료
    """)


# 메인메뉴용 함수 종료

def member_add_menu():  # 회원가입에서 사용할 메뉴
    print(f"""
    ----- 회원권한을 확인하세요.---------
    1. 관리자    2. 팀장    3. 일반사용자 
    """)


# ------------------ 메뉴 함수 끝 ------------------

# 프로그램 시작!!!!
while run:  # 메인 프로그램 실행 코드
    main_menu()  # 위에서 만든 메인 메뉴함수를 실행
    select = input(">>>")  # 키보드로 메뉴 선택
    if select == "1":  # 회원가입 코드
        member_add()  # 회원가입용 함수 호출

    elif select == "2":  # 로그인 메뉴 선택
        member_login()  # 로그인용 함수 호출

    elif select == "3":  # 로그아웃 메뉴 선택
        member_logout()  # 로그아웃 함수 호출

    elif select == "4":  # 회원정보 수정 선택
        member_modify()  # 회원정보 수정 함수 호출

    elif select == "5":  # 회원탈퇴 선택
        member_delete()  # 회원정보 삭제 함수 호출

    elif select == "9":  # 프로그램 종료 선택
        run = False

    else:
        print("잘못 입력하셨습니다.")
# while문 종료