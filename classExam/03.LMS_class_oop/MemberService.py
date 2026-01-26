import os

# Member 객체를 CURD 기능을 넣는다
# 메뉴 구현
# 텍스트파일 처리 (파일 읽기, 파일 저장)
# 회원가입, 로그인, 로그아웃, 회원수정, 회원탈퇴

from Member import Member # 회원 객체 추가 연결
#사용법 member.txt = Member() -> 객체가 생성됨
#      member.txt.필드/메서드 =??? 원하는거 넣고 쓰기


class MemberService:
    #------------클래스 생성시 초기값 관리-----------------------
    def __init__(self, file_name="1021member.txt"):

        self.file_name = file_name
        self.members = [] #회원들을 리스트로 만들어 Member()객체를 담는다
        self.session = None
        self.load_members() # 아래쪽에 메서드 호출
    #---------------------------------------------------------

    #---------------주실행 문
    def run (self):
        while True:
            self.main_menu()
            sel = input(">>>")

            if sel == "1" : self.member_add()
            elif sel == "2": self.member_login()
            elif sel == "3": self.member_logout()
            elif sel == "4": self.member_modify()
            elif sel == "5": self.member_delete()
            elif sel == "0": run = False
            else :
                print("잘못된 접근")


    def load_members(self):  # 파일에서 메모리로 불러온다
        if not os.path.exists(self.file_name) : # 맨위에 import os
            self.save_members()
            return
        self.members = [] #메모리에 남은 값을 초기화
        with open(self.file_name, "r", encoding = "utf-8") as f:
        # 0102members.txt.파일이름 , 읽기전용으로 한글지원 후 f 변수에 넣는다?
            for line in f :
                self.members.append(Member.from_line(line))
                #                   Member객체에 .from_line() 메서드 실행
                #                         1줄을 가져와클래스로 만듦
                # 0121members.txt뒤에 추가

    def main_menu(self):
        print("""
===== 회원관리 프로그램 (Member 객체 기반) =====
1. 회원가입
2. 로그인
3. 로그아웃
4. 회원정보수정
5. 회원탈퇴
--------------------------------------------
0. 종료
============================================""")

    #---------------------회원가입-------------------------------------
    def member_add(self):
        print("\n회원가입")
        uid = input("ID : ")

        if self.find_member(uid) : # 자주쓰는 중복 코드로 메서드 처리함 로그인, 수정, 삭제 등
            print("이미 존재하는 ID")
            return
        pw = input("PW : ")
        name = input("Name : ")
        role = "user"

        self.members.append(Member(uid,pw,name,role)) # Member클래스에 생성하면서 초기값 설정한 곳에 members가들어간다
        # Member 클래스의 init메서드로 바로 들어가 객체 생성
        self.save_members() # 파일로 기록
        self.load_members() # 데이터값으로 불러와
        print("회원가입 완료")
    #------------------------------------------------------------------

    #--------------------로그인-----------------------------------------
    def member_login(self):
        print("\n[로그인]")
        uid = input("ID : ")
        pw = input("PW : ")

        member = self.find_member(uid)

        if not member :
            print("존재 하지 않는 ID")
            return

        if not member.active :
            print("비활성화 계정")
            return


        if member.pw == pw :
            self.session = member
            print(f"{member.name}님 로그인 성공 ({member.role})")
            if member.role == "admin" :
                self.member_admin()

        else :
            print("비밀번호 확인 요망")
    #--------------------------------------------------------------------

    #---------------로그아웃----------------------------------------------
    def member_logout(self):
        pass

    def member_modify(self):
        pass

    def member_delete(self):
        pass

    #파일 저장용 코드
    def save_members(self):
        with open(self.file_name,"w", encoding = "utf-8") as f:
            for member in self.members:
                f.write(member.to_line()) # to_line~ 파일저장용
                #       Member객체의 메서드를 사용하여 1줄씩 기록

    #----------ID 이용해 members에서 객체 찾는 공통 메서드-------------------
    def find_member(self, uid):
        for member in self.members:
            # members 리스트에서 1개씩 member객체를 가져와
            if member.id == uid: #가져온 member객체ID 와 전달받은 ID가 같은지
                print(member.name,"님을 찾았습니다.")
                return member #같은 ID가 있으면 member.txt 객체를 return
        return None
    #-----------------------------------------------------------------

    #--------admin일경우 진입 가능 메서드--------------------------------
    def member_admin(self):
        subrun = True
        while subrun :
            print("""
[관리자 메뉴]
1. 회원리스트 조회
2. 비밀번호 변경
3. 블랙리스트 처리
4. 권한변경
-----------------
0. 종료하기 """)
            sel = input(">>>")

            if sel == "1" :
                self.show_member_list() #회원리스트 보이게

            elif sel == "2" :
                uid = input("대상 ID : ")
                member = self.find_member(uid)
                if member :
                    member.pw = input("PW : ")

            elif sel == "3" :
                uid = input("대상 ID : ")
                member = self.find_member(uid)
                if member :
                    member.active = False
                    self.save_members()
                    print("비활성화 계정 처리 완료")
                else :
                    print("존재하지 않는 계정 정보")

            elif sel == "4" :
                uid = input("대상 ID : ")
                member = self.find_member(uid)
                if member :
                    member.role = input("admin/manager/user : ")
                    self.save_members()
                    print("권한 변경 완료")
                pass

            elif sel == "0" :
                print("프로그램이 종료되었습니다")
                subrun = False

            else :
                print("잘못된 접근")
    #-------------------------------------------------------------

    #---------------회원 리스트 admin---------------------

    def show_member_list(self):
        print("\n[회원 목록]")
        print("-"*60)
        print(f"{'ID':10}{'Name':10}{'권한':10}{'상태'}")
        print("-" * 60)

        for member in self.members:
            #members리스트에 있는 객체를 하나씩 가져와 member에 넣음
            status = "활성" if member.active else "비활성"
            # member.txt.active == True이면 "활성" , 아니면 "비활성"
            print(f"{member.id:10}{member.name:10}{member.role:10}{status}")

        print("-"*60)





























