# __all__ 내장변수

# main.py 파일이 있는 상태에서
# from game.sound import *
#           패키지     하위 모든것

# >>> from game.sound import *
# >>> eco.eco_test()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'eco' is not defined
# echo라는 이름이 정의 되지 않았다는 오류가 나옴

# 모든것*을 사용하고 싶으면 2가지 해결 방법이 있다.
# 1. main.py 파일을 만들지 말것. 패키지가 아니게 만들기
# 2. main.py __all__을 이용해서 제공할 것

__all__ = ["echo"] # 변수에 리스트화 하여 모듈을 넣는다.
#          echo.py
# __all__이 의미하는 것은 sound 패키지 하위 모듈을 import할 목록

# 이때 착각하기 쉬운 것
# from game.sound.echo import *은 __all__에 상관없이 import됨
# from game.sound import * 은 패키지를 *로 import해서 __init__.py에 영향을 받음