# 회원 관리용 코드를 만든다
# C 회원 추가
# R (관리자일경우) 전체회원보기, (일반회원) 로그인
# U (관리자일경우) 회원차단,암호변경문의, (일반회원) 내정보수정, 암호변경
# D 회원 탈퇴

# 메뉴 구현
run = True
# 프로그램 동작중을 관리하는 변수 , 종료시에는 false 처리

menu = """
==============================================================
                MBC 아카데미 회원 관리 프로그램
==============================================================
1. 회원가입
2. 로그인
3. 회원정보보기
4. 내정보수정
5. 프로그램 종료
==============================================================
"""

# 사용할 리스트 변수를 생성한다.
sns = ["1","2","1234"] #학번,사용자고유번호
ids = ["kjy", "yky", "1234"] #로그인용 아이다
passwords = ["1234","4567", "1234"] #로그인용 비밀번호
names = ["관리자", "윤경영", "1234"] # 사용자명
emails = ["admin@mbc.com", "yky@mbc.com", "1234"] # 이메일주소
admins= [True,False,False] # 관리자 유무 . 관리자 : true, 일반 사용자 : false
login_user = None #로그인 상태를 유지할 변수 , 빈공간으로 만들어 두기

while run :
    print(menu)
    select = input("1~5숫자를 입력하세요 : ")
    if select == "1" :
        print("회원 가입 메뉴에 진입하였습니다.")
        while True :
            sn = input("사번을 입력하세요 : ")
            id = input("아이디를 입력하세요 : ")
            pw = input("비밀번호를 입력하세요 : ")
            pw2 = input ("동일한 비밀번호를 한번 더 입력하세요 : ")
            if pw == pw2 :
                print("입력하신 비밀번호가 일치합니다.")
                break
            else:
                print("입력하신 비밀번호가 일치하지 않습니다.")
                print("처음부터 다시 입력해주세요\n")

        name = input("이름을 입력하세요 : ")
        email = input ("이메일을 입력하세요 : ")
        admin = False
        print ("입력된 값이 정확한지 확인하시고 y를 누르면 가입됩니다.")
        print ("이름 : " + name)
        print ("id : " + id)
        print ("pw : " + pw)

        if input("y/n : ") == "y" :
            sns.append(sn) #가입된 정보 추가
            ids.append(id)
            passwords.append(pw)
            names.append(name)
            emails.append(email)
            admins.append(admin)
            print("입력이 완료 되었습니다.")
            print("새로 로그인 해주세요 ")
        else:
            print("처음부터 다시 진행하세요")

    elif select == "2" :
        print ("로그인 메뉴에 진입하였습니다.")

        id = input("아이디를 입력하세요 : ")
        pw = input("비밀번호를 입력하세요 : ")

        if id in ids : # 입력받은 id가 ids리스트에 있다면
            idx = ids.index(id) # 입력받은 아이디의 인덱스를 idx변수로 지정한다
            if passwords[idx] == pw : #입력받은 pw와 입력받아나온idx 인덱스와 같은 pw인덱스에있는 pw와 같으면
                login_user = idx # 그 idx의 정보로 로그인 한 유저로 인식
                print(f"{names[idx]} 님 로그인 성공 ")

                if admins[idx] : # admins리스트에 [idx] 에 0자리, True라고 써있으니까 그냥 if True면 프린트~
                    print ("관리자 계정입니다.")
                else :
                    print ("일반 회원 계정입니다.")
            else:
                print("입력하신 아이디와 비밀번호가 일치하지 않습니다.")
                print("처음부터 다시 입력해주세요\n")
                print(menu)
        else :
            print("존재하지 않는 아이디 입니다.")

    # 메뉴 1-3 회원 정보 보기
    elif select == "3" :
        if login_user == None :
            print("로그인 후 이용 가능합니다.")
            continue
        if admins[login_user] : #관리자 모드
            print("""
[ 전체 회원 목록 ] """)
            for i in range(len(ids)):
                print(f"{i+1},사번:{sns[i]}ㅣ아이디 : {ids[i]}ㅣ 비밀번호 : {passwords[i]} ㅣ 이름 : {names[i]} ㅣ이메일 : {emails[i]} ㅣ관리자 {admins[i]}")

        print ("회원 정보보기 메뉴에 진입하였습니다. ")
        print(f"""
[ 내 정보 보기 ]
사번 : {sns[login_user]}
아이디 : {ids[login_user]}
이름 : {names[login_user]}
이메일 : {emails[login_user]}

1.되돌아가기
2.로그아웃하기
            
            """.strip())
        choice = input("선택 : ")
        if choice == "1" :
            continue
        elif choice == "2" :
            login_user = None
        else :
            print("잘 못 입력하셨습니다. ")

    # 메뉴 1-4 회원 정보 수정
    elif select == "4" :
        if login_user is None:
            print("로그인 후 이용 가능합니다.")
            continue  # 상위 단계로 돌아감
        print("내 정보 수정 메뉴에 진입하였습니다.")
        print("""
               @내정보수정@
               1. 이름 변경
               2. 이메일변경
               3. 비밀번호 변경
               4. 되돌아가기
               5. 로그아웃하기
               """)

        choice = input("선택 : ")
        if choice == "1":
            names[login_user] = input("새이름 : ")
            print("이름 변경 완료" + names[login_user])
        elif choice == "2":
            emails[login_user] = input("새 이메일 :")
            print("이메일 변경 완료" + emails[login_user])
        elif choice == "3":
            passwords[login_user] = input("새 비밀번호 : ")
            print("비밀번호 변경 완료" + passwords[login_user])
        elif choice == "4":
            continue
        else:
            login_user = None
            print("정상적으로 로그아웃 되었습니다. ")

    elif select == "5" :
        print("회원 관리 프로그램을 종료합니다.")
        run = False
    else :
        print("입력 번호를 다시 한번 확인 하여 1~5 사이 숫자를 입력하세요")


