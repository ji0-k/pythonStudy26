# 상품에대한 CRUD구현
# C : 상품등록
# R : 전체 상품 목록
#     상품 자세히 보기
# U : 상품 수정
# D : 상품 품절

# 사용할 전역 변수
run = True

category = [] # 상품 분류
items_No = [] #상품번호
item_names = [] #상품명
unit_prices = [] #단가
quantity = [] # 수량
product_info = [] #상품정보

#사용할 함수 (메서드)
def new_item():
    print("new_item(): 함수")
    print("새상품 추가 메뉴로 진입합니다.")
    #새상품 추가용 실행문...

def item_list():
    print("item_list(): 함수")
    print("현재 판매중인 리스트 입니다.")
    # 리스트 출력용 for item in item_names :

def item_view():
    print("item_view(): 함수")
    print("상품 자세히 보기")
    #상품에 대한 상세정보 표시

def item_update():
    print("item_update(): 함수")
    print("상품 수정 하기")
    #상품 정보 수정하기

def item_delete():
    print("item_delete(): 함수")
    print("상품 삭제 하기")
    #상품 품절, 삭제 하기






itemMenu - """
-------------------------
@@@@@@@@@@@@@@@@@@@@@@
-------------------------
1. 상품등록하기
2. 상품보기(리스트/상세페이지) 
3. 상품보기(상세페이지)
4. 상품수정하기
5. 상품삭제하기
0. 프로그램종료

"""





def item_add_menu():
    print("""
======상품등록하기======
1.교재
2.사무용품
3.잡화
---------------------
0.상품등록하기 종료
======================

""")




#프로그램 주 실행 코드 시작
while run :
    itemMenu()

    select = input("숫자 입력 : ")
    if select == "1" :
        item_add_menu()
        new_item()
    elif select == "2" :
        item_list()
    elif select == "3" :
        item_view()
    elif select == "4" :
        item_update()
    elif select == "5" :
        item_delete()
    elif select == "9" :
        run = False
    else :
        print("잘못입력 , 다시")





















