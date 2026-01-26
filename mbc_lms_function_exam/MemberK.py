# C : 회원가입
# R : 관리자모드 의 정보확인
# r : 일반회원모드의 정보확인
# U : 관리자 모드의 정보수정 , 권한 수정 , 상태 수정
#     일반회원 모드의 정보수정
# D : 회원탈퇴

# 사용할 변수
run = True # 프로그램 구동
session = None # 로그인 유지를 위한 광역변수
FILE_NAME = "memberk.txt" #파일이 없을경우 회원정보 저장할 파일 생성할떄 파일이름
import os
memberk = [] #현재 비어잇음,만들어진 txt파일에있는 내용을 가져와 리스트처리함
#memberk는 2차원 배열로 될 것 이다.
#[                       ][                          ][                              ][ ... ]
#        0                             1                             2
#[아이디,PW,이름,권한,활성화]  [아이디,PW,이름,권한,활성화]      [아이디,PW,이름,권한,활성화]
#  0    1   2   3    4        0    1   2   3    4            0    1   2   3    4

# members 구조 :
# [아이디 , 비밀번호, 이름, 권한, 활성화여부]
#  "kkw"   "1234" "김기원" "admin" "True"
#  kkw|1234|김기원|admin|True 로 메모장에 저장될 예정임

ids = []
pws = []
names = []
address = []
emails = []
roles = []
role =""
active = []

#더미로 대왕관리자 만들어서 pw수정가능하게
mpw = 1234
apw = 4567

#-----------.txt 파일 데이터 저장을 위한 함수
def save_memberk():
    """
    members의 리스트 값을 membersK.txt 에 저장
    """
    with open(FILE_NAME,"w",encoding = "utf-8") as f :
#              상수 , 수정하고 덮어쓰기 , 한글처리용     파일객체
# 변수선언에서 FILE_NAME을 membersk.txt로선언
# 그 파일 열어서 한글로 코딩하고 덮어쓰는 모드로 열고 닫기 까지 해줘 , "a" 는 추가용
        for member in memberk :
            line = f"{member[0]}|{member[1]}|{member[2]}|{member[3]}|{member[4]}|{member[5]}|{member[6]}\n"
            f.write(line) #문자열 line을 f가 가르키는 파일에 그대로 써 넣는다.
#------------------save_membersk() 함수 종료

#-----------------데이터 저장된 값을 .txt파일에있는 값을 변수안에 리스트형태로 저장하는 함수, while런 하기전에 한번 불러오기
def load_memberk(): #텍스트 파일 읽어서 한줄씩 데이터 리스트 만든다  => 지금까지 중간수정X
    """
    members.txt 파일을 읽어서 members 리스트에 저장
    """
    # 기존파일이 없으면 새 파일로 만들어서 저장 (암기)
    if not os.path.exists(FILE_NAME) : # 현재 디렉토리에 FILE_NAME이 없다면
         # os.path 는 현재경로 -> os는 내부 라이브러리지만 기본적으로 포함되지않아 import해야함
        save_memberk() # 빈파일이 membersk.txt 로생성됨
        return #else가 굳이 필요하지 않은 조건 문
    # 파일 있으면 열어서 한줄씩 읽기
    with open(FILE_NAME,"r",encoding ="utf-8") as f:
    # FILE_NAME=membersk.txt 읽기모드로 한글지원 해서 f라는 변수에 넣어
        for line in f: # f파일의 내용을 한줄씩 line변수에다가 넣어
            #print("----------------------------------")
            #print(f"변조 전 데이터 : {line}")
            data = line.strip().split("|") # 줄끝에 엔터제거, "|"바로 리스트 분류화, |기준으로나눔
            data[6] = (data[6] == "True")
            if data[5] == "관리자":
                data[6] = True
            #print(f"변조 후 데이터 : {data0122}")
            memberk.append(data)






#-----------메뉴용 함수
#00. 메인 메뉴
def member_main_menu():
    print("""
=======회원관리 시스템=======
1. 회원가입
2. 로그인 / 로그아웃
3. 회원정보 보기 / 수정
4. 회원 상태 / 탈퇴
--------------------------
0. 프로그램 종료
==========================
""")
#01. 회원가입 메뉴
def member_add_menu():
    print("""
------회원 유형 선택--------
1. 일반회원
2. 매니저
3. 관리자 
-------------------------
0. 돌아가기
-------------------------
""")
#03. 회원 정보
def member_profile_menu():
    print("""
----------회원정보--------
1. 정보 보기
2. 정보 수정
-------------------------
0. 돌아가기
-------------------------
""")

def member_profile_edit_menu():
    print("""
1. 정보수정 
0. 돌아가기
--------------------------""")
    return input(">>>")



#02. 로그인/ 로그아웃 메뉴 프로그램 상태에서 대체

#03. 회원정보 보기 / 수정
#03-01 관리자가 보는 정보보기 / 수정

def member_profile_menu_admin():
    #----------회원정보 띄우기-----------------------
    print("="*80)
    print(f"{'ID':10}{'pw':10}{'이름':10}{'메일':10}{'주소':10}{'회원유형':10}{'상태':10}")
    print("="*80)
    for member in memberk:
        status_text = "활성화" if member[6] else "비활성화"
        print(f"{member[0]:10}{member[1]:10}{member[2]:10}{member[3]:10}{member[4]:10}{member[5]:10}{status_text:10}")
    print("="*80)
    select_edit = member_profile_edit_menu()
    #-------------정보수정, 아이디입력 -------------------
    if select_edit == "1" :
        select_id = input("정보 수정하려는 ID를 입력하세요 : ")
        for member in memberk:
            if member[0] == select_id:
                status_text = "활성화" if member[6] else "비활성화"
                print("=" * 80)
                print(f"{'ID':10}{'PW':10}{'이름':10}{'메일':10}{'주소':10}{'회원유형':10}{'상태':10}")
                print("=" * 80)
                print(
                    f"{member[0]:10}{member[1]:10}{member[2]:10}{member[3]:10}{member[4]:10}{member[5]:10}{status_text:10}")
                print("=" * 80)

                new_pw = input("PW : ")
                new_name = input("NAME :")
                new_email = input("EMAIL : ")
                new_address = input("ADDRESS : ")
                print(f"PW : {new_pw}")
                print(f"NAME : {new_name}")
                print(f"EMAIL: {new_email}")
                print(f"ADDRESS : {new_address}")
                save_edit = input("입력하신 정보로 수정하려면 y : ")
                if save_edit == "y":
                    new_pw = memberk[session][1]
                    new_name = memberk[session][2]
                    new_email = memberk[session][3]
                    new_address = memberk[session][4]
                    print("회원 정보 변경이 완료 되었습니다.")
                    return
                else :
                    print("입력하신 정보를 찾을 수 없습니다.")
                    member_profile_menu_admin()
                    return
    elif select_edit == "0" :
        return

#03-02 매니저가 보는 정보(all) / 수정 (본인의것만)
def member_profile_menu_manage():
    print("="*65)
    print(f"{'ID':10}{'이름':10}{'메일':10}{'주소':10}{'회원유형':10}{'상태':10}")
    print("="*65)
    for member in memberk:
        status_text = "활성화" if member[6] else "비활성화"
        print(f"{member[0]:10}{member[1]:10}{member[2]:10}{member[3]:10}{member[4]:10}{member[5]:10}{status_text:10}")
    print("="*65)
    member_profile_edit_menu()
    print("매니저는 본인의 회원 정보 수정만 가능합니다")
    if select_edit == "1" :
        new_pw = input("PW : ")
        new_name = input("NAME :")
        new_email = input("EMAIL : ")
        new_address = input("ADDRESS : ")
        print(f"PW : {new_pw}")
        print(f"NAME : {new_name}")
        print(f"EMAIL: {new_email}")
        print(f"ADDRESS : {new_address}")
        save_edit = input("입력하신 정보로 수정하려면 y : ")
        if save_edit == "y" :
            new_pw = memberk[session][1]
            new_name = memberk[session][2]
            new_email = memberk[session][3]
            new_address = memberk[session][4]
            print("회원 정보 변경이 완료 되었습니다.")
            return
    elif select_edit == "0" :
        return

#03-03 사용자가 보는 정보보기 / 수정
def member_profile_menu_user():
    print("="*60)
    print(f"{'ID':10}{'PW':10}{'이름':10}{'메일':10}{'주소':10}{'회원유형':10}")
    print("="*60)
    print(f"{memberk[session][0]:10}{memberk[session][1]:10}{memberk[session][2]:10}{memberk[session][3]:10}{memberk[session][4]:10}{memberk[session][5]:10}")
   # print(f"{member.txt[0]}{member.txt[2]}){member.txt[3]}{member.txt[4]}{member.txt[5]}{member.txt[6]}")
    #본인의 인덱스 넣어서 본인정보만 나오게 하기
    print("="*60)
    member_profile_edit_menu()

    if select_edit == "1" :
        new_pw = input("PW : ")
        new_name = input("NAME :")
        new_email = input("EMAIL : ")
        new_address = input("ADDRESS : ")
        print(f"PW : {new_pw}")
        print(f"NAME : {new_name}")
        print(f"EMAIL: {new_email}")
        print(f"ADDRESS : {new_address}")
        save_edit = input("입력하신 정보로 수정하려면 y : ")
        if save_edit == "y" :
            new_pw = memberk[session][1]
            new_name = memberk[session][2]
            new_email = memberk[session][3]
            new_address = memberk[session][4]
            print("회원 정보 변경이 완료 되었습니다.")
            return
    elif select_edit == "0" :
        return
#-----------프로그램 함수
#000. 회원 유형 선택 로직
def member_role_no():
    global session
    if session is not None :
        print("이미 가입된 회원 입니다.")
        return
    select = input(">>>")
    global role
    if select == "1" :
        print("일반회원으로 가입합니다.")
        role = "일반회원"
        member_add()
    elif select == "2" :
        print("매니저회원으로 가입합니다.")
        manage_pw = int(input("매니저PW : "))
        if manage_pw == mpw :
            print("매니저 암호 확인")
            role = "매니저"
            member_add()
        else:
            print("암호 오류, 관리자 문의")
            return
    elif select == "3" :
        print("관리자회원으로 가입합니다.")
        admin_pw = int(input("관리자PW"))
        if admin_pw == apw :
            print("관리자 암호확인")
            role = "관리자"
            member_add()
        else :
            print("암호오류, 관리자 문의")
            return
    elif select == "0" :
        print("이전 페이지로 ")
        return
    else :
        print("잘못된 접근")
        pass


#001. 회원 가입

def member_add():
    global session
    new_id = input("ID : ")
    #-------id 중복검사---------------
    for member in memberk :
        if member[0] == new_id :
            print("이미 존재 하는 ID")
            return
    #--------------------------------

    # ------ 다른 정보 입력 받기-----------------------
    new_pw= input("PW : ")
    new_name = input("NAME :")
    new_email = input("EMAIL : ")
    new_address = input("ADDRESS : ")
    new_role = role
    active = True

    print(f"""
입력된 정보를 확인하세요 
이름 : {new_name} / 아이디 :{new_id} 
비밀번호 : {new_pw}
주소 : {new_address} / 이메밀 :{new_email}
회원유형 :{new_role}
""")
    #----------------------------------------------

    #--------입력 정보 저장, 가입 ----------------------
    save_select = input("이 정보로 가입하려면 y : ")
    if save_select == "y" :
        memberk.append([new_id, new_pw, new_name, new_email, new_address,new_role,True])
        save_memberk()
        # ids.append(new_id)
        # pws.append(new_pw)             #이렇게 하나하나 쓰는거 말고 리스트에 통째로 넣기
        # names.append(new_name)
        # emails.append(new_email)
        # address.append(new_address)
        # roles.append(new_role)
        # active.append(True)
        print("회원가입이 완료 되었습니다")
        print("로그인 해 주세요")
        return
        #바로 로그인 세션 넣어주기
    else :
        print("회원가입이 중단되었습니다 \n 다시 시도해주세요 ")
        return
    #-------------------------------------------------

#002. 로그인 / 로그아웃 처리 함수

def member_loginout() :
    global session
    #---------로그인상태에서 로그아웃-------------------
    if session is not None : #세션이 None이 아닌 = 세션있는 = 로그인된
        print(f"{memberk[session][2]} 님 로그인상태입니다.")
        logout_select = input("로그아웃하시려면 y : ").strip().lower()
        if logout_select == "y" :
            session = None
            print("로그아웃 되었습니다.")
            return
        else :
            print("로그인상태 유지")
            return
    #-------------------------------------------------

    #-------------로그인----------------------
     #세션이 None인 = 세션 없는 = 로그인 안된
    user_id = input("ID : ")
    user_pw = input("PW : ")
        #----------회원정보 ID있는지 확인
    for idx, member in enumerate(memberk) :
        if member[0] != user_id :
            continue

        if not member[6] :
            print("비활성화 / 차단 계정입니다.")
            return
        if member[1] == user_pw :
            session = idx
            print(f"{member[2]} 님 로그인 성공")
            return
        else :
            print("PW 불일치 ")
    print("가입정보 확인 불가 ") # for문 돌다가 안 걸리면 ID없음으로 뜨게
    #----------------------------------------------------------------

#003. 회원 정보 / 수정 처리 함수

def member_profile() :
    global session
    if session is None :
        print("회원 정보 없음, 로그인 필요")
        return
    else :
        if memberk[session][5]== "관리자" :
            member_profile_menu_admin()
        elif memberk[session][5] == "매니저" :
            member_profile_menu_manage()
        else :
            member_profile_menu_user()



#-----------실행문
load_memberk() # 프로그램 시작 시 파일을 불러오기
#member_profile_menu_admin() #[] append안했기 때문에 공란으로 뜸
while run :
    member_main_menu()
    select = (input("번호입력 >>>"))
    if select == "1" :
        member_add_menu()
        member_role_no()
    elif select == "2" :
        member_loginout()
    elif select == "3" :
        member_profile()
    elif select == "4" :
        print()
    elif select == "0" :
        print()
        break
    else :
        print()
