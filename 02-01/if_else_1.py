#if 조건문 (만약 ~라면) 
#소프트웨어 로직을 컨트롤한다.

#code_challenge에서의 상황을 예로 들어보자
def plus(a, b):
    #파이썬의 if 조건문 형식
        # if condition:
            # 긍정조건문
        # else:
            # 부정조건문
    #총 3레벨 뎁스까지 들여쓰기를 함
    #condition 뒤 콜론은 반드시 붙여야함

    #if type(b) is str: #if 뒤 문장 type(b) is str이 condition
              # is는 operation(is not도 있음)
                  #"str"이 아닌 이유 : str자체가 string이라는 타입을 나타냄
        #return None #아무것도 반환하지 않을 것임
    #else:
        #return a + b

    #if type(b) is str: 라는 조건문은 한계가 있음 
        #유저가 str을 쓸지 bool을 쓸지 어떤걸 쓸지 모르기때문에 로직을 바꿔야 함
            #ㄴ>유저가 b의 자료형을 정수형 혹은 소수형을 쓴다면?
            #a +b를 반환할것
            #아니면 아무것도 반환 안함
    if type(b) is int or type(b) is float:
        return a + b
    else:
        return None

r_plus = plus(2, 10.3)
print(r_plus)
