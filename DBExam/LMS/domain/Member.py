# oop 기반의 Member 객체용

# 초기값 설정
# DB 값으로 가져오고 내보내기? DB연결?
# 로그인되어잇고 and 관리자or매니저일경우

class Member:
    def __init__(self, id, uid, password, name, role="user", active=True ): #초기값설정이기 때문에 role,active 값넣어줌
        self.id = id
        self.uid = uid
        self.password = password
        self.name = name
        self.role = role
        self.active = active
        #사용법 : member = Member("kkw","1234","김기원","admin", True)
        #                 Member 객체를 member에 넣음

    @classmethod # 초기값 설정 후 self라는 주소 말고 cls라는 객체 사용
    def from_db(cls,row:dict): # directory TYPE 명시
                               # dictcusor로 부터 전달받은 딕셔너리 데이터를 Member 객체로 변환
        if not row: # cls로전달받은 값이 없으면
            return None
        return cls(
            id=row.get("id"),
            uid=row.get("uid"),
            password=row.get("password"),
            name=row.get("name"),
            role=row.get("role"),
            active=bool(row.get("active")) # active: true -> 1 , False -> 0 , 불린
            )
    def is_admin(self):
        return self.role == "admin"
    def is_manage(self):
        return self.role == "manage"
    def __str__(self): # member객체 출력 (테스트용)
        return f"{self.id} | {self.uid} | {self.name} | {self.role} | {self.active}"
