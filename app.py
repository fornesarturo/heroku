from flask import Flask, request, render_template, send_file

app = Flask(__name__)


@app.route("/sayhi", methods=['POST','GET'])
def sayingHi():
	if request.method == 'GET':
		return "Get this",200
	if request.method == 'POST':
		request.get_data()
		data = request.json
		string = ""
		for key in data.keys():
			string += data[key]
		return string,200

@app.route("/Comment", methods=['POST'])
def postRequest():
	data = request.get_json(force=True)
	string = ""
	for key in data.keys():
		string += data[key]
	return string,200
