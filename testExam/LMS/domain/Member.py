class Member:
    #---------초기값 설정
    def __init__(self, uid, pw, name, role = "user", active = True):
            self.uid = uid
            self.pw = pw
            self.name = name
            self.role = role
            self.active = active

    #--------문자열
    def __str__(self):
        status = "활성" if self.active else "비활성"
        return f"{self.uid}|{self.name}|{self.role}|{status}"

    #--------데이터 저장 (직렬화)
    def to_line(self):
        return f"{self.uid}|{self.pw}|{self.name}|{self.role}|{self.active}"

    #--------파일 읽기 (역직렬화)
    @staticmethod
    def from_line(line:str):
        uid, pw, name, role, active = line.strip().split("|")
        return Member(
            uid=uid,
            pw=pw,
            name=name,
            role=role,
            active=(active=="True"))

    #------권한 처리
    def is_admin(self):
        return self.role == "admin" #관리자
    def is_manage(self):
        return self.role == "manage" #매니저
