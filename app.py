from flask import Flask, request, render_template, send_file

app = Flask(__name__)

@app.route('/', methods=['GET'])
def verify():
    # when the endpoint is registered as a webhook, it must echo back
    # the 'hub.challenge' value it receives in the query arguments
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "verification_string@":
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200

    return render_template('index.html'), 200

@app.route('/', methods=['POST'])
def callback():
	data = request.get_json()
	if data == None:
		return request.form
	if data["object"] == "page":
		for entry in data["entry"]:
			answer(entry)
	return "OK", 200

def answer(entry):
	for message_event in entry['messaging']:
		if message_event.get('postback'):
			return
		if message_event.get('message'):
			return

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

@app.route("/Comment", methods=['GET'])
def postRequest():
    name = request.args.get("name")
    email = request.args.get("email")
    message = request.args.get("message")
    print(name+"\n"+email+"\n"+message)
    string = name+" "+email+" "+message
    return string,200
