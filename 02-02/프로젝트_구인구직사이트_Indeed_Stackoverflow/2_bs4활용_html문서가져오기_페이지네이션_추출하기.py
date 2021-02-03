import requests
indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")
from bs4 import BeautifulSoup # 여기서 soup은 데이터 추출하는 것, beautifulsoup은 이쁘게 데이터 추출하기?

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser") #해당 url 안의 모든 텍스트를 가져오는 것, html의 구문을 분석하는 라이브러리

#print(indeed_soup)

pagination = indeed_soup.find("div", {"class" : "pagination"}) #indeed_soup에서 찾은 결과를 pagination이라는 변수에 넣어줌

#print(pagination) -> pagination 안에서 리스트가 만들어짐

pages = pagination.find_all("a")
spans = []

#print(pages)

#전체 페이지가 몇개인지 찾기 위하여 각 anchor의 span을 찾아보자
    #1.  span 가져오기
        # pagination의 리스트를 변수 pages에 넣어줌
        #루프 바깥쪽에 비어있는 리스트 spans = []를 만들어줌
        # for문 사용하여 pages라는 리스트의 a를 처음부터 마지막까지 각각 page라는 변수로 대입시킴
        # 비어있는 spans라는 리스트에 append 메소드로 변수 page에서 span을 가진 page들을 추가시킴 = spans.append(page.find("span"))
for page in pages : #복습 : for 변수 in 리스트(튜플, 문자열 등등)
    spans.append(page.find("span")) #복습 : append(x) 리스트 맨 마지막에 x라는 요소를 추가시키는 함수
#print(spans)
    # 현재 화면에 보이는 모든 page number와 next btn까지 나옴
    
    # 이제 가장 뒤에 있는 next btn은 없애주자
        # 리스트의 인덱싱 중 [-1]은 마지막 요소를 말한다.
        #콜론 :을 붙이면 해당 요소 전까지 나타내라는 뜻
        #ㄴ> 같은 의미 0:-1 은 (처음부터 마지막 전까지)
print(spans[0:-1])

