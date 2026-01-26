# OOP 객체 지향 프로그래밍
# Object - Oriented - Programming
# 현실 세계의 객체 개념을 기반으로 데이터를 속성(데이터)와 행위 (메서드)로 묶어서 관리하고
# 객체 간 상호작용을 통해 프로그램을 설계하는 프로그래밍 패러다임
# 장점 : 코드 재사용, 유지보수, 가독성 향상
# 핵심 원칙 : 캡슐화 , 상속 , 다형성 등

# .txt의 1행씩 되어있는 자료들을 클래스로 만들어 Member.id/.name/.pw 등으로 접근할 수 있다.
# main.py 는 주 실행 코드
# Member.py는 개인의 객체 [변수와 게터(출력값처리)/새터(입력값처리)] 등을 담당
# MemberService.py 는 CRUD용 메서드들이 들어있는 모듈

from MemberService import MemberService
# MemberService.py 파일안에있는 / MemberService 클래스를 지금 main.py에서 쓰겠다
# MemberService 전체를 가져와서 쓰겟다가 아닌, 필요한 부분만 참조해서 가져다 쓰겟다라고 봄

#app = MemberService() #MemberService의 클래스를 app이라는 변수에 연결
#app.run() # app 변수에 연결된 클래스안에 run() 메서드를 실행함
