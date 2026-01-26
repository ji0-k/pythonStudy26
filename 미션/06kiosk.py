# C : 관리자 , 판매자
# R : 상품리스트 , 상품상세보기(장바구니,바로구매 ...)
# U : 상품 수정페이지(판매자)
# D : 품절 ,
from prompt_toolkit.filters import control_is_searchable

#키오스크프로그램 만들기

import datetime
now = datetime.datetime.now()

run = True

# 필요한 변수
stockList = ["아메리카노", "카페라테", "카페모카", "소금빵", "치케", "두쫀쿠" ,"텀블러" ,"우산"]
stocks =[0,0,0,0,0,0,0,0]
salecount = [0,0,0,0,0,0,0,0]
SalesAmount = [0,0,0,0,0,0,0,0]
total = sum(SalesAmount)

#거래상품리스트업
#거래금액
#총매출액

order = 100
pws = "1234"
pw = None


main = """
========================
메가커피 
========================
1. 메뉴보기
0. 관리자 모드
========================
"""

menu = """
------------------------
1. drink
2. dessert
3. MD
------------------------

"""

drinkMenu = """
------------------------
1. 아메리카노 (2000원)
2. 카페라떼   (3000원)
3. 카페모카   (3500원)
------------------------
"""

dessertMenu = """
------------------------
1.소금빵    (1500원)
2.치즈케잌   (2500원)
3.두쫀쿠    (7500원)
------------------------
"""

MDMenu = """
------------------------
1. 텀블러 (12000원)
2. 우산   (4000원)
------------------------"""

adminMenu = """
------------------------
1. 재고관리
2. 매출관리
0. 처음으로
------------------------"""

stockMenu = """
------------------------
1. 재고 확인
2. 재고 수량 변경
0. 돌아 가기 
------------------------
"""

salesMenu = """
------------------------
1. 매출 확인
0. 돌아가기
------------------------"""


while run :
#--------메인 출력-----------
    print(main)
    select = input(">>>")
#-------서브----------------
    #-----상품 보기-----------
    if select == "1" :
        print(menu)
        choose = input("원하는 메뉴 눌러 : ")
        #-----음료메뉴----------
        subRun2 = True
        while subRun2:
            if choose == "1" :
                print(drinkMenu)
                chooseC = input(">>>")
                #-----아메리카노 --------
                if chooseC == "1" :
                    print("아메리카노 (2000원) ")
                    print("물 + 에스프레소")
                    # 아메리카노의 이미지와 함께 보여줘
                    if stocks [0] == 0 :
                        print("현재상품 품절 다른메뉴 선택")
                        continue
                    else :
                        pass

                    chooseC1 = input("구매를 원하면 y : ")
                    if chooseC1 == "y" :
                        print("""
1.아이스
2.핫
원하는 메뉴 번호 눌러 """)
                        chooseC1y = input(">>>")
                        if chooseC1y == "1" :
                            print("""
1. 포장
2. 먹고가기
원하는 번호 눌러""")
                            chooseC1y1 = input(">>>")
                            if chooseC1y1 == "1" :
                                print("아이스아메리카노 포장하기")
                                cheeesC1y11 = input("카드결제만 가능합니다 : ")
                                if cheeesC1y11 == "card" :
                                    print ("주문이 완료되었습니다.")
                                    order += 1
                                    stocks[0] -= 1
                                    salecount[0] += 1
                                    SalesAmount[0] += 2000
                                    print(f"주문번호 {order}")
                                    break
                                else :
                                    print("다시 주문 ")
                                    continue
                            elif chooseC1y1 == "2" :
                                print("아이스아메리카노 먹고가기")
                                cheeesC1y12 = input("카드결제만 가능합니다 : ")
                                if cheeesC1y12 == "card" :
                                    print ("주문이 완료되었습니다.")
                                    order += 1
                                    stocks[0] -= 1
                                    salecount[0] += 1
                                    SalesAmount[0] += 2000
                                    print(f"주문번호 {order}")
                                    break
                                else :
                                    print("다시 주문 ")
                                    continue
                            else :
                                print("다시 주문")
                                continue
                        elif chooseC1y == "2" :
                            print("""
1. 포장
2. 먹고가기
원하는 번호 눌러""")
                            chooseC1y2 = input(">>>")
                            if chooseC1y2 == "1":
                                print("따뜻한아메리카노 포장하기")
                                chooseC1y21 = input("카드결제만 가능합니다 : ")
                                if chooseC1y21 == "card":
                                    print("주문이 완료되었습니다.")
                                    order += 1
                                    stocks[0] -= 1
                                    salecount[0] += 1
                                    SalesAmount[0] += 2000
                                    print(f"주문번호 {order}")
                                    break
                                else:
                                    print("다시 주문 ")
                                    continue
                            elif chooseC1y2 == "2":
                                print("따뜻한아메리카노 먹고가기")
                                chooseC1y22 = input("카드결제만 가능합니다 : ")
                                if chooseC1y22 == "card":
                                    print("주문이 완료되었습니다.")
                                    order += 1
                                    stocks[0] -= 1
                                    salecount[0] += 1
                                    SalesAmount[0] += 2000
                                    print(f"주문번호 {order}")
                                    break
                                else:
                                    print("다시 주문 ")
                                    continue
                            else:
                                print("다시 주문")
                                continue
                        else :
                            print("다시 주문")
                            continue

                    else :
                        print("메뉴로돌아갑니다")
                        continue

                # ----카페라테 --------
                elif chooseC == "2" :
                    print("카페라떼 (3000) ")
                    print("스팀우유 + 에스프레소")
                    #카페라테 이미지와함께 보여줘
                    if stocks [1] == 0 :
                        print("현재상품 품절 다른메뉴 선택")
                        continue
                    else :
                        pass
                    chooseC2 = input("구매를 원하면 y : ")
                    if chooseC2 == "y":
                        print("""
1.아이스
2.핫
원하는 메뉴 번호 눌러 """)
                        chooseC2y = input(">>>")
                        if chooseC2y == "1":
                            print("""
1. 포장
2. 먹고가기
원하는 번호 눌러""")
                            chooseC2y1 = input(">>>")
                            if chooseC2y1 == "1":
                                print("아이스 카페라테 포장하기")
                                cheeesC2y11 = input("카드결제만 가능합니다 : ")
                                if cheeesC2y11 == "card":
                                    print("주문이 완료되었습니다.")
                                    order += 1
                                    stocks[1] -= 1
                                    salecount[1] += 1
                                    SalesAmount[1] += 3000
                                    print(f"주문번호 {order}")
                                    break
                                else:
                                    print("다시 주문 ")
                                    continue

                            elif chooseC2y1 == "2":
                                print("아이스카페라떼 먹고가기")
                                chooseC2y22 = input("카드결제만 가능합니다 : ")
                                if chooseC2y22 == "card":
                                    print("주문이 완료되었습니다.")
                                    order += 1
                                    stocks[1] -= 1
                                    salecount[1] += 1
                                    SalesAmount[1] += 3000
                                    print(f"주문번호 {order}")
                                    break
                                else :
                                    print("다시 주문 ")
                                    continue
                            else :
                                print("다시 주문")
                                continue
                        elif chooseC2y == "2":
                            print("""
1. 포장
2. 먹고가기
원하는 번호 눌러""")
                        chooseC2y2 = input(">>>")
                        if chooseC2y2 == "1":
                            print("따뜻한 카페라테 포장하기")
                            chooseC2y21 = input("카드결제만 가능합니다 : ")
                            if chooseC2y2 == "card":
                                print("주문이 완료되었습니다.")
                                order += 1
                                stocks[1] -= 1
                                salecount[1] += 1
                                SalesAmount[1] += 3000
                                print(f"주문번호 {order}")
                                break
                            else:
                                print("다시 주문")
                                continue
                        elif chooseC2y2 == "2":
                            print("따뜻한 카페라테 먹고가기")
                            chooseC322 = input("카드결제만 가능합니다 : ")
                            if chooseC322 == "card":
                                print("주문이 완료되었습니다.")
                                order += 1
                                stocks[1] -= 1
                                salecount[1] += 1
                                SalesAmount[1] += 3000
                                print(f"주문번호 {order}")
                                break
                            else:
                                print("다시 주문 ")
                                continue

                        else:
                            print("다시 주문")
                            continue

                    else:
                        print("메뉴로돌아갑니다")
                        continue

                #----카페모카-----------------
                elif chooseC == "3" :
                    print("카페모카 (3500원)")
                    print("모카시럽 + 스팀우유 + 에스프레소")
                    #휘핑이 올라간 카페 모가 사진과함께
                    if stocks [2] == 0 :
                        print("현재상품 품절 다른메뉴 선택")
                        continue
                    else :
                        pass
                    chooseC3 = input ("구매를 원하면 y : ")
                    if chooseC3 == "y":
                        print("""
1.아이스
2.핫
원하는 메뉴 번호 눌러 """)
                        chooseC3y = input(">>>")
                        if chooseC3y == "1":
                            print("""
1. 포장
2. 먹고가기
원하는 번호 눌러""")
                            chooseC3y1 = input(">>>")
                            if chooseC3y1 == "1":
                                print("아이스카페모카 포장하기")
                                chooseC3y11 = input("카드결제만 가능합니다 : ")
                                if chooseC3y11 == "card":
                                    print("주문이 완료되었습니다.")
                                    order += 1
                                    stocks[2] -= 1
                                    salecount[2] += 1
                                    SalesAmount[2] += 3500
                                    print(f"주문번호 {order}")
                                    break
                            elif chooseC3y1 == "2" :
                                print("아이스카페모카 먹고가기")
                                chooseC3y12 = input("카드결제만 가능합니다 : ")
                                if chooseC3y12 == "card" :
                                    print("주문이 완료되었습니다.")
                                    order += 1
                                    stocks[2] -= 1
                                    salecount[2] += 1
                                    SalesAmount[2] += 3500
                                    print(f"주문번호 {order}")
                                    break
                                else:
                                    print("다시 주문 ")
                                    continue
                            else :
                                print("다시 주문")
                                continue

                        elif chooseC3y == "2":
                            print("""
1. 포장
2. 먹고가기
원하는 번호 눌러""")
                            chooseC3y2 = input(">>>")
                            if chooseC3y2 == "1":
                                print("따뜻한 카페모카 포장하기")
                                chooseC3y21 = input("카드결제만 가능합니다 : ")
                                if chooseC3y2 == "card":
                                    print("주문이 완료되었습니다.")
                                    order += 1
                                    stocks[2] -= 1
                                    salecount[2] += 1
                                    SalesAmount[2] += 3500
                                    print(f"주문번호 {order}")
                                    break
                                else :
                                    print("다시 주문")
                                    continue
                            elif chooseC3y2 == "2" :
                                print("따뜻한 카페모카 먹고가기")
                                chooseC322 = input ("카드결제만 가능합니다 : ")
                                if chooseC322 == "card":
                                    print("주문이 완료되었습니다.")
                                    order += 1
                                    stocks[2] -= 1
                                    salecount[2] += 1
                                    SalesAmount[2] += 3500
                                    print(f"주문번호 {order}")
                                    break
                            else :
                                print("다시 주문 ")
                                continue

                        else :
                            print("다시 주문")
                            continue
                    else:
                        print("다시 주문")
                        continue

                else:
                    print("메뉴로돌아갑니다")
                    continue
#-----------------커피메뉴---------------------------------------------

            #----디저트메뉴---------

            elif choose == "2" :
                print(dessertMenu)
                chooseD = input ("원하는 메뉴 번호 : ")
            #-----소금빵----------------------------------------
                if chooseD == "1":
                    print("소금빵 (1500원)")
                    print("고메 버터 와 소금의 단짠 ~~")
                    # 따뜻한 김이 나는 소금빵 이미지와 함께
                    if stocks [3] == 0 :
                        print("현재상품 품절 다른메뉴 선택")
                        continue
                    else :
                        pass
                    chooseD1 = input("구매 원하면 y : ")
                    if chooseD1 == "y" :
                        print("""
1. 포장
2. 먹고가기
원하는 번호 눌러""")
                        chooseD1y = input(">>>")
                        if chooseD1y == "1" :
                            print("소금빵 포장하기")
                            chooseD1y1 = input("카드결제만 가능합니다 : ")
                            if chooseD1y1 == "card":
                                print("주문이 완료되었습니다.")
                                order += 1
                                stocks[3] -= 1
                                salecount[3] += 1
                                SalesAmount[3] += 1500
                                print(f"주문번호 {order}")
                                break
                            else :
                                print ("다시 주문")
                                continue
                        elif chooseD1y == "2" :
                            print("소금빵 먹고가기")
                            chooseD1y2 = input("카드결제만 가능합니다 : ")
                            if chooseD1y2 == "card" :
                                print("주문이 완료되었습니다.")
                                order += 1
                                stocks[3] -= 1
                                salecount[3] += 1
                                SalesAmount[3] += 1500
                                print(f"주문번호 {order}")
                                break
                            else :
                                print("다시 주문")
                                continue
                        else :
                            print("다시 주문")
                            continue


                #-----치즈케이크-------------------------------
                elif chooseD == "2":
                    print("치즈케이크 (3500원)")
                    print("필라델피아 치즈와 쿠키 ~~")
                    #촉촉한 조각 치즈케이크 이미지와 함께
                    if stocks [4] == 0 :
                        print("현재상품 품절 다른메뉴 선택")
                        continue
                    else :
                        pass
                    chooseD2 = input("구매 원하면 y : ")
                    if chooseD2 == "y":
                        print("""
1. 포장
2. 먹고가기
원하는 번호 눌러""")
                        chooseD2y = input(">>>")
                        if chooseD2y == "1":
                            print("치즈케이크 포장하기")
                            chooseD2y1 = input("카드결제만 가능합니다 : ")
                            if chooseD2y1 == "card":
                                print("주문이 완료되었습니다.")
                                order += 1
                                stocks[4] -= 1
                                salecount[4] += 1
                                SalesAmount[4] += 3500
                                print(f"주문번호 {order}")
                                break
                            else:
                                print("다시 주문")
                                continue
                        elif chooseD2y == "2":
                            print("치즈케이크 먹고가기")
                            chooseD2y2 = input("카드결제만 가능합니다 : ")
                            if chooseD2y2 == "card":
                                print("주문이 완료되었습니다.")
                                order += 1
                                stocks[4] -= 1
                                salecount[4] += 1
                                SalesAmount[4] += 3500
                                print(f"주문번호 {order}")
                                break
                            else:
                                print("다시 주문")
                                continue
                        else:
                            print("다시 주문")
                            continue
                #-----두쫀쿠-------------------------
                elif chooseD == "3":
                    print("두쫀쿠 (7500원) ")
                    print(f"두바이 쫀득 쿠키  일일 한정수량 10  ~~")
                    print(f"현재 남은 수량 : {stocks[5]}")
                    # 반으로 갈라져서 카다이프와 피스타치오스프레드가 가득한 두바이쫀득쿠키 이미지와 함께
                    if stocks[5] == 0:
                        print("현재상품 품절 다른메뉴 선택")
                        continue
                    else:
                        pass
                    #두쫀쿠 실시간 수량 표시 !
                    chooseD3 = input("구매 원하면 y : ")
                    if chooseD3 == "y":
                        print("""
1. 포장
2. 먹고가기
원하는 번호 눌러""")
                        chooseD3y = input(">>>")
                        if chooseD3y == "1":
                            print("두쫀쿠 포장하기")
                            chooseD3y1 = input("카드결제만 가능합니다 : ")
                            if chooseD3y1 == "card":
                                print("주문이 완료되었습니다.")
                                order += 1
                                stocks[5] -= 1
                                salecount[5] += 1
                                SalesAmount[5] += 7500
                                print(f"주문번호 {order}")
                                break
                            else:
                                print("다시 주문")
                                continue
                        elif chooseD3y == "2":
                            print("두바이 쫀득 쿠키 먹고가기")
                            chooseD3y2 = input("카드결제만 가능합니다 : ")
                            if chooseD3y2 == "card":
                                print("주문이 완료되었습니다.")
                                order += 1
                                stocks[5] -= 1
                                salecount[5] += 1
                                SalesAmount[5] += 7500
                                print(f"주문번호 {order}")
                                break
                            else:
                                print("다시 주문")
                                continue
                        else:
                            print("다시 주문")
                            continue
                else :
                    print("메뉴로돌아갑니다")
                    continue

            #----엠디상품-----------
            elif choose == "3" :
                print(MDMenu)
                chooseM =input("원하는 메뉴 번호 :  ")
                if chooseM == "1":
                    print("절대 녹지않고 절대 식지않는 완벽보냉 텀블러(12000원)")
                    #단단하고 강한 텀블러 이미지와 함께
                    if stocks [6] == 0 :
                        print("현재상품 품절 다른메뉴 선택")
                        continue
                    else :
                        pass
                    chooseM1 = input("구입원하면 y : ")
                    if chooseM1 == "y":
                        chooseM1y = input("카드결제만 가능합니다 : ")
                        if chooseM1y == "card" :
                            print("주문이 완료되었습니다.")
                            order += 1
                            stocks[6] -= 1
                            salecount[6] += 1
                            SalesAmount[6] += 12000
                            print(f"주문번호 {order}")
                            break
                        else :
                            print("다시 주문")
                            continue
                elif chooseM == "2":
                    print("안가져나오면 항상 비옴, 우산 (4000원) ")
                    #귀여운 투명우산 이미지와 함께
                    if stocks [7] == 0 :
                        print("현재상품 품절 다른메뉴 선택")
                        continue
                    else :
                        pass
                    chooseM2 = input("구입원하면 y : ")
                    if chooseM2 == "y":
                        chooseM2y = input("카드결제만 가능합니다 : ")
                        print("주문이 완료되었습니다.")
                        order += 1
                        stocks[7] -= 1
                        salecount[7] += 1
                        SalesAmount[7] += 4000
                        print(f"주문번호 {order}")
                        break
                    else :
                        print("다시 주문")
                        continue
                else :
                    print("잘못된 접근")
                    continue
        else :
            print("잘못된 접근")
#--------일반 메뉴 주문 끝-----------------------------------

    #-----관리자메뉴----------
    elif select == "0" :
        pw = input ("관리자 암호 : ")
        if pw == pws :
            adminRun = True
            while adminRun:
                print(adminMenu)
                admin = input(">>>")
                if admin == "1": #-----재고관리----------------

                    print(stockMenu)
                    choose = input(">>>")
                    if choose == "1": # 재고확인
                        print('------------------------')
                        print(f"아메리카노 : {stocks[0]}")
                        print(f"카페라테   : {stocks[1]}")
                        print(f"카페모카   : {stocks[2]}")
                        print('------------------------')
                        print(f"소금빵    : {stocks[3]}")
                        print(f"치즈케이크 : {stocks[4]}" )
                        print(f"두쫀쿠    : {stocks[5]}")
                        print("------------------------")
                        print(f"텀블러    : {stocks[6]}")
                        print(f"우산      : {stocks[7]}")
                    elif choose == "2": #재고 수정
                        print("""
1.아메리카노 
2.카페라테 
3.카페모카 
4.소금빵 
5.치즈케이크 
6.두쫀쿠 
7.텀블러
8.우산
0.돌아가기
수량변경 원하는 항목 코드입력""")
                        requset = int(input(">>>"))
                        if 1 <= requset <= 8 : # 숫자를 입력 받았어, 상품 재고 두개 나오게
                            index = requset - 1
                            change = int(input("재고 더하기(+), 재고 빼기(-) 포함 입력 : ")) #다른키 잘못눌렀을때 에러뜸
                            stocks[index] += change
                            print(f"{stockList[index]}의 수량 {stocks[index]}")
                            continue

                        elif requset == 0 :
                            print("이전화면으로 돌아가")
                            break

                        else :
                            print("잘못된 접근")
                            continue
                    elif choose == "0" :
                        print("이전화면 돌아가")
                        break

                    else :
                        print("잘못된 접근")

                elif admin == "2" :
                    print(f"{now} 기준 \n 총 주문건수 : {order-100}")
                    print("상품별 주문 건수 / 판매액 ")
                    print(f"{stockList[0]} : {salecount[0]}/{SalesAmount[0]}원")
                    print(f"{stockList[1]}   : {salecount[1]}/{SalesAmount[1]}원")
                    print(f"{stockList[2]}   : {salecount[2]}/{SalesAmount[2]}원")
                    print(f"{stockList[3]}     : {salecount[3]}/{SalesAmount[3]}원")
                    print(f"{stockList[4]}       : {salecount[4]}/{SalesAmount[4]}원")
                    print(f"{stockList[5]}     : {salecount[5]}/{SalesAmount[5]}원")
                    print(f"{stockList[6]}     : {salecount[6]}/{SalesAmount[6]}원")
                    print(f"{stockList[7]}       : {salecount[7]}/{SalesAmount[7]}원")
                    print(total)
                elif admin == "0" :
                    print("이전화면으로 돌아가")
                    break
                else :
                    print("잘못된 접근")
                    continue


        else :
            print("잘못된 접근")
            continue
    else :
        print("잘못된 접근")
        continue