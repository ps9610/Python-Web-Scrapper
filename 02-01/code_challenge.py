#계산기 만들기
#유저가 실수로 a,b에 문자를 대입했다면 숫자로 바꿔서 값을 출력하기

#x+y
def plus(a,b):
#a,b가 문자열이면 type을 integer로 바꾼다.
    if type(a) == str:
        a = int(a)
    if type(b) == str:
        b = int(b)
    return a+b
r_plus = plus("2", 10)
print(r_plus)

#x-y
def minus(a,b):
    if type(a) == str:
        a = int(a)
    if type(b) == str:
        b = int(b)
    return a-b
r_minus = minus("2", "10")
print(r_minus)

#x*y
def multy(a,b):
    if type(a) == str:
        a = int(a)
    if type(b) == str:
        b = int(b)
    return a*b
r_multy = multy("2", 10)
print(r_multy)

#x/y
def divide(a,b):
    if type(a) == str:
        a = int(a)
    if type(b) == str:
        b = int(b)
    return a/b
r_devide = divide("2", "10")
print(r_devide)

#x%y
def remind(a,b):
    if type(a) == str:
        a = int(a)
    if type(b) == str:
        b = int(b)
    return a%b
r_remind = remind(2, "10")
print(r_remind)

#-x
def negate(a,b=0):
    if type(a) == str:
        a = int(a)
    if type(b) == str:
        b = int(b)
    return -a
r_negate = negate("2")
print(r_negate)

#x**y
def power(a,b):
    if type(a) == str:
        a = int(a)
    if type(b) == str:
        b = int(b)
    return a**b
r_power = power("2", "10")
print(r_power)