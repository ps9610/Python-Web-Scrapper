# 1. requests module를 설치하고 가져오기
# 파이썬에서 요청을 만드는 기능 = requests / import requests를 사용할것
import requests

# 2. get 메서드를 이용하여 url 가져온 후, 변수(indeed_result) 만들기
indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")
              # requests.get() -> function안의 object가 있는 형태

print(indeed_result) # >>> <Response [200]> / 200 = okay
#print(indeed_result.text)로 페이지 전체의 html도 가져올 수 있음

# 3. 인디드 페이지 넘버 가져오기 -> beautifulsoup(html 정보를 추출하는 라이브러리) 이용
    # cmd로 beautifulsoup 설치하고 from bs4 import Beautiful 자동완성 뜨면 설치된것
from bs4 import BeautifulSoup

#파이썬만으로 url을 가져올 수 있다.
#라이브러리를 이용하면 더 편리하게 가져올 수 있다.
