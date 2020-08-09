# 서버에서 내용 읽어오기
import requests, json
url='http://localhost:5001/'
headers = {'Content-Type' : 'application/json; charset=utf-8'}

data = {'x' : 5, 'y' : 8}
res = requests.post(url, headers = headers, data=json.dumps(data))
print(res.url)
print(res.text)