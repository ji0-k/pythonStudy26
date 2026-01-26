import os # .txt파일 처리용
from enum import member

from domain.Member import Member
from common.Session import Session

#          상위 폴더  폴더 모듈          클래스

#회원 데이터 파일 경로
FILE_PATH = "data0122/members.txt"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "..","data0122","member.txt.txt")

class MemberService:
    # 회원관련 비즈니스로직 담당하는 클래스
    # CRUD 담당
    # 회원가입, 로그인,로그아웃, 정보수정, 탈퇴 ,관리자기능 등
    # 여기도 __init__() 메서드는 생략 -> @classmethod로 구현 연습


    members = [] # 회원들을 보관하는 리스트

    #-------파일에 있는 값 객체로 만들어 불러오기------------
    @classmethod
    def load(cls) : # 사용법 MemberService.load()
        # 파일에 있는데이터를 1줄씩 읽어 Member 객체로 만들고 리스트에 추가
        cls. members = []

        if not os.path.exists(FILE_PATH):
            return


        with open(FILE_PATH, "r", encoding="utf-8") as f:
            for line in f:
                cls.members.append(Member.from_line(line))
                #                   Member객체에 있는 .from_line() 메서드실행
                # members 리스트에 추가해라
    #--------------------------------------------------------
    #----------객체를 문자열로 변환하여 파일에 저장---------------
    @classmethod
    def save(cls) :
        # 메모리에 있는 members[]리스트를 .txt파일로 저장
        with open(FILE_PATH, "w", encoding="utf-8") as f:
            for m in cls.members : # members[]에있는 1줄씩 m 변수에 넣은
                f.write(m.to_line() + "\n")
                #       Member객체에 있는 .to_line()메서드
                # f"{self.uid}{self.pw}{self.name}{self.role}{self.active}"
                # f.write()는 파일에 저장해라
    #------------------------------------------------------------

    #-----------회원가입-------------------------------------
    @classmethod
    def signup(cls) :
        print("\n[회원가입]")

        uid = input("ID : ")
        #ID 중복체크
        if any(m.uid == uid for m in cls.members) : #any : 둘다 맞으면
            #                       .txt파일에 있는 members리스트에 넣었음
            #                 m변수에 1개씩 꺼내서 넣음
            # m. uid for에서 찾은 객체의 uid와
            # 객체로 만든 members에서 1개씩 찾아와 uid와 같은게 있으면 True
            # any() -> True 가 나오면 즉시 종료
            # 하나라도 True가나오면 True, 전부 False면 False처리
            print("이미 존재하는 아이디입니다.")
            return
        pw = input("PW : ")
        name = input("NAME : ")
        member = Member(uid, pw, name)
        cls.members.append(member)
        cls.save()
        cls.load()

        print("회원가입완료")
    #-----------------------------------------------------------

    #------------로그인-----------------------------------------
    @classmethod
    def login(cls):
        print("\n[로그인]")

        uid = input("ID : ")
        pw  = input("PW : ")

        for m in cls.members :
            if m.uid == uid :
                if not m.active:
                    print("비활성화 계정")
                    return
                if m.pw == pw :
                    Session.login(m) # 일치하면 Session객체에 member객체를 넣음
                    print(f"{m.name}님 로그인 성공 ({m.role})")
                    print(Session, "세선객체 출력테스트") #def __str__(self): 활용
                    return
                else :
                    print("비밀번호가 틀렸습니다.")
                    return
        print("존재하지 않는 아이디")
    #------------------------------------------------------

    #-----------로그아웃------------------------------------
    @classmethod
    def logout(cls) :
        if not Session.is_login():
            print("로그인 상태가 아닙니다")
            return
        Session.logout() # session = None
        print("로그아웃 완료")
    #-------------------------------------------------------

    #----------내 정보 수정---------------------------------
    @classmethod
    def modify(cls) :
        if not Session.is_login() :
            print("로그인 후 이용")
            return

        members = Session.login_member

        print("""
[내 정보 수정]
1. 이름 변경
2. 비밀번호 변경
0. 취소
""")
        sel = input("선택 : ")

        if sel == "1" : member.name = input("NAME : ")

        elif sel == "2" : member.pw = input("PW : ")

        elif sel == "0" :
            return

        else :
            print("잘못된 접근")
            return

        cls.save()
        print("정보 수정 완료")
    #-------------------------------------------------------------

    #----------회원 탈퇴, 비활성화----------------------
    @classmethod
    def delete(cls):
        if not Session.is_login() :
            print("로그인 후 이용")
            return

        member = Session.login_member
        print("""
1. 회원 탈퇴
2. 계정 비활성화 
0. 뒤로가기""")
        sel = input(">>>")
        if sel == "1" :
            cls.members.remove(member)
            Session.logout()
            cls.save()
            print("회원탈퇴완료")

        elif sel == "2" :
            member.active = False
            Session.logout()
            cls.save()
            print("계정비활성화완료")
    #-----------------------------------------------

    #----------관리자 메뉴--------------------------
    @classmethod
    def admin_menu(cls) :
        if not Session.is_login() or not Session.login_member.is_admin():
            print("관리자만 접근 가능")
            return

        while True :
            print("""
[관리자 메뉴]
1. 회원 목록 조회
2. 권한 변경
3. 블랙리스트 처리
0. 뒤로가기""")
            sel = input(">>>")
            if sel == "1" :
                cls.list_members()
            elif sel == "2" :
                cls.change_role()
            elif sel == "3" :
                cls.block_member()
            elif sel == "0" :
                break
            else :
                print("잘못된 접근")
    #-------------------------------------------------
    #------관리자 회원 리스트 조회---------------------
    @classmethod
    def list_members(cls) :
        print("\n[회원목록]")
        for m in cls.members:
            print(m)
    #-----------------------------------------------
    #-------관리자 권한부여--------------------------
    @classmethod
    def change_role(cls) :
        uid = input("대상 ID : ")
        for m in cls.members :
            if m.uid == uid :
                m.role = input("admin/manage/user : ")
                cls.save()
                cls.load()
                print("권한 변경 완료")
                return
    #------------------------------------------------
    #--------회원 차단 관리----------------------------
    @classmethod
    def block_member(cls) :
        uid = input("대상 ID : ")
        for m in cls.members :
            if m.uid == uid :
                m.active = False
                cls.save()
                cls.load()
                print("회원 차단 완료")
                return
        print("잘못된 입력")
    #----------------------------------------------








