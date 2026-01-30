# 주 실행코드 , 메인메뉴 등을 관리
from LMS.common.Session import Session
from LMS.service import *

def main():
    MemberService.load()


    run = True
    while run:
        print("""
=============================
    MBC 아카데미 관리 시스템 
 ---------------------------
 1. 회원가입
 2. 로그인
 3. 로그아웃
 4. 회원정보
 5. 게시판
 6. 성적관리
 7. 상품몰
 ---------------------------
 0. 프로그램 종료
=============================""")
        # 현재 세션상태
        member = Session.login_member
        if member is None :
            print("비 로그인 상태")
        else :
            print(f"{member.name}님 환영합니다.")
        # 메뉴선택
        sel = input("원하는 메뉴의 번호 입력 :")
        if sel == "1" :
            MemberService.signup()
        elif sel == "2":
            MemberService.login()
        elif sel == "3":
            MemberService.logout()
        elif sel == "4":
            MemberService.modify()
        elif sel == "5":
            print("게시판")
        elif sel == "6":
            print("성적관리")
        elif sel == "7":
            print("상품몰")
        elif sel == "0":
            print("프로그램종료")
        else :
            print("잘못된접근")

if __name__ == "__main__":
    main()
