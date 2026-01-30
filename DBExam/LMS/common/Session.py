# DB접속 관리 , 차후에 프론트엔드영역인 웹브라우저에서 세션 처리한다.
# Html, CSS , Js : W3C 웹표준
# 파이참에도 DB관리 메뉴 있음

#멤버서비스에서 로그인할때 객체 담아놓기,
#로그인
#로그아웃
#권한체크, admin, manage


import pymysql
# 외부에서 가져온 pymysql 터미널에서 위치 맞는지 확인후
# pip install pymysql 설치 삭제시에는 uninstall

class Session:
    login_member = None

    @staticmethod
    def get_connection():
        #print("DB연결")
        return pymysql.connect( # root계정 생성 쿼리정보 대소문자 확인
            host='localhost',
            user='mbc',
            password='1234',
            db='lms',
            charset='utf8mb4',
            cursorclass = pymysql.cursors.DictCursor

        ) #dict type으로 처리함


    @staticmethod
    def login(cls, member): #  MemberService에서 로그인시 객체를 담아놈
        cls.login_member = member

    @classmethod
    def logout(cls):  # 로그아웃 기능 (세션에 있는 객체를 None 처리함)
        cls.login_member = None

    @classmethod
    def is_login(cls): # 로그인 상태를 확인
        return cls.login_member is not None
      # 로그인 = True/ None = False

    # 추가: 권한 체크 메서드 (서비스 계층에서 사용됨)
    @classmethod
    def is_admin(cls):  # 로그인한 객체가 admin이냐??
        return cls.is_login() and cls.login_member.role == "admin"
        #     로그인 했고 role이 admin이면 True / None False

    @classmethod
    def is_manager(cls):
        # 매니저이거나 어드민이면 참 (보통 어드민이 매니저 권한을 포함함)
        return cls.is_login() and cls.login_member.role in ("manager", "admin")
        #  #로그인 = True이고 and 로그인 권한이 매니저나, 관리자 이면 참
