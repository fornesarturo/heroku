import json
import sys
import requests
from flask import Flask, request, render_template, send_file
from actions import *

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
    log(data)
    if data == None:
        return request.form
    if data["object"] == "page":
        log("I'm a page")
        for entry in data["entry"]:
            log("I'm an entry")
            log(entry)
            EM = EntryManager(entry)
            result_list = list(map(answer, EM.answerEntry()))
    return "OK", 200

def answer(answer_details):
    log(answer_details)
    params  = {"access_token": "EAAUXU7pfXaUBAN9LrhsBJg3lDS1bptbkiO7Md7s8nxZBk1fCPbQiQl5mnDKHG8n5czKEH9Ihdb5iaZCh5CzDWMQcKqf1GnEEcZBX8jUMbp30rZCyegawHgThxdkZCsG0XIKjdnExAoNFXl2tRlC2vejZCsK5myoMutTcQ8xfxezAZDZD"}
    headers = {"Content-Type": "application/json"}
    data = JSONify(answer_details)
    log(data)
    if(data is None):
        return None
    r = requests.post("https://graph.facebook.com/v2.6/me/messages",params=params,headers=headers,data=data)
    if r.status_code != 200:
        print(r.status_code)
        print(r.text)

#Generate Response
def generateQuickReplies(quick_type):
    if quick_type == 'options':
        return [
            {
                "content_type":"text",
                "title":"Help",
                "payload":"PAYLOAD_HELP"
             },
             {
                "content_type":"text",
                "title":"Vad är du?",
                "payload":"PAYLOAD_VAD"
             }
        ]
    return []

def JSONify(answer_details):
    log(answer_details)
    _type = answer_details['type']
    sender_id = answer_details['sender']

    if "text" in _type:
        message_answer = answer_details['text']
        data = {
                "recipient":{"id":sender_id},
                "message":{"text":message_answer}
                }
        data['message']['quick_replies'] = generateQuickReplies("options")
        return json.dumps(data)

#Deal with Entries

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

def log(message):
    print(str(message))
    sys.stdout.flush()
