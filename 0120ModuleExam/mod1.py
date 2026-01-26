# 모듈 학습하기
# 모듈은 파이썬 파일로 만든것을 연동하여 프로그램으로 처리
# 실무에서는 파일 1개로 제공 X
# 각각 기능이 있는 파일을 빼서 클래스화 하고 메서드로 동작한다.
# main.py -> __main__(__main__)주 실행코드 와 서비스를 연결하는 주 메뉴와 메서드
# MemberService.py -> 회원 관리 하는 클래스와 메서드
# ScoreService.py -> 성적관리하는 클래스와 메서드
# BoardService. py -> 게시판을 관리하는 클래스와 메서드
# ItemService.py -> 상품을 관리하는 클래스와 메서드
# CartService.py -> 장바구니를 관리하는 클래스 와 메서드

# 파이썬 확장자  .py로 만든 파이썬 파일은 모두 모듈로 처리 가능함

def add(a,b) :
    return a+b

def sub(a,b) :
    return a-b

# print(add(1,4))
# print(sub(4,2))
# # 터미널에 python을 실행하고
# # import mod1을 했더니
# # 바로 print문이 실행된다
# # 근데 main에서 실행하면 ?
# # mod1의 프린트와 main의 프린트가 실행
# # 메인에서는 add와 sub 함수만 호출해서 사용하려고만 했다.

if __name__ == "__main__" : #내가 메인이면 이걸 실행해라 아니면 말고
    # 클래스나 모듈이 호출된 자신이 main 역할인지를 확인
    print(add(3,4))
    print(sub(3,4))

print(__name__) #mod1 으로  찍힘


