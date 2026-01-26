import os

#경로
from testExam.LMS.common import Session
from testExam.LMS.domain import *

#회원파일 경로
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "..","data","member.txt")

class MemberService:
    members = []

    @classmethod
    def load(cls): # .txt파일->데이터로 불러
        cls.members = []
        if not os.path.exists(FILE_PATH):
            cls.save()
            return
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            for line in f:
                cls.members.append(Member.from_line(line))

    @classmethod
    def save(cls): # 데이터->.txt파일로저장
        with open(FILE_PATH, "w", encoding="utf-8") as f:
            for m in cls.members:
                f.write(m.to_line() + "\n")

    @classmethod
    def signup(cls):
        print("[회원가입]")
        uid = input("ID :")
        if any (m.uid == uid for m in cls.members) :
            print("ID 중복")
            return
        pw = input("PW :")
        name = input("NAME :")
        member = Member(uid, pw, name)
        cls.members.append(member)
        cls.save()
        print("[회원가입 완료]")

    @classmethod
    def loginout_menu(cls):
        print("""
-----------------
1. 로그인 하기
2. 로그아웃 하기
-------------------
0. 취소""")
        sel = input("메뉴번호 :")
        if sel == "1": MemberService.login()
        elif sel == "2": MemberService.logout()
        elif sel == "0": return
        else :
            print("잘못된 접근")
            return

    @classmethod
    def login(cls):
        print("[로그인]")
        uid = input("ID :")
        pw = input("PW :")
        for m in cls.members:
            if m.uid == uid:
                if not m.active:
                    print("계정 비활성화")
                    return

                if m.pw == pw :
                    Session.login(m)
                    print(f"{m.name}님 로그인")
                    return
                else :
                    print("PW오류")
                    return

        print("ID오류")

    @classmethod
    def logout(cls):
        if not Session.is_login():
            print("비로그인상태")
            return
        Session.logout()
        print("로그아웃완료")

    @classmethod
    def profile_menu(cls):
        if not Session.is_login():
            print("로그인 후 이용")
            return
        member = Session.login_member

        print("""
-----------------
1. 내 정보 보기
2. 내 정보 수정
-------------------
0. 취소""")
        sel = input("메뉴번호 :")
        if sel == "1":
            print("[내 정보 보기]")
            print(f" ID : {member.uid}")
            print(f"비밀번호 : {member.pw}")
            print(f"이름 : {member.name}")
            print(f"회원등급 : {member.role}")
            print(f"계정상태 ; {'활성'if member.active else '비활성'}")
        elif sel == "2":
            print("""
----------------
1. 이름변경
2. 비밀번호 변경
3. 탈퇴 및 비활성화
-----------------
0 취소 """)
            sel2 = input("메뉴번호 :")
            if sel2 == "1":
                member.name = input("변경할NAME :")
            elif sel2 == "2":
                member.pw = input("변경할PW :")
            elif sel2 == "3":
                print("""
----------------
1. 회원 탈퇴
2. 계정 비활성화
-----------------
0 취소 """)
                sel3 = input("메뉴번호 :")
                if sel3 == "1":
                    cls.members.remove(member)
                    Session.logout()
                    cls.save()
                    print("회원탈퇴완료")
                elif sel3 == "2":
                    member.active = False
                    Session.logout()
                    cls.save()
                    print("계정 비활성화 완료")
                elif sel3 == "0":
                    return
                else:
                    print("잘못된접근")
                    return

            elif sel2 == "0":
                return
            else :
                print("잘못된접근")
                return
            cls.save()
            cls.load()
        else :
            print("잘못된접근")
            return

    @classmethod
    def admin_menu(cls):
        if not Session.is_login() or not Session.login_member.is_admin():
            print("관리자만 접근 가능")
            return
        while True :
            print("""
----------------
1. 회원 목록 조회
2. 권한 변경
3. 블랙리스트 처리
-----------------
0 취소 """)
            sel = input("메뉴 번호 : ")
            if sel == "1":
                cls.list_members()
            elif sel == "2":
                cls.change_role()
            elif sel == "3":
                cls.block_member()
            elif sel == "0":
                break
            else :
                print("잘못된접근")
                return

    @classmethod
    def list_members(cls):
        print("[회원목록]")
        for m in cls.members :
            print(m)


    @classmethod
    def change_role(cls):
        uid = input("변경할ID :")
        for m in cls.members :
            if m.uid == id :
                m.role = input("admin / manage / user :")
                cls.save()
                cls.load()
                print("권한변경완료")
        print("ID확인필요")

    @classmethod
    def block_member(cls):
        uid = input("차단할 ID :")
        for m in cls.members :
            if m.uid == id :
                m.active -= False
                cls.save()
                cls.load()
                print("계정 차단 완료")
        print("ID확인필요")