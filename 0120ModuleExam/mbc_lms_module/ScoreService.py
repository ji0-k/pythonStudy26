class  ScoreService:
    def __init__(self):
        # 클래스 생성시 필요한 변수들
        score = []

    def run(self):
        subrun = True
        while subrun:
            print("""
============================
엠비씨 아카데미 LMS 서비스 
 : 성적관리 
----------------------------
1. 성적 입력
2. 성적 조회
3. 성적 수정
4. 성적 삭제
----------------------------
0. 종료
""")
            subSelect = input(">>>")
            if subSelect == "1":
                print("성적입력 메서드 호출")
            elif subSelect == "2":
                print("성적조회 메서드 호출")
            elif subSelect == "3":
                print("성적수정 메서드 호출")
            elif subSelect == "4":
                print("성적삭제 메서드 호출")
            elif subSelect == "0":
                print("성적관리 서비스 종료")
                subrun = False
            else :
                print("잘못된 접근")