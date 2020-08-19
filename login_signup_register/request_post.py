import requests, json

while(1):
	num = int(input('1.signup  2.login => '))

	if num==1: # 회원가입
		url='http://localhost:6000/signup'
		headers = {'Content-Type' : 'application/json; charset=utf-8'}

		input_id = input('set the id : ')
		input_pass = input('set the password : ')

		data = {'id' : input_id, 'password' : input_pass}
		res = requests.post(url, headers = headers, data=json.dumps(data))
		print(res.text)

	elif num==2: # 로그인
		url='http://localhost:6000/login'
		headers = {'Content-Type' : 'application/json; charset=utf-8'}

		input_id = input('enter the id : ')
		input_pass = input('enter the password : ')

		data = {'id' : input_id, 'password' : input_pass}
		res = requests.post(url, headers = headers, data=json.dumps(data))
		print(res.text)