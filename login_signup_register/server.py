from flask import Flask, request, jsonify
import json

app = Flask(__name__)

set_information={ } # 딕셔너리 선언

@app.route("/signup", methods = ['POST']) # 회원가입
def nan():
	global set_information
	if request.method == 'POST':
		set_id = request.json['id'] # id 설정하기
		set_password = request.json['password'] # password 설정하기

		if set_id in set_information: # 딕셔너리에 id가 이미 존재하면
			return jsonify('{ state : defined_id }') # 오류메세지 출력
		set_information[set_id]=set_password # id, password 딕셔너리에 저장
	return jsonify('{ state : success }')
	
@app.route("/login", methods = ['POST'])
def hee():
	global set_information
	if request.method == 'POST':
		input_id = request.json['id'] # id에 해당하는 값 받아오기
		input_password = request.json['password'] # password에 해당하는 값 받아오기

		if input_id in set_information: # 딕셔너리에 id가 존재할 때
			if(set_information[input_id]==input_password): # id 키 값에 맞는 password가 있으면
				return jsonify('{ state : success }') # success 반환
			else:
				return jsonify('{ state : fail_to_login }')
		else: # 딕셔너리에 id가 존재하지 않을 때
			return jsonify('{ state : undefined_id }')
	return 'failed'

if __name__ == "__main__":
    app.run(port="6000")