 # trt-finally : try문 수행중 예외 발생 여부에 상관없이 무조건 수행 되는 문장

try : # 예외가 발생할거같은 실행문
    f = open('foot', 'w')
    # 이것 저것 실행문

finally: # 중간에 오류가 나도, 안나도 실행 , 그냥 실행
    f.close()

# finally 뒤에 close()로 닫아준다
