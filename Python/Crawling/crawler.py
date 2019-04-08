#-*- coding:utf-8 -*-

from selenium import webdriver
from bs4 import BeautifulSoup as bs

user_id = '' # BOJ ID
user_pw = '' # BOJ Password

# Chrome driver option
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument('disable-gpu')

# chromedriver의 경로를 넣어준다.
driver = webdriver.Chrome('chromedriver_path', chrome_options=options) 

# login page를 켜고, 주어진 ID와 PW를 input 칸에 넣어준 후 로그인 버튼을 클릭한다.
driver.get('https://www.acmicpc.net/login?next=%2F')
driver.find_element_by_name('login_user_id').send_keys(user_id)
driver.find_element_by_name('login_password').send_keys(user_pw)
driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/div/form/div[4]/div[2]/button').click()

print("I'm ready") # 위의 처리가 다 끝나고 준비가 되면 신호를 준다.

while True:	
	try:
		# 몇 개의 파일명을 줄지 정하지 않고, 더 이상 없을 때까지 받아서 exception을 발생시키고,
		# 해당 exception이 발생하면 루프를 종료하는 방식으로 진행한다.
		files = input().split()	
	except:
		break

	# 입력받은 파일명들을 하나씩 접근하여 처리한다.
	for file in files:
		name = file.split('.')							# 파일명과 확장자를 분리한다.
		search_url = 'https://boj.kr/' + name[0][3:]				# 검색 url을 만든다.
		driver.get(search_url)							# selenium으로 해당 문제를 연다.
		html = driver.page_source						# html을 받아온다.
		soup = bs(html, 'html.parser')						# bs를 이용하여 파싱한다.

		problem_name = soup.select('#problem_title')[0].text 			# 문제 이름을 얻는다.
		print(name[0][3:] + ' ' + name[1] + ' ' + problem_name, end=' ')	# 문제 번호, 확장자, 문제 이름을 출력

		spoilers = soup.select('#problem_tags > ul > li')			# 알고리즘 분류에 해당되는 태그들을 가져온다.
		for spoiler in spoilers:						# 발견된 태그들을 하나씩 출력한다.
			print(spoiler.text, end=' ')
		print('')			
	break										# 마지막에 줄을 바꿔준다.

driver.quit()
