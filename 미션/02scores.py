# 성적 처리용 프로그램을 개발해보자
# Create : 성적입력
# Read : 성적보기
# Update : 성적수정
# Delete : 성적삭제

#필요한 변수? []리스트 만들기 , -s 붙여서 구분하기 쉽게
sns = [] #학번
names = [] # 이름
kors = [] #국어점수, **연산처리 때문에 문자로 안쓰고 숫자 그대로 사용
engs = [] #영어점수
mats = [] #수학점수

# 위에 변수를 사용하여 연산하고 나온결과값이 될거기 때문에 변수만 만들어 놓고 , 리스트는 빈 배열 [] 로 만들어 놓는다
tots = []
avgs = []
grades = []

menu = """
======================
 엠비씨 아카데미 성적처리
======================
1.성적입력
2.성적보기
3.성적수정
4.성적삭제
5.프로그램 종료
======================
"""

run = True # 프로그램 실행중

while run : #run 변수가 False 처리 될때까지 반복
    # 콜론 아래줄에는 들여쓰기(4칸) 진행
    # 들여쓰기는 하위 실행문
    print(menu) #콘솔창에 메뉴를 출력
    select = input("1~5의 값 입력 : ") #selcet 변수에 숫자를 입력 받음
                   #키보드로 입력받는 곳 앞쪽에 출력 메세지
    if select == "1" : # 키보드 입력 받은 값이 "1"이면  # 값을 변수에 넣을때 = 하나 , 같을때 같냐 물어볼깨 == 두개
        print("학생 성적을 입력합니다.") # 상위 if 일때 처리되는 부분
        sn = input ("학번을 입력하세요 : ")
        name = input("이름을 입력하세요 : ")
        kor = int(input("국어 점수를 입력하세요 : ")) #키보드를 이용한 점수를 입력 받으면 문자로 인식되기 때문에
        eng = int(input("영어 점수를 입력하세요 : "))  # 연산을위해서 숫자로 강제 변환하기 위해 int로 감싸준다
        mat = int(input("수학 점수를 입력하세요 : "))

        #print("입력한 정보를 확인합니다.") #입력한 정보를 확인 할 수 있게 출력 해주기 위함
        #print("학번 : " +  sn)
        #print("이름 : " + name)
        #print("국어 점수 : " + kor)
        #print("영어 점수 : " + eng) # 이거 너무 길고 print에서 숫자가 같이 출력 되려면 str()으로 숫자를 문자로 변경해야함
        #print("수학 점수 : " + mat) # f 포매팅 사용 print(f"")로 일괄적으로 써서 문자 숫자처리고 용이하게함

        print(f"학번 : {sn}, 이름 : {name}, 국어 : {kor}, 영어 : {eng}, 수학 : {mat}" )

        if input ("저장하려면 y : ") == "y" : # 출력된 정보가 일치해서 저장하려면 "Y"를 입력하라는 문구
            sns.append(sn) # 입력 받은 정보를 리스트업 해주는 것
            names.append(name)
            kors.append(kor)
            engs.append(eng) # 변수뒤에 s는 배열 (리스트)라고 생각
            mats.append(mat) # 리스트.append() 괄호 안에는 입력받은 값
            tot = kor + eng + mat
            tots.append(tot)
            avgs.append(tot/3)
            if avgs >= "90" :
                grades = "A"
            elif avgs >= "80" :
                grades = "B"
            elif avgs >= "70" :
                grades = "C"
            elif avgs >= "60" :
                grades = "D"
            else :
                grade = "F"

            # 미션
            #if avgs
            print("저장완료")
        else :
            print("저장 되지 않았습니다. ")
            print("처음부터 다시 입력하세요. ")

    elif select == "2" : #상위 if 비교 후 아니고 다음 비교 하려고 elif
        print("학색들의 성적 보기를 실행합니다.")
        print("=====================================")
        print("[성적목록]")

        #리스트의 처음 부터 끝까지 반복용 # 끝이 있는 조건 비교 for문
        for i in range(len(sns)) :
        # len(sns) 리스트의 길이를 가져옴 -> 5 (기본값, 미리 입력한 리스트 수)
        # range((len(sns)) -> , range(5) 0에서 5까지 증가
        # i in 5 i값에 0~5까지 반복 하고 5범위까지 하고 끝
        # 결론 i 값이 인덱스로 사용함

            #오류발생으로 주석 처리 -> 이유는 ? index out of range
            #해결 방법 : append()
            #tots[i] = kors[i] + engs[i] + mats[i]
            #avgs[i] = tots[i] / 3
            #grades[i] = [] #미션

            tots.append( kors[i] + engs[i] + mats[i] )
            avgs.append(tots[i] / 3 )

            print("-------------------------------------")
            print("학번 : " + sns[i] + "ㅣ 이름 : "+ names[i])
            print("국어 : " + str(kors[i]) + "ㅣ 영어 : " + str(engs[i]) + "ㅣ 수학 : " + str(mats[i]))
            print("총점 : " + str(tots[i]) + "ㅣ 평균 : " + str(avgs[i]))
            print("-------------------------------------")
            # Traceback (most recent call last):
            # File "C:\python_study\02scores.py", line 87, in <module>
            # print("국어 : " + kors[i] + "영어 : " + engs[i] + "수학 : " + mats[i])
            # TypeError: can only concatenate str (not "int") to str
            # 프린트

    elif select == "3" :
        print("학생 성적을 수정합니다.")
        #수정은 국영수만 가능하게, 총점 평균은 수정이안되게
        #수정을 했을때 총점 평균이 다시 계산되게 함이 필요

        ##등록된 학생의 점수를 가져온다.
        #학번을 이용하여 학생을 찾는다.
        sn = input("수정할 학번 : ")
        if sn in sns : # 학번리스트 sns에 입력한 학번sn이 있는지 확인
            print("학번이 있습니다.")
            idx = sns.index(sn) #sns리스트에 입력된sn이 있는 인덱스를 idx로 지정
            print(f"이름 : {names[idx]}, 국어 : {kors[idx]}, 영어 : {engs[idx]}, 수학 : {mats[idx]}")

            ## 등록된 학생의 점수를 수정한다.
            kors[idx] = int(input("수정할 국어 점수 : "))
            engs[idx] = int(input("수정할 영어 점수 : "))
            mats[idx] = int(input("수정할 수학 점수 : "))

            tots[idx] = kors[idx] + engs[idx] + mats[idx]
            avgs[idx] = tots[idx] / 3



        else :
            print("학번이 없습니다.")
            print("처음으로 돌아갑니다.")

        #등록된 학생의 점수를 수정한다.

        #수정된 값을 기준으로 총점과 평균, 등급을 다시 업데이트해준다

    elif select == "4" :
        print("학생 성적을 삭제합니다.")
        sn = input ("삭제할 학번 : ")
        if sn in sns :
            idx = sns.index(sn)
            print(f" 학번 : " + str({sns[idx]}) + "의 성적을 삭제하시겠습니까? " )
            # 리스트안에 값 삭제  .pop 주소로 삭제처리 , remove 이름 문자로 삭제처리
            sns.pop(idx)
            names.pop(idx)
            kors.pop(idx)
            engs.pop(idx)
            mats.pop(idx)
            tots.pop(idx)
            avgs.pop(idx)

    elif select == "5" :
        print("프로그램을 종료합니다.")
        run = False # while 문을 종료하여 프로그램이 꺼진다. #들여쓰기 주의
    else : # 메뉴선택 값 이외의 문자가 들어왔을때 잘못된 값 처리용
        print("1~5 값만 허용합니다.")

