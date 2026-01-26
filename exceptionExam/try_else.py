# try_else : try문 수행중 오류가 발생하면 except
#            오류 발생하지 않으면 else절 수행

try :
    age = int(input("나이를 입력하세요"))

except : #except에 클래스를 넣지 않으면 모든 예외
    print("숫자만 입력하세요")

else : # 예외 발생하지않으면 처리되는 문장
    if age <= 18 :
        print("귀하는 미성년자입니다")
    else :
        print("환영합니다 ")