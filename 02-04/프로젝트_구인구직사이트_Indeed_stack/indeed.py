import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}" 

#indeed 페이지를 추출하는 함수
def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("div", {"class" : "pagination"})

    links = pagination.find_all("a")
    pages = []

    for link in links[:-1] :
        pages.append(int(link.string))
        
    max_page = pages[-1]
    return max_page

#일자리 타이틀, 회사 이름 추출하는 함수
def extract_job(html):
        title = html.find("h2",{"class":"title"}).find("a")["title"] # 일자리 title 가져옴
        company = html.find("span",{"class":"company"}) # 일자리 conpany 가져옴
        company_anchor = company.find("a")
        if company_anchor is not None:
            company = str(company_anchor.string)
        else:
            company = str(company.string)
        company = company.strip()
        #print(company)
        location = html.find("span",{"class":"location"}).string
        div_id = html["data-jk"]
        return {"title":title, "company":company, "location":location, "link":f"{URL}&vjk={div_id}"} 
    


#indeed 페이지를 첫 페이지~마지막 페이지까지 각 페이지마다 낱개로 배열
def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping page {page}")
        result = requests.get(f"{URL}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class" : "jobsearch-SerpJobCard"})
        
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs 
    
# 최대한 한 곳으로 모아서 정리하려고 함수만듬
def get_jobs():
    last_page = get_last_page() # page를 가져오는 함수
    jobs = extract_jobs(last_page) # 함수 실행 시 마지막 페이지를 받아주는 매개변수를 쓴 변수
    return jobs