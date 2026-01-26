



def add(num) : # add 라는 함수 만들었다, num을 받아서
    global result # 전역 변수 가져와 0값을 가지고 있음
    result += num # result = result + num
    return result #
    # add() 함수 만듦


def add2(num) : # add2 라는 함수 만들었다, num을 받아서
    global result2 # 전역 변수 가져와 0값을 가지고 있음
    result2 += num # result = result + num
    return result2 #

print(add(5))
print(add2(9))
print(add(2))
print(add2(4))

# global영역에있는 result, result2를 공유함
# 단점은 다수가 프로그램을 사용할 때는?
# 여러명이 add() 함수 사용하려면 여려명 만큼 함수와 변수 생성
