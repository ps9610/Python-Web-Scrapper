#return에 대해서 더 알아보자
#return 밑으로는 어느 함수도 실행되지 않는다.
def r_plus(a, b):
    return a + b
    print("djfekjfiedjfdjkfdkjf jfiekjfiooje fef", True)
    
r_result = r_plus(2, 4)

print(r_result)
    #>>>6
    #왜 밑에 print함수는 실행되지 않았을까?
        #파이썬에선 하나의 함수에 하나의 결과 값만 출력받는다.
        #즉, 6이라는 하나의 결과값을 return했으니 그 이상의 일은 하지 않는 것.