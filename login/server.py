from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route("/login", methods = ['POST'])
def hello_first():
	if request.method == 'POST':
		input_id = request.json['id'] # id에 해당하는 값 받아오기
		input_password = request.json['password'] # password에 해당하는 값 받아오기

		print(input_id, input_password)

		if (input_id=='nanhee' and input_password=='nanhee0225!'): # 받은 id, password가 일치하면 'success'출력
			return jsonify('{ state : success }') # result 값 반환하기
		else:
			return jsonify('{ state : fail to login }') # 틀리면 'fail'출력 
	return 'failed'

if __name__ == "__main__":
    app.run(port="5002")