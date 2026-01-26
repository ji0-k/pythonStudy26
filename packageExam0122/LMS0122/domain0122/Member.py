# 회원에 대한 CRUD 객체용 클래스
class Member :

    # member.txt = Member("id","pw","name","role","active")
    def __init__(self,uid,pw,name,role="user",active=True):
    # 객체가 생성될때 초기값 처리함
        self.uid= uid
        self.pw= pw
        self.name= name
        self.role= role
        self.active= active

    def __str__(self) : # print(member.txt) 처리되는 용, 객체의 주소가 아닌 안에 값이 나옴
        status = '활성' if self.active else "비활성"
        return f"{self.uid}|{self.pw}|{self.name}|{self.role}|{status}"

    #------------파일 저장용 문자열 변환 ( 프로그램에서 받은 값을 .txt파일로 저장하기위한 문자열 변환)
    def to_line(self) :
        # 파일 저장용 (직렬화) : 메모리에 있는 객체를 메모장으로 저장할 문자열로 변환
        return f"{self.uid}|{self.pw}|{self.name}|{self.role}|{self.active}\n"
        # member.txt.to_line() -> id|pw|name|role|active 엔터 라는 객체가 .txt파일에 기록 저장됨

    #--------------
    @staticmethod # 객체가 아니라 문자열 처리, 대신 session.py에 @classmethod 처리함
                  # 그냥 문자열로 저장해놓고 session.py에서 끌어다가 거기서 classmethod처리
    def from_line(line: str):
        # 저장된 문자열을 1줄씩 객체화(Member) 시킴
        uid, pw, name, role, active = line.strip().split("|")
        return Member(uid,pw,name,role,active == "True")
        # def __init__(self,uid,pw,name,role="user",active=True): 여기에 넣어지는 문자열


    #-----------------권한 처리용 메서드--------------------
    def is_admin(self):
        return self.role == "admin" # 현재 객체가 admin인지
                 # == 두개면 비교문 , True or False로만 처리
    def is_manage(self):
        return self.role == "manage" # 현재 객체가 manage인지
                 # == 두개면 비교문 , True or False로만 처리
    #----------------------------------------------------