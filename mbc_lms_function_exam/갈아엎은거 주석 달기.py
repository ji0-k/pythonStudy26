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
import os
run = True # while 에서 전체적으로 사용되는 변수(프로그램 구동)
session = None # 로그인상태 저장용 -> 로그인한 사용자의 리스트 인덱스 기억용
FILE_NAME = "members.txt" # 회원 정보를 저장할 메모장 파일명
members = []  # 지금은 비어있지만 좀 있다 메모장에 있는 내용을 가져와 리스트 처리함
#members는 2차원 배열로 될 것 이다.
#[                       ][                          ][                              ][ ... ]
#        0                             1                         2
#[아이디,PW,이름,권한,활성화]
#   0   1   2   3    4      [아이디,PW,이름,권한,활성화]
#                             0    1   2   3    4        [아이디,PW,이름,권한,활성화]
#                                                          0    1  2    3    4
# members 구조 :
# [아이디 , 비밀번호, 이름, 권한, 활성화여부]
#  "kkw"   "1234" "김기원" "admin" "True"
#  kkw|1234|김기원|admin|True 로 메모장에 저장될 예정임

#파일 처리용 함수들!!
#--------------------회원 데이터 , 파일에 저장시키는 함수 , 메모리상에
def save_members() :
    """
    members 리스트 내용을 members.txt 파일에 저장
    """
    with open(FILE_NAME, "w", encoding="utf-8") as f:       # 변수 선언에서 FILE_NAME을 members.txt로 선언, 그거열어서
        #     상수     덮어쓰기         한글처리용     파일객체   # 한글로 코딩하고, 덮어쓰기가능한모드로 열고 닫기까지 해줘
        #                "a" = 추가용
        for member in members : #멤버는 멤버스의 2차워배열 중 1줄을 가져와 넣은것
            line = f"{member[0]}|{member[1]}|{member[2]}|{member[3]}|{member[4]}\n"
            #                kkw|       1234|      김기원|      admin|       True
            # 메모리에 있는 리스트를 |로 연결하여 한줄로 저장 .txt에는 "아이디|비번|이름|회원유형|상태" 로 써있
            f.write(line) #문자열line을 f가 가르키는 파일에 write() 그대로 써넣는다.
# -----------------------------save_members() 함수 종료

#-----------------데이터 저장된 .txt파일에있는 값을 읽어 변수 리스트에 저장하는 함수,while런하기전에 먼저 한번 불러와
def load_members() : #텍스트 파일을 전체 불러와 데이터 변수 리스트로 만든다 => 중간 수정이 안되기때문에
    """
    members.txt 파일을 읽어서 members 리스트에 저장
    """
    # 파일이 없으면 새파일 생성 (암기)
    if not os.path.exists(FILE_NAME): # 지금 디렉토리에 FILE_NAME이 없으면
          #os. path 는 현재경로 -> os는 내부 라이브러리지만 기본적으로 포함되지않아 import해야함
        save_members() # 원래 없빈 파일이 members.txt 로 생성됨
          #with open(FILE_NAME, "w", encoding="utf-8") as f:
         # 코드 중복 설명 다시 쓰기
        return

    # 있으면 파일을 열어서 한 줄씩 읽기
    with open (FILE_NAME, "r", encoding="utf-8") as f:
#          members.txt   읽기전용        한글지원      f 라는 변수에 넣어
        for line in f : # f파일 내용을 한줄씩 line 변수에 넣음
            print("-------------------------------")
            print(f"변조 전 데이터 : {line} ")
            #kkw|1234|김기원|admin|True
            #줄 끝에 엔터 제거 , |로 분류된거 리스트화
            data = line.strip().split("|")
            #         맨뒤에 엔터제거
            #                  |를 기준으로 나눔
            # 변조 후 데이터를 확인해보면 모두다~ 문자열로 취급됨
            # 숫자, 문자열 ?? 어
            # 문자열 "True"를 블리언(True/False) 타입으로 변환
            data[4] = True if data[4] == "True" else False
            #          받은변수   = 넣을 값      data4번재가 문자열 Trued이면 트루
            #                                   아니면 False를 넣음
            # if data0122[4] == "True" :
            #   data0122[4] = True
            # else :
            #   data0122[4] = False
            print(f"변조 후 데이터 :{data}")
            members.append(data)

#----------------------------load_members() 함수 종료


# 프로그램에서 사용될 함수들
#---------------------회원가입정보받아 리스트에 저장하고 .txt파일에 저장
def member_add():
    # 회원가입용 함수
    print("member_add 함수로 진입합니다.")
    # 회원가입에 필요한 기능을 넣음
    uid = input("아이디 : ")

    #=========아이디 중복검사
    for member in members :
        if member[0] == uid: # {member.txt[0]}|{member.txt[1]}|{member.txt[2]}|{member.txt[3]}|{member.txt[4]
            #                      uid        pw          name        role        active
            print("이미 존재하는 아이디 입니다.")
            return # 돌아감 , member_add() 함수를 빠져나감, else처리같이 되기때문에 else안쓰고 대체
    #=========아이디 중복검사 끝

    #=========다른정보 입력 받기
    pw = input("비밀번호 : ")
    name = input("이름 : ")

    # 권한 선택
    print("1. admin   2.manager 3.user ")
    roleselect = input("권한 선택 : ")

    role = "user" # 잘못 클릭해도 user권한으로 기본값
    if roleselect == "1":
        role = "admin"
    elif roleselect == "2":
        role = "manager"
    # ====== 입력 종료 =======

    # ===========입력값 확인
    print(f"아이디 : {uid}  이름 : {name} ")
    print(f"권한 : {role}    암호 : {pw} ")
    # ==============================

    save_true = input("저장하려면 y를 누르세요 :")
    if save_true == "y" :
        # 저장 시작!!!
        members.append([uid, pw, name, role, True]) # 리스트로 만듬
        save_members() # 리스트를 파일에 저장
        print("회원가입완료")
    print("member_add 함수를 종료합니다.")
#------------------ member_add() 함수 종료

#--------------------member_login

def member_login() :
    # 가입된 회원을 확인하여 로그인 처리 후 session 변수에 인덱스를 넣음
    print("member_login 함수로 진입합니다.")
    global session # 전역변수로 생성한 값을 가져옴
    if session is not None :
        print("이미 로그인중, 로그아웃 후 이용 ")
        return
    uid = input("ID : ")
    pw = input("PW : ") #키보드로 id pw입력 받아 변수에 넣기

    #회원 목록에서 아이디 검색
    for idx, member in enumerate(members) :
        #enumerate (members) for문은 반복문 , 인덱스(주소)를 가져옴 #2차원 배열에 쓰임
        # idx-> 1차원 주소 가 들어오고
        # member.txt -> 2차원 리스트 가 들어오고
        #print("idx :" , idx)  무슨내용인지 확인하려고 씀
        #print("member.txt: ",member.txt) 무슨내용인지 확인하려고 씀

        if member[0] == uid : #키보드로 입력한 uid와 리스트에 있는 값이 같으면 아이디 찾음
            if not member[4] : # False이면 (활성화 상태 확인)
                print("로그인 할 수 없는 계정입니다.")
                return

            if member[1] == pw : # 입력한 pw와 리스트 1자리의 값과 같으면
                session = idx # 전역 변수에 로그인한 주소를 넣음
                print(f"{member[2]}님 로그인 성공")
                return
            else :
                print("비밀번호가 다릅니다 초기메뉴로 리턴")
                return

    print ("존재하지 않는 아이디 입니다/") #for문이 진행하면서 return에 없는경우

# ----------------------------회원로그인용 함수 종료

#------------관리자 모드 로그인
def member_admin() :
    # 관리자가 로그인 했을 경우 할수 있는 기능을 작성
    print("member_admin 함수로 진입합니다.")
    # 다른 사용자 암호 변경 코드

    # 블랙리스트로 변환 -> active를 False

    # 권한 부여 -> 사용자의 권한roles를 변경 (manage <-> user)

    print("member_admin 함수로 종료합니다.")
# 관리자가 사용자 변경사항 함수 종료

def member_logout() :
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

def main_menu() :
    print(f"""
    ==== 엠비씨아카데미 회원관리 프로그램입니다======
    1. 회원가입    2. 로그인     3. 로그아웃
    4. 회원정보수정      5. 회원탈퇴
    9. 프로그램 종료
    """)
# 메인메뉴용 함수 종료

def member_add_menu() : # 회원가입에서 사용할 메뉴
    print(f"""
    ----- 회원권한을 확인하세요.---------
    1. 관리자    2. 팀장    3. 일반사용자 
    """)

# ------------------ 메뉴 함수 끝 ------------------

# 프로그램 시작!!!!
load_members() # 프로그램 시작 시 파일을 불러오기
print(members) #[] append안했기 때문에 공란으로 뜸

while run : # 메인 프로그램 실행 코드
    if session == None :
        print("비로그인상태")


    main_menu() # 위에서 만든 메인 메뉴함수를 실행
    select = input(">>>") # 키보드로 메뉴 선택
    if select == "1" : # 회원가입 코드
        member_add()   # 회원가입용 함수 호출

    elif select == "2" : # 로그인 메뉴 선택
        member_login() # 로그인용 함수 호출

    elif select == "3" : # 로그아웃 메뉴 선택
        member_logout() # 로그아웃 함수 호출

    elif select == "4" : # 회원정보 수정 선택
        member_modify()  # 회원정보 수정 함수 호출

    elif select == "5" : # 회원탈퇴 선택
        member_delete()     # 회원정보 삭제 함수 호출

    elif select == "9" : # 프로그램 종료 선택
         run = False

    else:
        print("잘못 입력하셨습니다.")
# while문 종료