# 주 실행 코드

from service0122 import * # /Service/__init__.py에 __all__에 있는 모든 것을 가져옴
from common0122.Session import Session
#    하위폴더.모듈            클래스

def main():
    #프로그램 시작 시 데이터 로드
    MemberService.load()
    run = True
    while run:
        print("""
===== MBC 아카데미 시스템 (패키지방식) =====
1. 회원가입
2. 로그인
3. 로그아웃
4. 회원관리(관리자)
5. 게시판
6. 성적관리
---------------------------------------
0. 종료
=======================================""")
        sel = input(">>>")

        if sel == "1": MemberService.signup()
        elif sel == "2": MemberService.login()
        elif sel == "3": MemberService.logout()
        elif sel == "4": pass #MemberService.admin_menu()
        elif sel == "5": pass #BoardService.run()
        elif sel == "6": pass #ScoreServicer.run()
        elif sel == "0":
            print("프로그램종료")
            run = False

if __name__ == "__main__":
    main()
