from flask import Flask, render_template, request
from twilio.rest import Client

app = Flask(__name__)

@app.route('/')
def demo():
    return "hello"

@app.route('/send', methods=['POST'])
def send_whatsapp():
    account_sid = 'AC36e5d266b52677fc40ac49767f7d08cb'
    auth_token = 'f5c89c225cee95f7ca2d47171e2bb738'
    from_whatsapp_number = 'whatsapp:+14155238886'
    to_whatsapp_number = 'whatsapp:+918210072487'

    client = Client(account_sid, auth_token)
    message_body = request.form['message']
    client.messages.create(body=message_body, from_=from_whatsapp_number, to=to_whatsapp_number)

    return 'WhatsApp message sent successfully!'

if __name__ == '__main__':
    app.run(debug=True)
