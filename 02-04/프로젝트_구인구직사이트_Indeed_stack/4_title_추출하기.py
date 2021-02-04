import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}" 

#indeed 페이지를 추출하는 함수
def extract_indeed_pages():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("div", {"class" : "pagination"})

    links = pagination.find_all("a")
    pages = []

    for link in links[:-1] :
        pages.append(int(link.string))
        
    max_page = pages[-1]
    return max_page

#2번째 request : indeed 페이지의 마지막 페이지까지 낱개로 배열
def extract_indeed_jobs(last_page):
    jobs = []
    #for page in range(last_page):  이렇게 하니까 모든 페이지의 h2 class="title"이 나와서 주석달고 다른 for문 만들거임
    result = requests.get(f"{URL}&start={0*LIMIT}") #for문 없앴으니까 page*LIMIT -> 0*LIMIT으로 변경
    soup = BeautifulSoup(result.text, "html.parser") #soup 이용해서 html 데이터 중 제목 부분을 추출할거임
    results = soup.find_all("div", {"class" : "jobsearch-SerpJobCard"}) # soup의 find_all 기능이 div class="jobsearch-SerpJobCard" 요소를 찾음
    #print(results)
    #for문을 사용해서 div class="title 안의 a title=""만 가져와서 제목만 추출할거임
    for result in results:
        title = result.find("h2",{"class":"title"}).find("a")["title"] #[]하면 attribute 써주기
        print(title)
    # print(result.status_code) / 작동이 잘 되는지만 확인
    return jobs 