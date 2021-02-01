 #입력 인수의 갯수와 대입할 값의 갯수가 같지 않을 수도 있을까?
 #keyword argument
    #인자의 갯수, 인자 위치에 상관 없이 인자 자체에 값을 줌
    #아주 많이 쓰이는 방법
    #인자가 아주 많을 때, 순서대로 입력하지 않아도 된다는 것이 가장 큰 장점

def plus(a, b):
    return a - b

result = plus(b=30, a=1)
print( result ) #>>>-29

#문자열로 결과값 받기
def say_hello(name, age):
    return f"Hello {name} you are {age} years old"
    return "Hello name you are age years old"

hello = say_hello("ellyy", 24)

print(hello) 
#>>>Hello name you are age years old
    # 변수가 대입되지 않고 ""안의 string이 그대로 출력되어 나옴

#변수를 대입하려면 두가지 방법이 있다.
    #1. 문자열끼리 +로 연결
    # return "Hello" + name + "you are" + age + "years old"
    #2. f(=format)와 {}를 이용
    #>>>Hello ellyy you are 24 years old와 같은 변수가 대입된 결과를 볼 수 있다.
