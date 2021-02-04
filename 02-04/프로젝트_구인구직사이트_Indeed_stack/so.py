import requests
from bs4 import BeautifulSoup

URL = "https://stackoverflow.com/jobs?q=python&so_source=JobSearch&so_medium=Internal"

# 기본 설정
    # import requests 
    # from bs4 import BeautifulSoup
    # 변수 URL = https://stackoverflow.com/jobs?q=python&so_source=JobSearch&so_medium=Internal

# 1. page 추출
    # 먼저 함수 두개만들기
        # 하나는 main이랑 이어지는 함수 def get_jobs()
        # 하나는 기능 수행하는 함수 def get_last_page()
    # def get_last_page()에서
        # 1. requests.get(URL) = url 가져오라고 requests
            # ㄴ> result 변수로 묶기
        # 2. "html.parser" = html의 구문을 분석해라, 즉 result를 text로 나타내는데 html의 구문을 분석한 걸 나타내라
            # ㄴ> soup 변수로 묶기
        # 3. soup(가져온 url 에서 text로 나타낸 것 중에 html의 구문을 분석한 것 중)에서 div class="s-pagination"를 찾아라,
        # 그리고 그 안에 a 링크를 찾아라
            # ㄴ> pages 변수로 묶기
        # 4. 이제 next 없애주기
            # pages에서 제일 마지막 순서 -1(next btn)의 전 -2를 text로 가져와라(get_text)
                #ㄴ> last_page 변수로 묶기
            # white space 제거 -> strip=True
        # 5. last_page(next-btn없는 페이지만 나옴)를 인자로 받는 함수 생성 = def extract_jobs(last_page)
            # last_page는 a 링크 중 마지막에서 두번째까지[-2] 만 text로 받아오고 공백은 없애기(stript = True)
        # 6. jobs라는 empty 리스트 만들어놓고 loop 바깥쪽으로 for문 형성
            # main과 import 되어있는 함수 get_jobs에 연결
        # 7. for문 = last_page 전체 범위를 낱개로 뿌려라 (변수 page로 받음)
            # page가 인덱스 넘버라 0부터 시작하니까 +1해서 1부터 시작하게 함

def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class":"s-pagination"}).find_all("a") #find_all 아니고 find면 한개만 찾아옴
    last_page = pages[-2].get_text(strip=True)
    #-1은 마지막 순서 = next고 우리는 next 전 = 페이지 중 마지막이 필요하니까 -2 
    return int(last_page)
    #print(last_page)
    
def extract_job(html):
    title = html.find("div", {"class":"fl1"}).find("h2").find("a")["title"]
    print(title)

def extract_jobs(last_page):
    jobs = []
    for page in range(last_page): # 복습 : range() -> 정수를 범위로 표시해주는 함수, type은 int를 사용해야한다.line 37 return에서 값을 반환받을때 type 바꿔주기
        result = requests.get(f"{URL}&pg={page+1}")
        #print(result.status_code) # url을 써줬으니까 작동하는지 보려고 status_code
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class":"-job"})
        for result in results:
            #print(result["data-result-id"])
            job = extract_job(result)
            jobs.append(job)
    return jobs

def get_jobs():
    last_page = get_last_page() #일단 중복되도 만들어놓고 나서 나중에 이름만 바꿔주면 됨
    jobs = extract_jobs(last_page)
    return jobs
# 2. request 요청
    #1. print(page+1)이 작동하면 requests 시작
        # 결국 여태까지 했던 page 구하기는 url에 써주기 위함이였음
            #ㄴ> result 변수로 묶기
    #2. result를 텍스트로 보이게 하고 html 구문 분석하게 하기
    #3. soup에서 div class="-job"을 찾아 모든 일자리 찾아내기
    #4. for문으로 낱개 낱개 보여지게 하기
# 3. job 추출
    #1. def extract_job () 함수 만들기
    #2. job 변수로 extract_job () 실행 + result 매개변수로 받기
    #3. 비어있는 리스트 jobs에 append
    #4. return jobs
# 파이썬 함수도 제이쿼리와 같이 스코프 안에 있는 변수는 서로 겹치지 않음

