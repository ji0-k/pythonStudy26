# Member.py에는 회원 자료를 담당
# 웹프로그래밍에 백엔드는 DB와 결합
# MemberDTO ( Data transfer Object ) 데이터 전송 객체
# MemberVO ( Value Object ) 값 객체

# 회원들 각각의 자료를 리스트가 아닌 변수에 담아 제공

class Member : # 클래스는 대문자 시작
    def __init__(self, uid, pw, name, role="user", active = True) : #()안에 매개변수
    # Member 라는 객체가 만들어질때 , 자동으로 실행되며 , 이 객체들이 가져야 할 기본정보를 초기 상태로 설정하는 함수
    # 현재까지는 객체변수가 아님 , 외부에서 전달받는 값 매개변수임
    # __init__ 생성자 constructor , 객체가 생성되는 순간 자동 실행 , 직접 호출 X
        self.id = uid #객체에 저장된 실제 속성 , 이 객체가 가진 id라는 공간에 밖에서 받은 uid
        self.pw =pw #이객체가 가진 pw공간에 밖에서 받은 pw를 저장
        self.name = name # 이객체가 가진 name공간에 밖에서 받은 name저장
        self.role = role # 이객체가 가진 (여기서의 객체는 지금 새로운 member정보 만드는중에있는 회원이될거야)
        self.active = active # 이객체가 가진 active공간에 밖에서 받은 active에 저장
    # 여기부터 객체의 속성이 생김
    # 여기까지는 __init__는 객체가 생성될때 전달받은 값을
    # 해당 객체의 속성으로 저장해 초기 상태를 만드는 생성자이다.

    # member.txt = Member() member객체를 생성하여 Member안에 변수에 연결

    #------------파일 저장용 문자열 변환 ( 프로그램에서 받은 값을 .txt파일로 저장하기위한 문자열 변환)
    def to_line(self): #함수, 1행씩 저장하기 위한, member.txt 객체를
        return f"{self.id}{self.pw}{self.name}{self.role}{self.active}\n"
    # member.txt.to_line() -> id|pw|name|role|active 엔터 라는 객체가 .txt파일에 기록 저장됨

    #-----------파일 읽기용 객체 처리(.txt파일에 저장되있는 문자열을 불러와 프로그램안에서 객체처리)
    @classmethod #이 메서드는 클래스(Member)자체에 소속된 메서드다
    def from_line(cls,line) : #.txt파일 한줄 받아서 Member객체 1개로 변환해서 만들어주는 클래스 메서드이다
        uid,pw,name,role,active = line.strip().split("|")
                                #한줄가져와.양쪽공백+기행문자제거."|"기준으로값분리
        return cls(uid,pw,name,role,active=="True")
        #()괄호안에 값들로 Member객체 하나 만들어서 반환

    # 사용법 : m = Member(uid,pw,name,role,active) -> 바로넣는거 권장X, self객체 사용
    # 권장법 : m = Member.from_line(line) -> 객체 생성을 클래스가 담당 cls사용하는 클래스변수

    # 직렬화(serialization) : 객체 -> 저장가능한 형태 , member.txt.to_line()
    # 병렬화(Deserialization) : 저장된 데이터 -> 객체 (@classmethod), Member.from_line(line)




















