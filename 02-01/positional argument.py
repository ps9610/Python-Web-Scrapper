#입력 변수(argument) 받는 방법 알아보기
def say_hello(who):
        #입력 변수는 말 그대로 변수를 받아주는 매개체(다리)역할이라고 하면 됨
        #함수 이름 옆 소괄호 안에 입력 변수 이름 써주기 / who 
    print("Hello", who) #who는 (매개체)다리역할이기 때문에 실제로 who의 자리를 받아주는 무엇인가가 대기해야함

say_hello("소혜") #여기서 입력 변수 받음
    #>>>Hello 소혜

#입력 변수를 이용한 계산기능 만들기
def plus(a, b):
    print(a + b)

plus(2, 5) #>>>7

def minus(a, b):
    print(a - b)

minus(2, 5) #>>>-3

#입력 변수의 갯수와 호출하려는 값의 갯수가 같아야함!
def minus(a, b=0):
    print(a - b)

minus(2) 
    #2만 호출하고 싶다고 이렇게 쓰면 입력 변수 갯수랑 호출값 갯수가 안 맞아서 에러남 
    #이럴땐 반드시 입력 변수에 값을 줘야함 | b=0으로 값을 줌
    # ㄴ> defalut Value라고 부름
    #>>>2



