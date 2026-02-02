class Board: #붕어빵 틀

    #붕어빵 속을 뭐로 채울지 재료 선언
    def __init__(self,id,title,content,member_id,active=True,writer_name=None, writer_uid=None):
        #                                               writer_name과 writer_uid에 기본값(None)을 설정해서,
        #                                               게시글 단독 조회와 JOIN 조회를 모두 하나의 클래스로 처리할 수 있습니다.

        self.id = id #게시글 번호선언 및 정의
        self.title = title # 제목 선언 및 정의
        self.content = content
        self.member_id = member_id # 작성자의 고유 번호 (FK)
        self.active = active # 삭제 여부 boolean 1/10
        #인스턴스변수 = 매개변수
        #인스턴스변수 : 객체가 생성되면서 삭제되는때까지 기억하는 변수
        #매개변수 : 메서드 호출 될때 잠깐 들어왔다가 사라지는 매개변수
        # 사라지면안되니까 인스턴스 변수에다가 넣어두기

        # JOIN을 통해 가져올 추가 정보들
        self.writer_name = writer_name
        self.writer_uid = writer_uid

        # 초기화(Definition): 외부에서 전달받은 값(title, content 등)을 선언한 변수에 실제로 집어넣어 값을 확정 짓습니다.
        # 이 메서드로 객체가 생성 될때 위의 선언된 데이터값을 가질거라 정의하는 설계도의 핵심과정
        # 객체가 사용할 데이터 저장소를 개설하고 값을 채우는 과정


    # 먹기 좋은 형태로 구워져 나오게 정의
    @classmethod
    def from_db(cls, row:dict): # 팩토리 메서드(Factory Method) 패턴
        # DB값 파이썬에서 볼 수 있게 통역해주는 역할
        # DB에서 갓 뽑아온 데이터(딕셔너리)를 우리 프로그램에서 쓰기 좋은 형태(Board 객체)로 가공하는 전용 가공소"
        return cls(
            id=row.get('id'), # 딕셔너리의 'id'값을 꺼내서 Board의 id에 대입
            title=row.get('title'), # 딕셔너리의 'title' 값을 꺼내서 Board의 title에 대입
            content=row.get('content'), # 딕셔너리의 'content' 값을 꺼내서 Board의 title에 대입
            member_id=row.get('member_id'), # 딕셔너리의 'member_id'값을 꺼내서 Board에 대입
            active=row.get('active'), # 딕셔너리의 'active' 값을꺼내서 Board에 대입
            writer_name=row.get('writer_name'), # join쿼리로 가져올 이름 대입
            writer_uid=row.get('writer_uid') # join쿼리로 가져올 아이디 대입
        )
        # row.get('키') : row['키']라고 쓰면 해당 키가 없을 때 에러가 나며 프로그램이 멈춥니다.
        # 하지만 .get()을 쓰면 값이 없을 때 에러 대신 None을 돌려주기 때문에 훨씬 안전합니다.

        # cls의 정체: @classmethod이기 때문에 첫 번째 인자로 클래스 자신(Board)을 받습니다.
        # return cls(...)는 결국 "나(Board)와 똑같이 생긴 객체를 하나 새로 만들어서 돌려줄게!"

    # 샘플, 시식 이렇게 넣어서 만들면 이런 붕어빵이 나온다
    def __str__(self): # 문자열 반환 , 객체를 출력할때 보여줄 모습 결정, 리턴값 필수
        writer = self.writer_name if self.writer_name else f"ID :{self.member_id}"
        #                       만약 작성자에 이름이있으면
        # 그 이름을 writer에넣고
        #                                            없으면 member_id를 출력한다
        return (f"{self.id:<5}" #4칸의 공간을 만들고 왼쪽 정렬합니다.
                f"{self.title:<25}" # 20칸의공간을 만들고 왼쪽 정렬
                f"{writer:<10}") # 10칸의 공간을 만들고 왼쪽 정렬





















