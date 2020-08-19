# 서버에 POST 요청하고 id, password 넘기기
import requests, json
url='http://localhost:5002/login'
headers = {'Content-Type' : 'application/json; charset=utf-8'}

data = {'id' : 'nanhee', 'password' : 'nanhee0225!'}
res = requests.post(url, headers = headers, data=json.dumps(data))
print(res.url)
print(res.text)