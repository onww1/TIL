#-*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup as bs

LOGIN_INFO = {
	'login_user_id' : '',  # boj ID
	'login_password' : ''  # boj PW
}

with requests.Session() as s:
	# login
	req = s.post('https://www.acmicpc.net/signin', data=LOGIN_INFO)
	if req.status_code == 200: 
		print('login success')
	else:
		print('login failure')
		raise Exception('로그인이 되지 않았습니다.')

	while True:	
		try:
			# 몇 개의 파일명을 줄지 정하지 않고, 더 이상 없을 때까지 받아서 exception을 발생시키고,
			# 해당 exception이 발생하면 루프를 종료하는 방식으로 진행한다.
			files = input().split()	
		except:
			break

		# 입력받은 파일명들을 하나씩 접근하여 처리한다.
		for file in files:
			name = file.split('.')						# 파일명과 확장자를 분리한다.
			search_url = 'https://boj.kr/' + name[0][3:]			# 검색 url을 만든다.
			page = s.get(search_url)					# request로 해당 문제를 연다.
			html = page.text						# html을 받아온다.
			soup = bs(html, 'html.parser')					# bs를 이용하여 파싱한다.

			problem_name = soup.select('#problem_title')[0].text 		# 문제 이름을 얻는다.
			print(name[0][3:] + ' ' + name[1] + ' ' + problem_name, end=' ')# 문제 번호, 확장자, 문제 이름을 출력

			spoilers = soup.select('#problem_tags > ul > li')		# 알고리즘 분류에 해당되는 태그들을 가져온다.
			for spoiler in spoilers:					# 발견된 태그들을 하나씩 출력한다.
				print(spoiler.text, end=' ')
			print('')			
