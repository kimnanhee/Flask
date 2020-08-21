import requests, json

while(1):
	num = int(input('1.signup  2.login  3.change password => '))

	if num==1: # 회원가입
		url='http://localhost:5000/signup'
		headers = {'Content-Type' : 'application/json; charset=utf-8'}

		input_id = input('set the id : ')
		input_pass = input('set the password : ')

		data = {'id' : input_id, 'password' : input_pass}
		res = requests.post(url, headers = headers, data=json.dumps(data))
		print(res.text)

	elif num==2: # 로그인
		url='http://localhost:5000/login'
		headers = {'Content-Type' : 'application/json; charset=utf-8'}

		input_id = input('enter the id : ')
		input_pass = input('enter the password : ')

		data = {'id' : input_id, 'password' : input_pass}
		res = requests.post(url, headers = headers, data=json.dumps(data))
		print(res.text)

	elif num==3: # 비밀번호 재설정
		url='http://localhost:5000/change'
		headers = {'Content-Type' : 'application/json; charset=utf-8'}

		input_id = input('enter the id : ')
		input_pass = input('enter the password : ')
		input_new_pass = input('enter the new password : ')

		data = {'id' : input_id, 'password' : input_pass, 'newpassword' : input_new_pass}
		res = requests.post(url, headers = headers, data=json.dumps(data))
		print(res.text)
