#자주 쓰는 코드들을 함수로 묶어줌


import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}" 
    #대문자로 변수설정한건 수정하지 말라는 암묵적인 약속 
    # &start로 계속 요청을 보낼거라서 변수로 설정해줌 

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
def extract_indeed_jobs(last_page): #최대 페이지 갯수 받을것임
    jobs = []
    for page in range(last_page): #매개변수 last_page를 배열로
        #print(f"&start={page*LIMIT}")
        result = requests.get(f"{URL}&start={page*LIMIT}")
        print(result.status_code)
        return jobs # extract_indeed_jobs에서 모든 일자리를 추출한 후 빈 jobs array에 넣어서 return할거임

#for n in range(max_page) : 
    #print(n) # 배열은 0부터 시작하니까 0 1 2 3 4가 나옴
    #print( f"start={ n*50 }" )
    #현재 range의 값 = n 을 indeed에서 가져온 요소의 갯수 = 50개 만큼 곱해줌
    #이걸 indeend의 url(https://www.indeed.com/jobs?q=python&limit=50&start=0)에 있는 start에 넣어줌