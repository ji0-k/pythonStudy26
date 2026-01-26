# 비회원용 게시판을 만들어 보자
#C : 게시글 등록
#R : 게시글 전체보기(List) , 게시글 자세히보기
#U : 게시글 수정
#D : 게시글 삭제

# 사용할 변수 리스트 # 위에 쓴 변수는 전역변수 프로그램전체에서 사용 (global)

run = True # while 문 프로그램 구동 중
borad_nos = [] #중복되지 않는 유일한 값, null은안됨 , 공백 안됨 , not null
borad_titles = [] #게시글의 제목
borad_contents = [] # 게시글의 내용
borad_writers = [] # 글쓴이
borad_passwords = [] # 게시글의 수정 삭제용
borad_hits = [] #좋아요 수
borad_visitcounts = [] # 조회 수

board_home ="""
===========================
!비회원 전용 Boarrrrdddddd!
===========================
1. 게시물 등록
2. 게시판 보기
3. 게시물 자세히보기
4. 게시물 수정
5. 게시물 삭제
6. 게시판 프로그램 종료
===========================
"""

# 프로그램 실행문
while run :
    print(board_home)
    select = input("1~6 중 원하는 메뉴의 숫자를 입력하세요 : ") # while문 안에서 존재하는 1회용 지역변수(local)
    if select == "1" : #"" : input으로 받은 값은 문자로 인식되어서
        print("[게시물 등록하기를 선택하셨습니다.]")
        # 게시글 등록용 코드 추가
        # 게시글의 번호는 프로세서가 자동처리되어 입력되게한다.
        title = input("제목 : ")
        contnet = input("내용 : ")
        writer = input("작성자 : ")
        password = input ("게시글 암호 : ")

        # 입력받은 정보를 확인시켜준다.
        print(f"제목 : {title}")
        print(f"내용 : {contnet}")
        print(f"작성자 : {writer}, 암호 : {password}")
        choose = input("저장하려면 y를 누르세요 :")
        if choose == "y" :
            borad_titles.append(title)
            borad_contents.append(contnet)
            borad_writers.append(writer)
            borad_passwords.append(password)

            #제목의 리스트에서 인덱스를 추출하여 +1 한값이 No.로 1부터 입력됨
            for idx in range(len(borad_titles)):
                borad_nos.append(idx+1)
            borad_hits.append(0)
            borad_visitcounts



    elif select == "2" :
        print("[게시판 보기를 선택하셨습니다.]")
    elif select == "3" :
        print("[게시물 자세히 보기를 선택하셨습니다.]")
    elif select == "4" :
        print("[게시물 수정을 선택하셨습니다.]")
    elif select == "5" :
        print("[게시물 삭제를 선택하셨습니다.]")
    elif select == "6" :
        print("게시판 프로그램을 종료합니다.")
        run = False #

    else :
        print("잘못된 입력입니다. 입력된 번호를 확인해주세요.")
