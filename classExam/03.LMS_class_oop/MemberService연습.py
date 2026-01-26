# Member 객체를 CRUD 기능 넣기
# 메뉴 구현
# 텍스트 파일 처리 (읽기, 저장, 수정)
# add, login, logout, modify, delete

import os
from Member import Member #Member.py 안에 정의된 Member클래스를 여기서 가져다 쓰겠다
from mbc_lms_function_exam.MemberExam import active


# Member.py 는 파일=모듈
# Member 는 파일안에 클래스 = 설계도
# m = Member(...) = 객체 생성
#from Member import Member = .py모듈안에 객체생성 설계도 가져오기

class MemberService : #클래스 생성은 여기서 함!
    #-------------클래스 생성시 초기값 관리 -----------------
    def __init__(self, file_name="1021member연습.txt"):
        self.file_name = file_name
        self.members = []
        self.session = None
        self.load_members()
    #-----------------------------------------------------

    #-----------------메인 루프 메서드-----------------------
    def run(self) :
        while True :
            self.main_menu() # 메인들어가서 보일메뉴
            sel = input(">>>")

            if sel == "1" :  self.add_member()
            elif sel == "2" : self.log_member()
            elif sel == "3" : self.modify_member()
            elif sel == "4" : self.delete_member()
            elif sel == "0" : break
            else : print("잘못된 접근")
    #-----------------------------------------------------

    #-------------.txt파일에서 객체로변환 해서 가져오기--------
    def load_members(self):
        if not os.path.exists(self.file_name) : # 여기서 import os 상단에 작성
            self.save_members()
            return
        # 파일이 없으면 만들어서 save_members로 반환해
        self.members = []
        # 아무 회원도 없는 상태로 초기화 한뒤
        with open(self.file_name,"r", encoding = "utf-8") as f :
        # 파일을 읽기모드로 열어서 f라 정하겠다
            for line in f :
                self.members.append(Member.from_line(line))
               #                     파일의 각 줄을 읽어 문자열 -> Member객체로 변환한다.
               # 반환된 객체를 members 리스트에 저장한다.
    #------------------------------------------------------
    #---------객체를 문자열로 변환하여 .txt파일에 저장하기--------
    def save_members(self) :
        with open(self.file_name,"w", encoding = "utf-8") as f :
            #파일열어, 쓰고저장가능으로, 그건 f라하겠다
            for member in self.members :
                #members 리스트 안에 들어잇는 Member객체 하나를 member라고 부르겠다
                f.write(member.to_line())
                #       Member 객체 하나를 문자열 한줄로 변환해서
                # 파일에써라.
    #------------------------------------------------------



    def main_menu(self):
        print("""
=================================
 회원 관리 서비스 - Member 객체 기반
--------------------------------
1. 회원가입
2. 로그인 / 로그아웃
3. 회원정보 수정 
4. 회원 탈퇴
-------------------------------
0. 프로그램 종료
================================""")

#---------------회원가입------------------------
    def add_member(self): #회원가입
        print("\n[회원가입]")
        uid = input("ID : ")
        if self.find_member(uid) :
            print("이미 존재하는 ID")
            return
        pw = input("PW : ")
        name = input("NAME : ")
        role = "user"
        # Member.py의 초기값 설정에서 이미 active == True값 지정해줫기때문에 회원가입할때 안해도댐
        self.members.append(Member(uid,pw,name,role))
        # Member클래스를 이용해 입력받은 값을 가진 Member객체 하나를 생성해서 members 리스트에 추가한다
        self.save_members()
        self.load_members()
#-----------------------------------------------
#----------로그인 , 로그아웃----------------------
    def log_member(self): #로그인아웃
        if self.log_session() :
            print("\n[로그아웃]")
            print(f"{self.session.name} 님 로그인중 ")
            sel = input("로그아웃 하려면 y : ") .strip().lower()

            if sel == "y" :
                print(f"{self.session.name}님 로그아웃")
                self.session = None

            else :
                print("로그인 상태 유지")
            return

        print("\n[로그인]")
        uid = input("ID : ")
        pw = input("PW : ")

        member = self.find_member(uid)
        if not member :
            print("존재하지 않는 ID")
            return
        if not member.active :
            print("비활성화 계정")
            return
        if member.pw != pw :
            print("비밀번호가 일치하지 않습니다.")
            return
        self.session = member
        print(f"{member.name}님 로그인")

        if member.role == "admin" :
            self.admin_member()

    def modify_member(self): #수정
        pass

    def delete_member(self): #탈퇴
        pass

    def log_session(self) : #True면 로그인상태 , False면 비로그인 상태
        return self.session is not None

    def admin_member(self):
        pass

    def find_member(self, uid):
        pass



