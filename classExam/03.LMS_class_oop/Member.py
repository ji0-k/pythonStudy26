# Member.py 는 각 회원에 자료를 담당한다
# 웹프로그래밍에 백엔드에는 데이터베이스와 결합하는데
# MemberDTO, MemberVO라는 이름으로 사용된다.
# DTO = data0122 transfer Object , 데이터 전송 객체
# VO = value Object, 값 그 자체 ,

# 회원 각각의 자료를 리스트가 아닌 변수에 담에 제공하려 함

class Member : #클래스는 첫글자 대문자
    def __init__(self,uid,pw,name,role="user",active=True):
        self.id = uid
        self.pw = pw
        self.name = name
        self.role = role
        self.active = active

    # 사용법 member.txt = Member() -> 객체 생성하여 변수에 연결 / 클래스는 첫글자 대문자
    # 이름 : member.txt.id
    # 암호 : member.txt.pw

    #파일 저장용 문자열 변환
    def to_line(self) :
        return f"{self.id}|{self.pw}| {self.name} |{self.role}|{self.active}\n"
    # 사용법 member.txt = Member()
    # member.txt.to_line() -> kkw|1234|김기원|admin|True 엔터
    # 메모장에 객체기록용

    # 파일에서 불러온 내용 객체처리
    @classmethod  # 객체(self)가 아니라 클래스(cls)자체를 다루는 메서드정의
    def from_line(cls,line) : # line: 메모장의 1행 문자열 , 객체 저장시 from_line~ , 변환시 to_line~
        uid,pw,name,role,active = line.strip().split("|")
        #    위의 변수들에 넣음 <= 1행 문자열 엔터지우고 |로 잘라서
        return cls(uid,pw,name,role,active =="True")

    # 사용법 : m = Member(uid,pw,name,role, active) ->권장하지않음(바로넣음)
    #            self를 사용하는 방법 ( 객체 변수 )
    # 권장법 : m = Member.from_line(line) -> r객체생성 책임을 클래스가 담당
    #            cls를 사용하는 방법 ( 클래스 변수)
    ##직렬화(Serialization) : 객체 -> 저장가능한 형태
    #          member.txt.to_line()
    ##역직렬화(Deserialization) : 저장된데이터 -> 객체 (@classmethod)
    #       Member.from_line(line)