#순서정리
# 1. import requests + requests의 get 메소드로 url 가져옴
# 2. import BeautifulSoup : 후
# 3. 변수 indeed_soup: list links에 쓰일 모든 페이지 수 가져옴
# 4. pagination : html 내 class가 pagination인 요소 모두를 딕셔너리 자료형으로 가져옴
# 5. pagination의 모든 a 링크를 links라는 변수로 만들어줌
# 6. for문을 이용해 links의 내용을 낱개로 하나 하나 분리
# 6. links 중에 span 요소만 찾아내기 위해 loop 범위 밖으로 empty list | pages=[]를 만들고 
    #빈 pages에 link에서 찾은 모든 span들을 추가한다.
    
import requests
from bs4 import BeautifulSoup #soup은 object
indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50&start=0")
indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")
#print(indeed_soup)

pagination = indeed_soup.find("div", {"class" : "pagination"})
#print(pagination)

links = pagination.find_all("a")
#print(links)
pages = []

for link in links[1:] : #index 1번(2번째 요소 = 1)부터 낱개로 뿌려라
    #pages.append(link.find("span"))
#print(pages[:0])
    #pages.append(link.find("span").string) #전체 요소까지 필요 없고 페이지가 몇 개인지만 알아내면 되니까 문자열만 가져오기
    pages.append(int(link.string)) #a -> span -> string이 하나밖에 없으면 a에서 바로 string을 찾으라고 해도 됨
#pages = pages[:-1]
#print(pages)
 #이렇게 하면 int() 인수가 nontype이 아닌 문자열,객체 또는 숫자여야 한다고 오류가 난다.
 #TypeError: int() argument must be a string, a bytes-like object or a number, not 'NoneType'
 #왜냐면 span의 마지막 부분을 생략한 건 pages지 links가 아니기 때문
    #pages = pages[:-1]를 생략하고 links에서 마지막 부분을 미리 생략해서 마지막 span인 next가 나옴을 방지하자

#이제 가장 큰(맨 뒤) 숫자를 찾자
max_page = pages[-1]
print(max_page)

