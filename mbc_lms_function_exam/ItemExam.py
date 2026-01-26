# 상품에대한 CRUD구현
# C : 상품등록
# R : 전체 상품 목록
#     상품 자세히 보기
# U : 상품 수정
# D : 상품 품절

# 사용할 전역 변수
run = True
category = ["도서","사무용품","잡화"] # 상품 분류
item_names = ["책","볼펜","담요"] #상품명
item_prices = [10000,2000,8000] #단가
quantity = [20,30,10] # 수량
product_info = ["수돗물도 금값에 파는 화술","부드럽게써지는 3색 볼펜","불가마 속 열기를 느끼게 해주는 담요"] #상품정보


#사용할 함수 (메서드)
#-----------------------새상품추가-------------------------

def new_item():
    print("새상품 추가 메뉴로 진입합니다.")
    #새상품 추가용 실행문...
    name = input("상품명 : ")
    price = int(input("가격 : "))
    qty = int(input("수량 : "))
    info = input("상품설명 : ")
    cate = input("카테고리 : ")
    cate_no = int(cate)
    if cate_no == 1 :
        cate = "도서"
    elif cate_no == 2 :
        cate = "사무용품"
    elif cate_no == 3 :
        cate = "잡화"
    else :
        print("잘못된입력")

    print(f"상품명 : {name}ㅣ가격 : {price}ㅣ수량 : {qty}ㅣ상품설명 : {info} ㅣ카테고리 : {cate}")
    check = input("입력한 값 맞으면 y :")
    if check == "y" :
        item_names.append(name)
        item_prices.append(price)
        quantity.append(qty)
        product_info.append(info)
        category.append(cate)
        print("상품등록 완료, 상품보기에서 확인")
    else:
        print("상품 등록이 취소되었습니다.") #else 없어도 가능한 구조 (생략가능)

#------------------------------------------------------------

#----------------판매리스트-----------------------------------

def item_list():
    print("현재 판매중인 상품 입니다.")
    # 리스트 출력용 for item in item_names :
    for i in range(len(item_names)) :
        print(f"{i+1}. {item_names[i]}") #품절 리스트 표시 하는법

#-----------------------------------------------------------

#------------------상세설명보기-------------------------------
def item_view():
    print("상품 자세히 보기")
    #상품에 대한 상세정보 표시
    for i, item in enumerate(item_names, start=1) : #1번부터 번호 붙이기
        print(i, item)
    view = int(input("자세히 보기 할 상품 번호 : "))
    item_idx = view -1
    info_list(item_idx)
#------------------------------------------------------------

#-----------------상품수정하기--------------------------------

def item_update():
    print("상품 수정 하기")
    #상품 정보 수정하기
    for i, item in enumerate(item_names, start=1) :
        print(i, item)
    item_idx = int(input("수정할 상품 번호 : "))-1
    print(f"""
    ============================
    1. 상품명 : {item_names[item_idx]}
    2. 상품가격 : {item_prices[item_idx]}
    3. 수량 : {quantity[item_idx]}
    4. 설명 : {product_info[item_idx]}
    5. 분류 : {category[item_idx]}
    ============================
    """)
    field_no = int(input("수정할 내용 번호 :"))
    if field_no == 1 :
        item_names[item_idx] = input("수정 내용 입력 : ")
        print(f"변경 후 상품명 : {item_names[item_idx]}")

    elif field_no == 2 :
        item_prices[item_idx] = int(input("수정 내용 입력 :"))
        print(f"변경 후 가격 : {item_prices[item_idx]}")

    elif field_no == 3 :
        quantity[item_idx] = int(input("수정 내용 입력 : "))
        print(f"변경 후 수량 : {quantity[item_idx]}")

    elif field_no == 4 :
        product_info[item_idx] = input("수정 내용 입력 : ")
        print(f"변경 후 설명 : {product_info[item_idx]}")
    elif field_no == 5 :
        category[item_idx] = input("수정 내용 입력 : ")
        print(f"변경 후 분류 : {category[item_idx]}")

    else :
        print("잘못된 입력")

#-------------------------------------------------------------------

#------------상품 삭제하기--------------------------------------------
def item_delete():
    print("상품 삭제 하기")
    #상품 품절, 삭제 하기
    for i in range(len(item_names)) :
        print(f"{i+1}. {item_names[i]}")
    remove = int(input("삭제할 상품 선택 : "))
    idx = int(remove)-1
    remove2 = input(f"[{item_names[idx]}]\n위 상품과 포함한 모든 정보를 삭제? y : ")
    if remove2 == "y" :
        item_names.pop(idx)
        item_prices.pop(idx)
        quantity.pop(idx)
        product_info.pop(idx)
        category.pop(idx)
        print("삭제가 완료 되었습니다.")

def itemmenu():
    print("""
-------------------------
------- 장    터  --------
-------------------------
1. 상품등록하기
2. 상품보기(리스트/상세페이지) 
3. 상품보기(상세페이지)
4. 상품수정하기
5. 상품삭제하기
0. 프로그램종료

""")

def item_add_menu():
    print("""
======카테고리선택======
1.도서
2.사무용품
3.잡화
---------------------
0.상품등록하기 종료
======================

""")

def info_list(item_idx) :
    print(f"""
============================
1. 상품명 : {item_names[item_idx]}
2. 상품가격 : {item_prices[item_idx]}
3. 수량 : {quantity[item_idx]}
4. 설명 : {product_info[item_idx]}
5. 분류 : {category[item_idx]}
============================
""")


#-----------------------------------
#프로그램 주 실행 코드 시작, 메뉴 선택용이라 짧은거
#-----------------------------------
while run :
    itemmenu()

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
    elif select == "0" :
        run = False
    else :
        print("잘못입력 , 다시")

