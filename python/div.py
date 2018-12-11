from flask import Flask, request
import json
import sys

app = Flask(__name__)

@app.route('/<float:a>/<float:b>')
def div(a,b):
    if(b is not 0):
        return a/float(b)

@app.route('/json')
def div()
	data = request.get_json()
	a = data['a']
	b = data['b']
	return div(a,b)
	
if __name__ == "__main__":
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    print(div(a, b))