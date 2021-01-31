# 들여쓰기 함부로 하면 IndentationError: unexpected indent 라는 오류남(들여쓰기 오류: 예기치 않은 들여쓰기)
# sequence type : list
# list 안의 요소(값)를 바꿀 수 있음 = mutable sequence

#여기 날짜를 모아놓은 리스트가 있다.
    # days = "Mon, Tue, Wed, Thur, Fri"
#3번째 요일을 구하려면?
    #print(days)
        #>>> Mon, Tue, Wed, Thur, Fri
        #ㄴ> 전체만 알 수 있을 뿐 요일은 알 수 없다!
        #이럴 때⭐list⭐를 활용하자
            #ㄴ>list는 많은 값을 하나의 list에 저장할 때 유용하다
#리스트로 만드는 방법은 변수 = [정수,"문자열",...]
days = ["Mon","Tue","Wed","Thur","Fri"]
print(type(days))
    #>>><class 'list'> / 이렇게 list로 타입이 바뀌어져 있다.

#list 연산자 사용하기 -1.  x in s
print("Mon" in days)
    #>>>True
print("Sun" in days)
    #>>>False


#list 연산자 사용하기 -2.  s[i]
#이제 3번째 요일을 구해보자
    #ㄴ>index값이기 때문에 0부터 시작 / 3번째라고 하면 index값은 2
print(days[2])
    #>>>Wed

#list 연산자 사용하기 -3.  len[s]
    #ㄴ> 리스트 안의 값들이 몇개인지 알고 싶을 때
print(len(days))
    #>>>5

#list 연산자 사용하기 -4. append(list에 요소 추가)
print(days)
days.append("Sat") #days라는 리스트 안에 Sat이라는 스트링을 append,추가하세요
print(days)
    #>>>['Mon', 'Tue', 'Wed', 'Thur', 'Fri']
    # >>>['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat']
        #ㄴ> Sat이 리스트에 추가되었음을 알 수 있음
        #ㄴ> 파이썬은 코드를 위에서 아래로 읽기 때문에 윗줄은 Sat이 없고 아랫줄은 Sat이 나온거임

#list 연산자 사용하기 -5. reverse(list 요소 거꾸로 배치)
print(days)
days.reverse()
print(days)
    #>>>['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat']
    #>>>['Sat', 'Fri', 'Thur', 'Wed', 'Tue', 'Mon'] / 요소들이 reverse, 거꾸로 배치되어 입력됐음