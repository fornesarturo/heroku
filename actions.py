def generateAnswer(text):
    if "hej" in text.lower():
        return "Hej, jag ar en djur.","text"
    else:
        return "Jag ar Skoldpadda.","text"

class EntryManager(object):
    def __init__(self,entry):
        self.entry = entry
        self.message_list = []
        for event in entry['messaging']:
            if(event.get("message")):
                self.message_list.append(event)
    def answerEntry(self):
        def getAnswer(event):
            if event.get("message"):
                sender = event['sender']['id']
                text = event['message'].get('text')
                if not text:
                    answer,_type = 'Nice ' + str(event['message']['attachments'][0]['type']),'text'

                else:
                    answer,_type = generateAnswer(text)

                if "text" in _type:
                    return {'sender':sender,'user_text':text,'text':answer,'type':_type}
        answer_list = map(getAnswer, self.message_list)
        return answer_list
