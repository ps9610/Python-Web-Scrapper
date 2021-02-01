# sequence type : dictionary
# 값들이 서로 대응 관계를 갖음
# Object, reference와 같이 단순 리스트 이상을 원할 때 

#딕셔너리 = key : value로 이루어짐
# 딕셔너리는 {} ( 리스트는 [], 튜플은 () )
sohye = {
    "nickname": "elly",
    "age": 26,
    "alien": True,
    "fav_food": ["choco","snack"]
}
print(sohye)
    #>>>{'nickname': 'elly', 'age': 26, 'alien': True, 'fav_food': ['choco', 'snack']}
        #ㄴ> 하나의 정의내려진 사전이 만들어짐
# 이 중에서 sohye의 age를 알아내려면 어떻게 해야할까?
print(sohye["age"])
    #>>>26
# sohye에 정보를 추가하고 싶다면
sohye["highschool"] = "chungshin girl's high school"
print(sohye)
    #>>>{'nickname': 'elly', 'age': 26, 'alien': True, 'fav_food': ['choco', 'snack'],  
        #'highschool': "chungshin girl's high school"}