#순서정리
# 1. import requests + requests의 get 메소드로 url 가져옴
# 2. import BeautifulSoup : 후
# 3. 변수 indeed_soup: list links에 쓰일 모든 페이지 수 가져옴
# 4. pagination : html 내 class가 pagination인 요소 모두를 딕셔너리 자료형으로 가져옴
# 5. pagination의 모든 a 링크를 links라는 변수로 만들어줌
# 6. for문을 이용해 links의 내용을 낱개로 하나 하나 분리 + links의 마지막 요소(next-btn)는 생략[:-1]
# 7. links 중에 span 요소만 찾아내기 위해 loop 범위 밖으로 empty list | pages=[]를 만들고 
    #빈 pages에 link에서 찾은 모든 문자열(페이지넘버)을 append(추가)한다.
# 8. 수동으로 여러 개의 request 보내기
# 9. indeed.py 생성 -> indeed 페이지를 추출하는 코드를 묶어 함수로 만들기
#10. indeed.py에서 extract_indeed_pages 함수 import하기 + 함수를 변수로 묶어 실행
#11. indeed 페이지의 마지막 페이지를 불러올 함수 만들기 + 

from indeed import extract_indeed_pages, extract_indeed_jobs    

last_indeed_page = extract_indeed_pages() # page를 가져오는 함수를 변수로 만들어줌
 
extract_indeed_jobs(last_indeed_page) # 함수 실행 시 마지막 페이지를 받아주는 매개변수 써줌

indeed-jpbs