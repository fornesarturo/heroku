from flask import Flask, request, render_template, send_file

app = Flask(__name__)

@app.route(/sayhi, methods=['POST','GET'])
def sayingHi():
	if request.method == 'GET':
		return "Get this",200
	if request.method == 'POST':
		data = request.form
		return data,200


