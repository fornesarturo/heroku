from translate import Translator

translator = Translator(to_lang="sv",from_lang="en")

def generateAnswer(text):
    if "hej" in text.lower():
        return "Hej, jag är en djur.","text"
    if "help" in text.lower():
        return "Type in 'translate ' followed by the expression you want translated: 'translate {expression}'","text"
    if "translate" in text.lower():
        if text == "translate" or text == "translate  ":
            return "Type in 'translate ' followed by the expression you want translated: 'translate {expression}'","text"
        message = text.replace("translate", "", 1).strip()
        if len(message) > 0:
            return translator.translate(message),"text"
        else:
            return "Empty message","text"
    else:
        return "Jag är Sköldpadda.","text"

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
