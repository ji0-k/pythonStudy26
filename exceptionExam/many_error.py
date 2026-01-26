 # 예외가 이것저것 생길 것 같다
 # try문 안에서 여러개의 오류를 처리

try :
    a = [1,2]
    print(a[3])
    4/0

# except ZeroDivisionError as e:
#     print(e)
#     print("0으로 나눠지는 예외 발생")
# except IndexError as e :
#     print(e)
#     print("리스트 인덱스 범위 초과")

except (ZeroDivisionError, IndexError) as e :
    print(e)
    print("0으로 나눴거나 리스트의 범위 초과 예외 발생")
    