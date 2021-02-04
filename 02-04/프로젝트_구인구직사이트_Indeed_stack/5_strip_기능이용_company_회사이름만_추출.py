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

#2번째 request : indeed 페이지를 첫 페이지~마지막 페이지까지 각 페이지마다 낱개로 배열
def extract_indeed_jobs(last_page):
    jobs = []
    #for page in range(last_page):
    result = requests.get(f"{URL}&start={0*LIMIT}") #soup object : 각 일자리
    soup = BeautifulSoup(result.text, "html.parser") #수프할 때 soup이랑 같음 = result를 텍스트로 모아둔게 다 섞여있다는 뜻인가....
    results = soup.find_all("div", {"class" : "jobsearch-SerpJobCard"})
    #print(results)
    for result in results:
        title = result.find("h2",{"class":"title"}).find("a")["title"] # 일자리 title 가져옴
        company = result.find("span",{"class":"company"}) # 일자리 conpany 가져옴 -> span 안에 a가 있는게 있고 없는게 있어서 if,else 써줄거임
        company_anchor = company.find("a")
        #만약 객체 company가 a 요소를 찾는다면(회사에 a 링크가 있으면) company_anchor(span안의 a의 문자열)을 프린트하라, 아니면 그냥 company(요소는 span)의 문자열을 가져와라
        if company_anchor is not None:
            company = str(company_anchor.string)
        else:
            company = str(company.string)
        #line 32에서의 company는 soup이였는데 if문에서 새롭게 정의내려줌 가능
        #현재 if문의 문제 : 각 문장에 빈 칸이 너무 많음 -> strip(delete)으로 정리
            #company = company.strip("F") # = company의 모든 F 지움
        company = company.strip() # = company의 모든 공백(whitrspace)를 지움
        print(company)
    return jobs 