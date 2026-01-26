# 주실행 코드로 주메뉴를 담당한다.
# 외부 모듈을 호출해서 연동한다.

import MemberService  # 회원관리용 클래스
import ScoreService   # 학생 점수 관리용 클래스
import BoardService   # 게시판 관리용 클래스
import ItemService    # 상품관리용 클래스

def main():
    run = True
    while run :
        print("""
============================
  엠비씨 아카데미 LMS 서비스 
----------------------------
1. 회원관리
2. 성적관리
3. 자료게시판
4. 교보재관리
5. 교수전용
6. 취업용게시판
----------------------------
0. 종료
""")
        select = input(">>>")
        if select == "1":
            print("회원관리 서비스로 진입합니다.")
            # 회원서비스 클래스 호출용 코드
            MemberService.MemberService().run()
            # import          클래스       메서드
            print("회원관리 서비스를 종료합니다.")

        elif select == "2":
            print("성적관리 서비스로 진입합니다.")
            #성적관리 클래스 호출용코드
            ScoreService.ScoreService().run()
            # import        클래스       메서드
            print("성적관리 서비스를 종료합니다.")

        elif select == "3":
            print("자료게시판 진입합니다.")
            print("자료게시판 종료합니다.")

        elif select == "4":
            print("교보재관리 서비스로 진입합니다.")
            print("교보재관리 서비스를 종료합니다.")

        elif select == "5":
            print("교수전용 서비스로 진입합니다.")
            print("교수전용 서비스를 종료합니다.")

        elif select == "6":
            print("취업용 게시판에 진입합니다.")
            print("취업용 게시판을 종료합니다.")

        elif select == "0":
            print("MBC LMS 서비스를 종료합니다.")
            run = False

        else :
            print("잘못된 접근")

if __name__ == "__main__" :
# 여러파일 호출하기 때문에 main일때만 main()메서드 실행 하기위해 확인하는
    main() #위에 만든 main()함수 실행한다
