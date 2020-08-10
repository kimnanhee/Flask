from flask import Flask, request, jsonify
import json

app = Flask(__name__)

set_id=''
set_password=''

@app.route("/signup", methods = ['POST']) # 회원가입
def nan():
	global set_id, set_password
	if request.method == 'POST':
		set_id = request.json['id'] # id 설정하기
		set_password = request.json['password'] # password 설정하기
	return jsonify('{ state : success }')
	
@app.route("/login", methods = ['POST'])
def hee():
	global set_id, set_password
	if request.method == 'POST':
		input_id = request.json['id'] # id에 해당하는 값 받아오기
		input_password = request.json['password'] # password에 해당하는 값 받아오기

		print(input_id, input_password)

		if (set_id==input_id and set_password==input_password): # 설정된 정보와 비교
			return jsonify('{ state : success }') # result 값 반환하기
		else:
			return jsonify('{ state : fail_to_login }')
	return 'failed'

if __name__ == "__main__":
    app.run(port="5555")