#### Virtualenv

---

시스템에 설치되어있는 패키지와 격리된 가상의 환경을 만들어준다.

why? 프로젝트마다 필요한 패키지 버전이 다를 수 있는데, 이를 효과적으로 처리하기 위함



```
pip install virtualenv # 가상 환경 설치
virtualenv venv # 가상 환경 만들기
```

```
venv\scripts\activate # 실행환경 활성화
```



##### flask 설치

``` 
pip install Flask
```



기본 서버

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello"

if __name__ == '__main__':
    app.run()
```

hello.py

```
python hello.py # 실행
```



외부에서 접근이 가능하게 하려면 app.run() 함수에 인자로 host를 0.0.0.0으로 설정해준다.

```
app.run(host='0.0.0.0')
```

