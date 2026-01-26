import os
from domain.Member import Member
from common.Session import Session

# 회원 데이터 파일 경로
FILE_PATH = "data0122/members.txt"


class MemberService:
    """
    회원 관련 비즈니스 로직 담당 클래스
    - 회원가입
    - 로그인 / 로그아웃
    - 회원정보 수정
    - 회원탈퇴
    - 관리자 기능
    """

    members = []   # Member 객체 리스트

    # ===============================
    # 파일 로드
    # ===============================
    @classmethod
    def load(cls):
        cls.members = []

        if not os.path.exists(FILE_PATH):
            return

        with open(FILE_PATH, "r", encoding="utf-8") as f:
            for line in f:
                cls.members.append(Member.from_line(line))

    # ===============================
    # 파일 저장
    # ===============================
    @classmethod
    def save(cls):
        with open(FILE_PATH, "w", encoding="utf-8") as f:
            for m in cls.members:
                f.write(m.to_line() + "\n")

    # ===============================
    # 회원가입 (Create)
    # ===============================
    @classmethod
    def signup(cls):
        print("\n[회원가입]")

        uid = input("아이디: ")

        # 아이디 중복 체크
        if any(m.uid == uid for m in cls.members):
            print("이미 존재하는 아이디입니다.")
            return

        pw = input("비밀번호: ")
        name = input("이름: ")

        member = Member(uid, pw, name)
        cls.members.append(member)
        cls.save()

        print("회원가입 완료")

    # ===============================
    # 로그인 (Read + Session)
    # ===============================
    @classmethod
    def login(cls):
        print("\n[로그인]")

        uid = input("아이디: ")
        pw = input("비밀번호: ")

        for m in cls.members:
            if m.uid == uid:
                if not m.active:
                    print("비활성화된 계정입니다.")
                    return

                if m.pw == pw:
                    Session.login(m)
                    print(f"{m.name}님 로그인 성공 ({m.role})")
                    return
                else:
                    print("비밀번호가 틀렸습니다.")
                    return

        print("존재하지 않는 아이디입니다.")

    # ===============================
    # 로그아웃
    # ===============================
    @classmethod
    def logout(cls):
        if not Session.is_login():
            print("로그인 상태가 아닙니다.")
            return

        Session.logout()
        print("로그아웃 완료")

    # ===============================
    # 내 정보 수정 (Update)
    # ===============================
    @classmethod
    def modify(cls):
        if not Session.is_login():
            print("로그인 후 이용 가능합니다.")
            return

        member = Session.login_member

        print("""
[내 정보 수정]
1. 이름 변경
2. 비밀번호 변경
0. 취소
""")
        sel = input("선택: ")

        if sel == "1":
            member.name = input("새 이름: ")
        elif sel == "2":
            member.pw = input("새 비밀번호: ")
        else:
            return

        cls.save()
        print("정보 수정 완료")

    # ===============================
    # 회원탈퇴 / 비활성화 (Delete)
    # ===============================
    @classmethod
    def delete(cls):
        if not Session.is_login():
            print("로그인 후 이용 가능합니다.")
            return

        member = Session.login_member

        print("""
[회원 탈퇴]
1. 완전 탈퇴
2. 계정 비활성화
""")
        sel = input("선택: ")

        if sel == "1":
            cls.members.remove(member)
            Session.logout()
            cls.save()
            print("회원 탈퇴 완료")

        elif sel == "2":
            member.active = False
            Session.logout()
            cls.save()
            print("계정 비활성화 완료")

    # ===============================
    # 관리자 메뉴
    # ===============================
    @classmethod
    def admin_menu(cls):
        if not Session.is_login() or not Session.login_member.is_admin():
            print("관리자만 접근 가능합니다.")
            return

        while True:
            print("""
[관리자 메뉴]
1. 회원 목록 조회
2. 권한 변경
3. 블랙리스트 처리
0. 뒤로가기
""")
            sel = input("선택: ")

            if sel == "1":
                cls.list_members()
            elif sel == "2":
                cls.change_role()
            elif sel == "3":
                cls.block_member()
            elif sel == "0":
                break

    # ===============================
    # 관리자 기능들
    # ===============================
    @classmethod
    def list_members(cls):
        print("\n[회원 목록]")
        for m in cls.members:
            print(m)

    @classmethod
    def change_role(cls):
        uid = input("대상 아이디: ")
        for m in cls.members:
            if m.uid == uid:
                m.role = input("admin / manager / user: ")
                cls.save()
                print("권한 변경 완료")
                return
        print("회원 없음")

    @classmethod
    def block_member(cls):
        uid = input("대상 아이디: ")
        for m in cls.members:
            if m.uid == uid:
                m.active = False
                cls.save()
                print("블랙리스트 처리 완료")
                return
        print("회원 없음")
