# 오류 회피하기 : 코드를 작성하다 보면 특정 오류가 발생해도 그냥 통과해야할때

students = ["김기원","조정화","김수빈","이재정"]

for student in students:
    # 리스트에서 1개씩 꺼내와 students변수에 넣음
    try :
        with open (f"{student}_성적.txt","r",encoding="utf-8") as f:
            score = f.read()
            #파일에 있는 내용을 불러와 score에 넣음
            print(f"{student}의 성적 : {score}")
            #score변수에 있는 내용을 출력
    except FileNotFoundError :
        print(f"{student}의 성적 파일이 없습니다.")
        print("다음 학생으로 넘어갑니다")