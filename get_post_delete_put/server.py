from flask import Flask, request, jsonify
import sqlite3

conn = sqlite3.connect('server.db', isolation_level=None)
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username TEXT)")

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def hello():
    try:
        conn = sqlite3.connect('server.db', isolation_level=None)
        cur = conn.cursor()
        cur.execute("SELECT * FROM users")
        ret = cur.fetchall()
        print(ret)
        return jsonify(ret)
    except:
        return "get error"

@app.route("/", methods = ['POST'])
def post():
    try:
        conn = sqlite3.connect('server.db', isolation_level=None)
        cur = conn.cursor()
        return 
    except:
        return "post error"

@app.route("/", methods = ['PUT'])
def put():
    try:
        print(request)
        print(request.json)
        user = (int(request.json['id']), request.json['username'])
        conn = sqlite3.connect('server.db', isolation_level=None)
        cur = conn.cursor()
        cur.execute("INSERT INTO users(id, username) VALUES(?, ?)", user)
        return "put success"
    except:
        return "put error"

@app.route("/", methods = ['DELETE'])
def delete():
    return "delete"

if __name__ == "__main__":
    app.run(host="0.0.0.0")