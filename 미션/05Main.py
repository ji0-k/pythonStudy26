# 대부분 프로그래밍에서 1번이 되는 (start) 파일을 main으로 만듦


# 목표 : MBC 아카데미 LMS 프로그램을 만들어 보자
# 회원 관리 : 시스템담당자, 교수, 행정, 학생, 손님, 학부모
# 성적 관리 : 교수[성적등록,수정]
#           행정[백업(이전->삭제)]
#           학생[성적일람, 성적출력]
#           손님[소개페이지열람]
#           학부모[자녀학사관리]
# 게시판 : 회원제, 비회원제, 문의사항, Q&A

#필요한 변수
run = True # 메인메뉴용 while
subRun = True # 보조메뉴용 whlie
session = None # 로그인한 사용자의 인덱스를 유지

# 필요한 리스트

# 1.회원에 대한 리스트
sns = [1,2] #회원번호
sn = None
ids = ["kkw", "1234"] #로그인 id
pws = ["1234","1234"] #암호
groups = ["관리자", "학생"] # 회원분류
#adamin = 관리자 , stu = 학생, pro = 교수, guest = 손님 , par = 학부모

# 2.성적에 대한 리스트
pythonScores = [100,100] #파이썬점수 리스트
dataBadeScores = [100,100] #DB 점수 리스트
wwwScores = [100,100] #프론트점수 리스트
totalScore = [] #총점 리스트
avgScore = [] # 평균 리스트
stuIdx = [] #학생의 인덱스(학번) <-> 회원의 sn와  연결


# 게시판에 대한 리스트
board_no = [] # 게시물의 번호
board_title = [] # 게시물의 제목
board_content = [] # 게시물의 내용
board_writer = [] # 게시물의 작성자 <-> 회원SN


#메뉴구성
mainMeun = """
===================================
LMS에 오신걸 환영합니다.
===================================

1. 로그인 (회원가입)
2. 성적관리
3. 게시판
4. 관리자메뉴

0. 프로그램 종료

"""

memberMenu = """
---------------------------------
회원 관리 메뉴입니다.
---------------------------------
1.회원가입
2.로그인
3.회원수정
4.회원탈퇴

0. 회원관리 메뉴종료

"""

scoreMenu = """
---------------------------------
성적 관리 메뉴 입니다.
---------------------------------

1. 성적 입력 (교수전용)
2. 성적 보기 (학생/학부모용)
3. 성적 수정 (교수전용)
4. 성적 백업 (행적직원 전용)

0. 성적관리 메뉴종료

"""

boardMenu = """
--------------------------------
회원제 게시판 입니다.
--------------------------------
1. 게시물 등록
2. 게시판 보기
3. 게시물 보기
4. 게시글 수정
5. 게시글 삭제

0. 게시판 메뉴 종료

"""

# 주실행문 구현
while run :
    print(mainMeun)
    select = input("원하는 메뉴의 번호를 입력하세요 : ")

    if select == "1": # 셀렉 인풋이 문자로 입력받았기 때문에 "1" 라고 표시
        print("로그인(회원가입)메뉴로 진입합니다.")

        subRun = True
        while subRun : # 부메뉴 반복용
            print(memberMenu) # 회원관리 메뉴가 출력
            subSelect = input("원하는 메뉴의 번호를 입력하세요 : ")
            if subSelect == "1":
                if session is [idx] :
                    print("이미 로그인중")
                    continue
                else :
                    print("회원가입 메뉴로 진입합니다.")
                    id = input(" id : ")
                    pw = input(" PW : ")
                    print("""회원 유형의 번호를 입력하세요
1. 교수
2. 학생
3. 학부모
4. 행정 
""")
                    groupSelect = input(" : ")
                    if groupSelect == "1":
                        group = "pro"
                    elif groupSelect == "2":
                        group = "stu"
                    elif groupSelect == "3":
                        group = "par"
                    elif groupSelect == "4":
                        group = "staf"


                    else:
                        print("잘못된 입력")
                        continue

                    print(" id : " + id)
                    print(" pw : " + pw)
                    if input("입력된 정보 맞으면 y 눌러 : ") == "y":
                        ids.append(id)
                        pws.append(pw)
                        groups.append(group)
                        sn = len(sns) + 1
                        sns.append(sn)

                        print("회원가입이 완료 되었습니다.")
                        print("다시 로그인 해 주세요")
                    else:
                        print("회원가입취소")
                        continue


            elif subSelect == "2":
                print("로그인 메뉴로 진입합니다.")

                id = input(" ID :") #입력 받은 값 변수에 넣어주고
                pw = input(" PW :")
                if id in ids:        # 변수에 넣은 값을 검증 하기
                    idx = ids.index(id)
                    if pws[idx] == pw:
                        session = idx
                        print(f"회원번호 : {sns[idx]}  / 권한 : {groups[idx]}")
                        print("로그인성공")
                    else:
                        print("입력하신 아이디와 비밀번호가 일치하지 않습니다.")
                        print("처음부터 다시 입력해주세요\n")

                else :
                    print("아이디를 찾을 수 없습니다. ")


            elif subSelect == "3" :
                if session is None :
                    print("로그인 후 이용 가능합니다.")
                    continue
                print("회원 수정 메뉴로 진입합니다.")

                print("정보 수정")
                print("1. id 변경")
                print("2. pw 변경")
                print("0. 돌아가기")
                choice = input("선택 : ")

                if choice == "1":
                    ids[session] = input("새 id : ")
                    print("id 변경 완료" + ids[session])

                elif choice == "2":
                    pws[session] = input("새 pw : ")
                    print(" pw 변경 완료 " + pws[session])

                elif choice == "0":
                    continue

                else:
                    print("잘못된 선택")


            elif subSelect == "4":
                if session is None :
                    print("로그인 후 이용 가능합니다.")
                    continue
                print("회원 탈퇴 메뉴로 진입합니다.")
                print(f"회원번호 : {sns[idx]}  / {groups[idx]} 의 탈퇴를 진행할까요? ")
                if input("탈퇴를 원하면 y :") == "y" :
                    sns.pop(idx)
                    ids.pop(idx)
                    pws.pop(idx)
                    groups.pop(idx)
                    print("회원 탈퇴 완료")
                else :
                    print("잘못입력")

            elif subSelect == "0":
                print("회원 관리 메뉴를 종료합니다.")
                subRun = False # 회원 while 종료 !

            else : # 없는 값 넣었을 경우
                print ("잘못된 입력")

    elif select == "2":
        #main에서 로그인이 유지되게?
        #로그인 안하고 접근 못하게?
        print("성적관리메뉴로 진입합니다.")
        subRun = True
        while subRun:  # 부메뉴 반복용
            print(scoreMenu)  # 회원관리 메뉴가 출력
            subSelect = input("원하는 메뉴의 번호를 입력하세요 : ")
            if subSelect == "1":
                # 교수만 접근 가능한 검증 넣기?
                print("성적을 입력합니다.")


    elif select == "3":
        print("게시판메뉴로 진입합니다")
    elif select == "4":
        print("관리자 메뉴로 진입합니다.")
    elif select == "0":
        print("LMS 프로그램을 종료합니다.")
