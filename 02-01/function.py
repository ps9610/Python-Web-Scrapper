#함수 만드는 방법 (파이썬은 함수를 define(정의)한다고 한다.)
    #1. function의 이름을 쓴다. | say_hello
    #2. function옆에 소괄호 | say_hello()
    #3. ()를 채우거나 비워두면 끝
    #4. 함수를 정의할 땐 함수이름 앞에 def(함수를 정의한다는 뜻)
    #5. 함수 옆에 ⭐콜론⭐을 쓰고 body에 내용 입력
def say_hello(): 
    print("hello")
        # 파이썬은 자바스크립트 함수 function blabla(){}처럼 괄호로 묶지 않고
        #tab. space를 사용한 들여쓰기로 함수의 몸통을 결정한다.
        # = 들여쓰기 했다 = 함수임(들여쓰기 주의해서 쓰기)
        # 그리고 함수 소괄호 옆에 ⭐콜론⭐ 반드시 쓰기!!
    print("bye")

say_hello()
    #>>>hello
    #   bye