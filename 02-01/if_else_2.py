#참, 거짓 로직

#나이를 보고 음주가능/불가능을 나타내기
    #18세 미만이면 음주 불가      (if)
    #18세 또는 19세면 뉴비                (if가 아니면, elif)
    #20~25세라면 아직 어려!       (if가 아니면, elif)
    #18세 이상이면 맛있게 드세요~ (else)

def age_check(age):
    print(f"you are {age}")
    if age < 18:
        print("you cant drink")
    elif age == 18 or age == 19:
        print("you are new to this!")
    elif age >=20 and age<=25: # and = 두 조건 모두 true
        print("you are still young")
    else:
        print("enjoy your drink")

age_check(29)
 