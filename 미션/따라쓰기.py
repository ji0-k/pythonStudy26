# LMS

run = True
session = None #로그인한 회원 인덱스잡기

# 회원 데이터
sns = [1]
ids = ["admin"]
pws = ["1234"]
groups = ["admin"] # admin , pro , satf , stu, par


# 성적 데이터
studx = []
pythonScores = []
dbScores = []
websCores = []
tots = []
avgs = []

# 게시판 데이터
board_no = []
board_title = []
board_content = []
board_writer = []

# 메인메뉴
mainMenu = """
==========================
LMS
==========================
1. 로그인 / 회원가입
2. 성적관리
3. 게시판
4. 관리자메뉴
0. 프로그램 종료
"""

memberMenu = """
회원관리 메뉴

1.로그인
2.회원가입
0.뒤로가기
"""

scoreMenu = """
성적관리 메뉴

1.성적입력 (교수)
2.성적보기 (학생)
0.뒤로가기
"""

boardMenu = """
게시판 메뉴

1.글쓰기
2.글목록
3.글보기
"""

adminMenu = """
관리자 메뉴 

1.회원목록
2.회원 강제 삭제
0.뒤로 가기
"""

#=====================================
#메인루프
#=====================================
while run: # 메인메뉴 , 전체 돌아가는
    print(mainMenu) # 메인메뉴 출력
    select = input(">>>") # 메인메뉴중 하나 입력받음

    #--------------------------------
    # 1. 로그인 , 회원가입
    #-------------------------------
    if select == "1" : # 로그인 / 회원가입 선택후
        subRun = True # 하위 메뉴 돌게 만드는 변수
        while subRun : # 하위메뉴 돌리기
            print(memberMenu) #회원메뉴 출력
            sub  = input(">>>") #회원메뉴 뭐할건지 입력받기

            #------1로그인-----------
            if sub == "1" : #1.로그인 들어가기
                uid = input("ID : ")  # 유저 id 입력받기
                upw = input("PW : ")  # 유저 pw 입력 받기
                if uid in ids : # 입력받은 아이디가 리스트에있는지
                    idx = ids.index(uid) # 있다면 아이디 리스트에서 인덱스 가져오기
                    if pws[idx] == upw : # ids와pws 인덱스같은자리에 값이 입력된 pw와 같다면
                        session = idx # 그 인덱스 정보를 로그인세션으로 유지하기위한 변수
                        print(f"로그인 성공 / 권한 : {groups[idx]}")
                        # 로그인하고 권한 띄우기 위해 (f"")
                        # 권한 또한 위에서 따온 인덱스의 같은 주소의 값으로
                        subRun = False #하위메뉴 로그인 완료 , 끝냄
                    else :
                        print("비밀번호 오류 ") #입력받은 pw가 pws != [idx] 와 같지않으면
                else :
                    print("존재하지 않는 ID") #하나 윗단계의 ID가 일치하지않는경우
                    #로그인 후 상태관리 , 어떤상태, 어떤 sn을 가지고 있는지
                    #확인할 수 있는 부분 출력되게

            #--------2회원가입---------
            elif sub == "2" : #2.회원가입 값
                print("회원가입")
                uid = input("ID : ") # 새로등록할 ID 값 입력받기
                if uid in ids : # 입력받은ID ids 리스트에 있다면
                    print("이미 존재하는 ID") # 중복ID X
                    continue

                upw = input("PW : ")
                ###########ROLE 분기###############
                if session is None : #로그인세션이 널값이면
                    print("회원 유형 선택")  #입력하게함
                    print("1.학생")
                    print("2.부모")

                    r = input("선택 : ") #입력받은 숫자를 r변수로 넣은뒤;
                    if r == "1" : # 입력받은 r변수 1이면
                        role = "stu" # role 변수는 stu 이고
                    elif r == "2" : # r 변수 2입력받으면
                        role = "par" # role변수는 par 이고
                    else : # 그 외의 값입력 시 X
                        print("잘못된 접근")
                        continue #여기서 중단 후 다시 위로
                elif groups[session] == "admin" : # 세션값이 admin이면
                    print("권한선택")
                    print("1.관리자(admin)")
                    print("2.교수(pro)")
                    print("3.행정(staf)")
                    print("4.학생(stu)")
                    print("5.부모(par)")

                    role_map = {
                        "1" : "admin",
                        "2" : "pro",
                        "3" : "staf",
                        "4" : "stu",
                        "5" : "par"
                    }
                    r = input("선택 : ")
                    if r in role_map :
                        role = role_map[r]
                    else :
                        print("잘못된선택")
                        continue
                else :
                    print("관리자만 회원을 추가할 수 있습니다.")
                    continue
                sns.append(len(sns)+1)
                ids.append(uid)
                pws.append(upw)
                groups.append(role)
                print(f"회원가입 완료 (권한 :{role})")

            elif sub == "0" :
                subRun = False
            else :
                print("잘못입력")
                continue





            elif sub == "0" :
                subRun = False

            else :
                print()


























