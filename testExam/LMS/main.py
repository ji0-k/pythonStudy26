from testExam.LMS.service import *
from testExam.LMS.common import Session

def main():
    MemberService.load()

    run = True
    while run:
        print("""
=================
 MBC 아카데미 LMS 
=================
1. 회원가입
2. 로그인/로그아웃
3. 정보 보기 / 변경
4. 관리자메뉴
5. 성적관리
6. 게시판
----------------
0. 종료하기
""")
        member = Session.login_member

        if member is None :
            print("현재 로그인상태가 아닙니다.")
        else:
            print(f"{member.name}님 환영합니다. ")

        sel = input(">>> ")
        if sel == "1": MemberService.signup()
        elif sel == "2": MemberService.loginout_menu()
        elif sel == "3": MemberService.profile_menu()
        elif sel == "4": MemberService.admin_menu()
        elif sel == "5": pass#ScoreService.run()
        elif sel == "6": pass#BoardService.run()
        elif sel == "0":
            print("프로그램 종료")
            run = False

if __name__ == "__main__":
    main()