    #print와 return의 차이에 대해서 알아보자
def p_plus(a, b):
    print(a + b)

def r_plus(a, b):
    return a + b

p_result = p_plus(2, 3)
r_result = r_plus(2, 3)
print(p_result, r_result) 
#>>>5, None 5
    #ㄴ>첫번째 5는 line 3의 print(a+b)
    #ㄴ>두번째는 p_result = none, r_result = 5가 나왔다. 
        #none이 나온 이유는 p_plus는 되돌아오는 값이 없기 때문에 none
        #print(a+b)는 어떤 결과값이 아니고 단순히 print()라는 함수를 실행했을 뿐이다.
    