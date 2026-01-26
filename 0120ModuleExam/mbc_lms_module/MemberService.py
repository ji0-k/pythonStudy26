# 회원에 관한 CRUD를 구현
# 부메뉴와 함께 run()메서드를 진행



class MemberService:
    def __init__(self):
        #클래스 생성시 필요한 변수들
        # 파일명, 리스트
        members = []

    def run (self):
        #부메뉴 구현 메서드
        subrun = True
        while subrun :
            print("""
============================
엠비씨 아카데미 LMS 서비스 
 : 회원관리 
----------------------------
1. 로그인
2. 회원가입
3. 회원수정
4. 회원탈퇴
5. 로그아웃
----------------------------
0. 종료
""")
            subSelect = input(">>>")
            if subSelect == "1":
                print("로그인 메서드 호출")
            elif subSelect == "2":
                print("회원가입 메서드 호출")
            elif subSelect == "3":
                print("회원수정 메서드 호출")
            elif subSelect == "4":
                print("회원탈퇴 메서드 호출")
            elif subSelect == "5":
                print("로그아웃 메서드 호출")
            elif subSelect == "0":
                print("회원서비스 종료")
                subrun = False
            else :
                print("잘못된 접근")

