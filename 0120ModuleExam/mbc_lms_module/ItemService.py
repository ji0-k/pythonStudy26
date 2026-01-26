class ItemService:
    def __init__(self):
        item = []
    def run(self):
        subrun = True
        while subrun:
            print("""
============================
엠비씨 아카데미 LMS 서비스 
 : 교보재관리
----------------------------
1. 게시물 보기
2. 게시물 등록
3. 게시물 수정
4. 게시물 삭제
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