# 클래스는 주로 같은 내용에 변수 및 메서드를 모아서 처리하는 용도
# 인스턴스 : 객체를 복체해서 같은변수나 메서드를 찍어내는 효과

# LMS 프로그램 지금처럼 콘솔에 짜면 1인용인데
# 클래스로 구현하면 여러명이 접근해서 사용할 수 있다. -> Flask, fastAPI(웹서버)
# 변수 선언시 글로벌 영역에 선언하면 : session -> 값을 공유
# 클래스가 아닌 일반 사항으로 처리하면 1명이 로그인하면
# 다른사람이 접속 할때 이미 로그인 한 상태가 됨


# 함수를 이용해 더하기 기능 구현한 파이썬 코드
result = 0 #전역에 있는 변수 , 함수 호출후 처리 결과가 누적될 값
def add (num) : # num(매개변수:함수 호출 시 외부에서 전달 받는)을 받아 add라는 이름을 가진 함수 만듦
    global result # 전역변수를 이 함수 안에서 수정하겠다고 선언
                  # 함수안에서 새변수를 만들지 않고 밖에 있는 변수 result를 그대로 사용
    result += num # 결과값에 num을 더해 result에 넣음
    return result # 처리된 result값을 반환함

print(add(3)) # 0 + 3
print(add(4)) # 3 + 4
print(add(5)) # 7 + 5

# 연속 프린트시 결과값이 누적되어 각각의 계산이 어려움
# 이런 상황 해결 하기 위해 함수를 각각 따로 만들어야 함
#----------------------------------------------------

#------각각의 따로 도는 함수 만들기
result1 = 0
result2 = 0

def add1 (num) : # 계산기 1 num매개변수를 받아 처리하는 add1라는 함수 만듦
    global result1 # 전역변수를 가져와 이 함수안에서 수정하겠다고 선언
    result1 += num # result1 = result1 + num
    return result1  # 처리된 result1 반환

def add2 (num) : # 계산기 2 , num이라는 매개변수 받아 처리하는 add2라는 함수 만듦
    global result2 # 전역변수 가져와 이 함수 안에서 수정 하겠다 선언
    result2 += num # result2 = result2 + num
    return result2 # 처리된 result2 반환

print(add1(1))
print(add1(2))
print(add2(3))
print(add2(4))

#각각 함수 add1, add2은 서로에게 영향을 미치지 않고
#각자 자기 함수 내에서 변수에게만 영향을 미친다
#---------------------------------------------------

#----------------
class Calculator : # Calculator라는 클래스(설계도) 만듦
    def __init__(self)  : #객체(인스턴스)가 생성될때 자동 호출되는 초기화 매서드
                #self는 생성된 객체 자기 자신을 가르키는 참조 변수
        self.result = 0 # self객체에 result라는 변수를 만들고 그 값을 0으로 설정

    def add(self,num): # 첫번째 객체 self와 두번째 num이라는 매개변수로 실행되는 함수 add를 만듦
                       # 객체 자신 self와 외부에서 전달 받은 값 num을 사용해 실행 되는 메서드
        self.result += num # self객체 안에 result라는 변수에다가 num에들어가는 값을 더한 값을 self객체안에 result라는 변수의 값으로 넣기
        return self.result # 변경된 self객체안에 result라는 변수의값을 반환한다

cal1 = Calculator() #Calculator 설계도로 만든 1번 계산기(객체)
cal2 = Calculator() # Calculator 설계도로 만든 2번 계산기(객체)
# 둘다 서로 같은 설계를 가진 계산기이지만 각각의 독립적인 값을 가진 계산기 객체(인스턴스)읻이다.
#클래스는 설계도이고, 인스턴스는 그 설계도로 만든 서로 독립적인 객체이며, self는 “지금 이 객체”를 가리키는 참조다.
print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(4))























