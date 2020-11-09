from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

# Chrome 웹 드라이버 생성
driver = webdriver.Chrome('./chromedriver.exe')

# 네이버 로그인 페이지 url
#url = "https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com"

url = 'https://library.busan.go.kr/gsmbooks/member/login'
# url 로딩
driver.get(url)

# 로그인 정보 입력
# 네이버 로그인
'''
id = 'next450'
pw = 'kdy1023!'
'''
# 도서관 로그인
#'''
id = 'next450'
pw = 'sktkrkwk51!'
#'''

driver.execute_script("document.getElementsByName('id')[0].value=\'" + id + "\'")
# time.sleep(1)
#driver.execute_script("document.getElementsByName('pw')[0].value=\'" + pw + "\'")  #네이버
driver.execute_script("document.getElementsByName('password')[0].value=\'" + pw + "\'")   #도서관
# time.sleep(1)
#driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
driver.find_element_by_xpath('//*[@id="save-btn"]').click()     # 도서관 들어가기
