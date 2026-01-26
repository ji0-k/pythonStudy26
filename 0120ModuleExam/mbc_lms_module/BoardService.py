import os
class BoardService:

    def __init__(self,file_name="board.txt"):
        self.file_name = file_name  # 객체에 파일이름을 넣는다.
        self.board = []  # 객체에 board 리스트를 만들다.
        self.load_board()  # 아래에 선언된 load_board() 메서드를 호출한다.
        self.next_bno = 1 # 게시물 작성 시 처음 지정된 고유 번호 ,

    # ==========게시물 데이터 저장 파일 로드====================
    def load_board(self):
        self.board = []
        if not os.path.exists(self.file_name):  # 동일 디렉토리에 파일명이 없으면
            self.save_board()  # save_members()메서드 호출 (open()으로 파일생성)
            return  # load_members()메서드 빠져 나와라
        with open(self.file_name, "r", encoding="utf-8") as f:
            #      board.txt  읽기전용          한글처리  -> f라는 변수에 넣어라
            for line in f:  # f변수에 있는 파일개체를 줄단위로 반복함
                data = line.strip().split("|")  # 1줄 읽은 값을 엔터제거 | 파이프 기준으로 잘라 -> 일차원리스트 생성
                # ["writer","pw","no","title","contents" ] 여기서 True는 문자열로 인식
                self.board.append(data)
                # 2차원 배열인 members 맨뒤에 추가 ~ for 종료
    #=========================================================

    #===========게시물 데이터 저장 ============================
    def save_board(self):  # board의 2차원 리스트 값을 파일로 덮어쓴다. memory->file
        # why? 파일처리는 수정을 하지않는다. r(읽기전용), w(덮어쓰기), a(마지막에 추가)
        with open(self.file_name, "w", encoding="utf-8") as f:
            #     board.txt   덮어쓰기         한글처리  -> f라는 변수에 넣어라
            for b in self.board:  # 메모리에 있는 board 2차원 리스트를 1줄씩 가져와서
                # b변수에 넣어라
                f.write(f"{b[0]}|{b[1]}|{b[2]}|{b[3]}|{b[4]}\n")
                # b =  [ ID | PW | No. | title | contents ] -> write 저장, for 종료까지
    #=================================================================================

    #==============게시물 등록===========================
    def add_board(self): # self는 클래스의 객체 주소
        bno = self.next_bno
        self.next_bno += 1
        print("\n[게시물등록]")
        bid = input("작성자 : ") # 세션적용시 세션아이디 연결
        bpw = input("게시물비밀번호 : ")
        title = input("게시물 제목 : ")
        contents = input("작성 내용 : ")

        #---------------------변수 입력완료

        print("="*60)
        print(f"게시물 작성자 : {bid} 게시물 비밀번호 : {bpw}")
        print(f"게시물 제목 : ")
        print(f"게시물 내용 : \n{contents}")
        print("=" * 60)
        # ------------------- 변수 입력내용 출력 확인 완료
        subselect = input("확인 후 게시물을 등록하시려면 y : ")
        if subselect == "y":
            self.board.append([bid, bpw, str(bno), title, contents])
            self.save_board()
            self.load_board()
            print("게시물 등록이 완료되었습니다.")
        return
    #===========================================================
    #=================게시물보기==================================
    def view_board(self):
        subrun = True
        while True:
            self.list_board()
            print(f"1.게시물자세히보기\n0.돌아가기")
            back = input(">>>")
            if back == "1":
                subselect = input("자세히보기 할 게시물의 게시번호 입력 : ")
                for b in self.board :
                    if b[2] == subselect :
                        print("=" * 80)
                        print(f"제목 : {b[3]:10} 작성자 : {b[0]:10}")
                        print("-" * 80)
                        print(f"내용 : {b[4]}")
                        print("=" * 80)
                        print(f"1.다른게시물보기\n2.돌아가기\n3.종료하기")
                        choose = input(">>>")
                        if choose == "1":
                            continue
                        elif choose == "2":
                            run = False
                        elif choose == "3":
                            exit()
                        else :
                            print("잘못된 접근")
            elif back == "0":
                return
            else :
                print("잘못된 접근")
    #===========================================================

    #================게시물수정==================================
    def modify_board(self):
        self.list_board()
        target_bno = input("수정할 게시물 게시번호 입력 : ").strip()
        target_pw = input("게시물 비밀번호 입력 : ").strip()


        target_idx = None
        for idx, b in enumerate(self.board):
            if b[2] == target_bno:
                target_idx = idx
                break

        if target_idx is None:
            print("해당 게시번호의 게시물이 없습니다.")
            return


        if self.board[target_idx][1] != target_pw:
            print("비밀번호가 일치하지 않습니다.")
            return


        current_title = self.board[target_idx][3]
        current_contents = self.board[target_idx][4]

        print("-" * 80)
        print(f"현재 제목: {current_title}")
        new_title = input("새 제목(그대로 두려면 엔터): ").strip()
        if new_title == "":
            new_title = current_title

        print("-" * 80)
        print("현재 내용:")
        print(current_contents)
        new_contents = input("새 내용(그대로 두려면 엔터): ").strip()
        if new_contents == "":
            new_contents = current_contents


        self.board[target_idx][3] = new_title
        self.board[target_idx][4] = new_contents

        print("수정 완료")
    #==========================================================

    #================게시물삭제=================================
    def delete_board(self):
        self.list_board()
        del_bno = input("삭제할 게시물 게시번호 입력 : ").strip()
        del_bpw = input("삭제할 게시물 비밀번호 입력 : ").strip()

        del_idx = None
        for idx, b in enumerate(self.board):
            if b[2] == del_bno:
                del_idx = idx
                break

        if del_idx is None: #게시물 번호 잘못입력
            print("해당 게시번호의 게시물이 없습니다.")
            return

        if self.board[del_idx][1] != del_bpw: # 게시물의 비번틀릴때
            print("비밀번호가 일치하지 않습니다.")
            return

        self.board.pop(del_idx)
        self.save_board()
        self.load_board()

        print("게시물 삭제 완료")
    #=========================================================

    #=================게시물 리스트 띄우기용 함수=================
    def list_board(self):
        print("=" * 80)
        print("[게시물 목록]")
        print("-" * 80)
        for b in self.board:
            print(f"게시번호 : {b[2]:10} 제목 : {b[3]:10} 작성자 : {b[0]:10}")
        print("=" * 80)

    #=========================================================

#===========게시판메뉴 주 실행문============================

    def run(self):
        subrun = True
        while subrun:
            print("""
============================
엠비씨 아카데미 LMS 서비스 
 : 자료게시판
----------------------------
1. 게시물 보기
2. 게시물 등록
3. 게시물 수정
4. 게시물 삭제
----------------------------
0. 종료
""")
            subselect = input(">>>")
            if subselect == "1":
                print("게시물보기 메서드 호출")
                self.view_board()
            elif subselect == "2":
                print("게시물등록 메서드 호출")
                self.add_board()
            elif subselect == "3":
                print("게시물수정 메서드 호출")
                self.modify_board()
            elif subselect == "4":
                print("게시물삭제 메서드 호출")
                self.delete_board()
            elif subselect == "0":
                print("자료게시판 서비스 종료")
                subrun = False
            else :
                print("잘못된 접근")

if __name__ == "__main__": #이거 왜 작동한거야?
    service = BoardService()
    service.run()
#=======================================================끝