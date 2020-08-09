from flask import Flask, request, jsonify
import json

app = Flask(__name__)


@app.route("/", methods = ['GET','POST'])
def hello_first():
	if request.method == 'POST':
		x = request.json['x']
		y = request.json['y']
		print(x, y)
		return jsonify('{ result : %d }' % (x + y))
	return 'failed'

if __name__ == "__main__":
    app.run(port="5001")