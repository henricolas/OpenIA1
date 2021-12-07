from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
from GibBot import ask, append_interaction_to_chat_log
app = Flask(__name__)

app.config["SECRET_KEY"] = 'The fam,ous effel tower is really popular in paris'
@app.route('/GibBot', methods=['POST'])
def jabe():
 incoming_msg = request.values['Body']
 chat_log = session.get('chat_log')
 answer = ask(incoming_msg, chat_log)
 session['chat_log'] = append_interaction_to_chat_log(incoming_msg, answer,
 chat_log)
 msg = MessagingResponse()
 msg.message(answer)
 return str(msg)
if __name__ == '__main__':
 app.run(debug=True)