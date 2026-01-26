# 로그인 상태 관리 클래스
# 현재 로그인한 회원(Member 객체)을 보관
# 전역변수 대신 객체로 돌려씀
# 로그인 , 로그아웃, 로그인 여부, 관리자인지

# 이곳은 객체가 돌아다녀야 됨 -> @classmethod 처리 필수

class Session:
    #def __init__(self): 초기화 필요없음
    # cls로 Member 를 활용하기 때문에

    login_member = None # 현재 로그인 객체
    # 로그인 했으면 login_member = Member()

    @classmethod #cls와 세트로 구현
    def login(cls,member): # Session.login(member.txt)
        # 로그인 성공하면 @staticmethod로 만든 객체를 클래스로 변환
        cls.login_member = member

    @classmethod
    def logout(cls):  # cls,member에서 member.txt 필요없어 # Session.logout()
        cls.login_member = None
        # 로그아웃하면 login_member = None 이 되겠지

    # “MemberService 클래스가 가지고 있는 login_member라는 변수에
    # 무언가가 들어있으면(True), 없으면(False) 라고 판단한다.”


    @classmethod # 클래스 메서드는 cls 를 쓰지 , self안씀
    def is_login(cls) : # 현재 로그인 상태인지
        return cls.login_member is not None # login_member cls안에 None이아니면 =로그인상태이면
        # cls : Member객체 ,

    @classmethod
    def is_admin(cls) : # 현재 admin상태인지 볼수 있음
        return cls.is_login() and cls.login_member.is_admin()
                            # and는 둘다 True이여야 True가됨

    @classmethod
    def is_manager(cls) : #현재 manage 상태인지 볼 수 있음
        return cls.is_login() and cls.login_member.is_manager()


    @classmethod
    def is_active(cls) :  # 현재 활,비 상태인지 볼 수 있음
        return cls.is_login() and cls.login_member.is_active()