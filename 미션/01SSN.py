# 주민번호를 입력 받아 생년월일 남여 구분을 하는 코드
# input() 함수를 사용하면 콘솔로 데이터를 넣을 수 있다.
# 처리 0 : 주민번호 입력 검증 -> 14글자인지 ? 7번째 (-) 유무
# 처리 1 : 생년월일을 추출 ! -> 1,2,5,6 1900년생 , 나머지 2000년생
# 처리 2 : 주민번호 8번째 글자를 추출 -> 남여 구분
# 처리 3 : 9~10 번째 글차를 추출 -> 출생지역

print("주민번호를 입력하세요(-포함 14글자)")
#print(">>>") #입력창 생략해도 된다
ssn = input(">>>")
print("입력된 주민번호 : " + ssn)

#입력된 주민번호 검증 코드
if len(ssn) == 14 : #입력 받은 문자열이 14자 인지 확인
        print("14자 입력이 확인 되었습니다.")
else :
        print("주민번호 14자가 입력되지 않았습니다.")
        exit(0) #강제 종료 됨
if ssn[6] == "-" :
        print("주민번호 7번째 구문자 인식완료")
else :
        print("주민번호 형식이 올바르지 않습니다.")
        print("프로그램을 처음부터 다시 실행하세요.")
        exit(0)  #for while 문에서는 break 로 쓰임

# 주민번호 앞 6자리를 생년월일로 추출 -> 1,2,5,6, 이면 1900년대
# 나머지는 2000년생

year = ssn[0:2] #생년
month = ssn[2:4] #생월
day = ssn[4:6] #생일
sex = ssn[7] # 성별
area = ssn[8:10]

fullyear = "" #if 안에서 변수 만들면 버그가 생길 수 있어서 변수 미리 만들고 조건문, "" null값

if ssn[7] in ["1","2","5","6"] :
        fullyear = "19" + year
else :
        fullyear = "20" + year

print("귀하의 생년은 " + fullyear + "년생 입니다.")

#나이계산 방법
age = 2026-int(fullyear)

print("귀하의 나이는" + str(age) + "세 입니다.")
# 문자열 안에 계산식은 넣지 않는다
# "문자" + 숫자 + '문자" , 숫자 문자열 혼합식은 출력 오류 발생
# 숫자를 문자열로 변환 (강제타입변환) -> str(age)

# 주민번호 8번째 숫자가 1,3,5,7 이면 남자, 나머지 여자
gender = "" #성별 null 변수 선언
if ssn[7] in ["1","3","5","7"] :
        gender = "남성"
elif  ssn[7] == "9" :
        gender = "외계인"
else :
        gender = "여성"
print("귀하는 " + gender + " 으로 판단됩니다.")

# 출생지역판단
# 항상 사용할 변수 먼저 만들기
local = ""
ssnlocal = ssn[8:10] #출생 지역 코드
if int(ssnlocal) <= 8 :
        local = "서울"
if int(ssnlocal) <= 12 :
        local = "부산"
if int(ssnlocal) <= 15 :
        local = "인천"
if int(ssnlocal) <= 23 :
        local = "경기"

print ("귀하의 출생지는 " + local + " 입니다.")


