# 서버에 POST 요청하고 입력받은 id, password 넘기기
import requests, json
url='http://localhost:5005/login'
headers = {'Content-Type' : 'application/json; charset=utf-8'}

input_id = input('ente!r the id : ')
input_pass = input('enter the password : ')

data = {'id' : input_id, 'password' : input_pass}
res = requests.post(url, headers = headers, data=json.dumps(data))
print(res.url)
print(res.text)