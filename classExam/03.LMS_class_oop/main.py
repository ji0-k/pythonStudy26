# 파이선에 oop를 적용해보자
# oop 객체지향 프로그래밍, object - oriented Programming
# 현실세계의 객체, 개념을 기반으로 데이터를 속성(데이터)와 행위(메서드)로 묶어 관리
# 객체 간 상호작용을 통해 프로그램을 설계하는 프로그래밍 패러다임으로,
# 장점 코드재사용 , 유지보수의 용이성, 가독성 향상
# 캡슐화 , 상속 , 다형성 등 핵심원칙

# 지금까지는 2차원 배열을 이용해서 인덱스로 데이터에 접근을 하는데,
# [0] 이곳에 무엇이 들어있는지 암기를 하고 [4]는 무엇이 들어갈지?
# 메모장의 1줄로 되어있는 자료를 클래스로 만들면
# Member.name / Member.id / Member.pw 등으로 접근 할 수 있다.

# Member.py는 개인의 객체 -> 변수와 게터(나오는값처리)/세터(검증,입력값처리) 등을 담당함
# MemberService.py CRUD용 메서드들이 들어 있는 모듈
# main.py 는 주 실행 코드

from MemberService import MemberService
# 외부파일 (모듈) 가져와 ~  (클래스 연결)
app = MemberService()
app.run()

