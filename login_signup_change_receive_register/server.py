from flask import Flask, request
import json

app = Flask(__name__)

set_information={ } # 딕셔너리 선언
set_code={ } # 코드 저장 리스트
'''
{
	id:[code],
	id:[code],
	id:[code]
}
'''

@app.route("/signup", methods = ['POST']) # 회원가입
def signup():
	global set_information, set_code
	if request.method == 'POST':
		set_id = request.json['id'] # id 설정하기
		set_password = request.json['password'] # password 설정하기

		if set_id=='' or set_password=='': # id or pw가 공백이면 저장X
			return 'blank_input'

		if set_id in set_information: # 딕셔너리에 id가 이미 존재하면
			return 'defined_id' # 오류메세지 출력
		set_information[set_id]=set_password # id, password 딕셔너리에 저장
		set_code[set_id]=[]
	print(set_information) 
	return 'success'

@app.route("/login", methods = ['POST'])
def login():
	global set_information
	if request.method == 'POST':
		input_id = request.json['id'] # id에 해당하는 값 받아오기
		input_password = request.json['password'] # password에 해당하는 값 받아오기

		if input_id in set_information: # 딕셔너리에 id가 존재할 때
			if(set_information[input_id]==input_password): # id 키 값에 맞는 password가 있으면
				return 'success' # success 반환
			else:
				return 'fail_to_login'
		else: # 딕셔너리에 id가 존재하지 않을 때
			return 'undefined_id '
	return 'failed'

@app.route("/change",  methods = ['GET', 'POST']) # 비밀번호 변경
def change():
	global set_information
	if request.method == 'POST':
		input_id = request.json['id'] # id에 해당하는 값 받아오기
		input_password = request.json['password'] # password에 해당하는 값 받아오기
		input_new_password = request.json['newpassword'] # new password에 해당하는 값 받아오기

		if input_id in set_information: # 딕셔너리에 id가 존재할 때
			if(set_information[input_id]==input_password): # id 키 값에 맞는 password가 있으면
				set_information[input_id] = input_new_password # password 변경
				return 'success_change_password'
			else: # 비밀번호가 틀렸을 때
				return 'wrong_password'
		else: # 딕셔너리에 id가 존재하지 않을 때
			return 'undefined_id'
	return 'failed'

@app.route("/receive", methods = ['POST']) # 데이터 받기
def receive():
	global set_information, set_code
	if request.method == 'POST':
		input_id = request.json['id'] # id에 해당하는 값 받아오기
		input_password = request.json['password'] # password에 해당하는 값 받아오기
		input_code = request.json['code'] # 코드 받아오기

		if input_id in set_information: # 딕셔너리에 id가 존재할 때
			if(set_information[input_id]==input_password):
				set_code[input_id].append(input_code) # 받은 코드를 해당하는 id 리스트에 붙이기
				print(set_code)
				return 'code_receive_success'
			else: # 비밀번호가 틀렸을 때
				return 'wrong_password'
		else: # 딕셔너리에 id가 존재하지 않을 때
			return 'undefined_id'
	return 'failed'

@app.route("/request", methods = ['POST']) # request 요청이 들어오면 code보내주기
def code_request():
	global set_code
	if request.method == 'POST':
		input_id = request.json['id'] # id에 해당하는 값 받아오기

		if input_id in set_code: # 딕셔너리에 id가 존재할 때
			return str(set_code[input_id]) # code 전송
		else: # 딕셔너리에 id가 존재하지 않을 때
			return 'undefined_id'
	return 'failed'

if __name__ == "__main__":
    app.run(host="0.0.0.0")