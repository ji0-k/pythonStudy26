# 클래스 용도로 파일을 생성하면 대문자로 시작

class FourCal :
    pass # 아무동작 안하고 넘어감

#변수 선언부 __init__
    def __init__(self): #생성자 , 객체 생성할때 쓰는 자료 기본값
        self.first = 0
        self.second = 0
        # 위 방법은 개발자들이 취약한 코드라고 판단!
        # 직접적으로 바로 넣는거 보다는
        # 검증 코드를 넣어 한번 더 거쳐서 입력

    # 보완 방법
    # 세터와 게터를 이용해 구현함
    def setdata(self,first,second): #setdata : 값을 넣는다 라고 생각
    # a.first와 a.second 를 직접 가서 처리가가능
    # 하지만 검증해서 값을 처리하는 것도 필요함
    # 데이터를 넣는 메서드를 세터라고 한다.
        if first <= 0 :
            self.first = 0
        else :
            self.first = first
        if second <= 0 :
            self.second = 0
        else :
            self.second = second
    def add(self) :
        result = self.first + self.second
        return result



# 메서드 선언부
a = FourCal()
#a.first = 100 # 취약한 코드
#a.second = 200


a.setdata(-10, 10) # 보완한 코드 처리값
result1= a.add()
print(f"-10+10을 add()메서드 실행 결과값 : {result1}")


print(a.first)
print(a.second)


# a변수에 Fourcal() 클래스를 연결한다
#print(type(a))
#<class '__main__.FourCal'> 얘는 클래스 타입이고 어떤 메인에 대한 FourCal이다 라고함...?
# __main__ 모듈의 이름을 담고 있는 파이썬 내장 변수
# 최상위 코드가 실행되는 환경의 이름 (주 실행 코드임)
# 건물에는 무조건 1층 입구가 잇듯이 프로그램 실행은 main으로 판단

class MoreFourCal (FourCal) :
    #              부모 객체
    # 부모 객체의 모든 기능을 사용 하면서 추가 메서드를 만듦
    def pow(self):
        result = self.first ** self.second
        #            부모의 추가 메서드 제곱
        return result

c=MoreFourCal()
c.add() #부모의 메서드 활용
c.pow() #자식의 메서드 활용

# 메서드 오버라이딩 (부모가 만든 메서드를 튜닝 할때)
# d = FourCal()
# d.setdata(8,0)
# result= d.div()
# print(result)

#--------0일경우 0을 처리 하는 방법

# def div (self) : #부모와 같은 메서드 명
#     if self.second == 0 : # second 0이연
#         return 0 # 0을 반환하고
#     else :
#         return self.first/self.second #아니면 입력 값 처리 후 반환


# e = MoreFourCal()
# e.setdata(9,0)
# result = e.div()
# print(result)


#클래스 변수(필드) : __init 나 일반 메서드에 바깥쪽 변수
class Family :
    lastname = "김"
    # 이곳은 메서드들...
print(Family.lastname)
a=Family()
b=Family()
a.lastname = "최"

print(a.lastname)
print(b.lastname)



























