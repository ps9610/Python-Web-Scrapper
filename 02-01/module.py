#Module(모듈)
    #모든 파이썬에 내장되어있는 모듈
    #함수, 변수, 클래스들을 모아 놓은 파일, 다른사람이 만든것도 있고 우리가 직접 만들수도있음
    #모듈을 갖다 쓸 수 있는데 이걸 import한다고 함
        #나중에 엑셀 파일을 정리한 것들 가져올 수 있는 cvs module도 있음
    

    #print(math.ceil(1.25))
        #에러원인 : math라는 모듈을 갖고오지 않았기 때문에 뭘 어떻게 print 하라는 건지 못 알아들었음
        #math를 import해주자

#import math #수학기능을 모아놓은 module

#print(math.ceil(1.25)) #올림
#print(math.fabs(-1.2)) #절대값

#모듈 전체를 가져오는건 비효율적, 본인에게 필요한 모듈만 가져올것!, 올림값과 합이 필요함, 특정함수 가져올땐 from 사용
    #모듈 가져와서 이름 바꾸기 가능, as 사용
from math import ceil, fsum as sexy_sum

print(ceil(1.2))
print(sexy_sum([1, 2, 3, 4, 5, 6 ,7]))

#내가 만든 calculator.py에서 모듈을 가져와서 사용할 수도 있음
from calculator import plus, minus

print(plus(1,2), minus(1,2))

#print 함수가 어떻게 무한으로 매개변수를 가질 수 있을까? -> django에서 이어짐 ㄷㄷㄷㅈ
