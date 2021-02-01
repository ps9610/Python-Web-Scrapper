#무한 루프(loop)
    #무한히 반복한다는 의미, 루프는 for문, while문에서 볼 수 있다

#for문(아주많이쓰임)
    #for 변수 in 객체:

#요일로 예를 들어보자

#복습 : 리스트[mutable], 튜플(immutable), 딕셔너리{key:value}
days = ("Mon","Tue","Wed","Thur","Fri")
#한 줄이 아니라 하나씩 출력해야 한다면? = 작업되는 배열의 값을 순차적으로 출력해야할때
#for x in days:
#    print(x)

#for문에서도 루프에서 빠져나올 수 있다.
for x in days:
    if x == "Wed": #if x is "Wed":랑 똑같은건데 파이썬 콘솔이 is 대신 == 쓰라고 했음( SyntaxWarning: "is" with a literal. Did you mean "=="? )
        break #루프에서 빠져나오는 방법
    else:
        print(x)

#list 말고 str에서도 사용 가능
for letter in "elly":
    print(letter)