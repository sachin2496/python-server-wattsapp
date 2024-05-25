from flask import Flask, render_template, request
from twilio.rest import Client

app = Flask(__name__)

@app.route('/')
def demo():
    return "hello"

@app.route('/send', methods=['POST'])
def send_whatsapp():
    account_sid = 'AC21fa36c85fdee453c592064943a0b27e'
    auth_token = 'f784676f7c518c64d3d9506afe2799e5'
    from_whatsapp_number = 'whatsapp:+14155238886'
    to_whatsapp_number = 'whatsapp:+918210072487'

    client = Client(account_sid, auth_token)
    message_body = request.form['message']
    client.messages.create(body=message_body, from_=from_whatsapp_number, to=to_whatsapp_number)

    return 'WhatsApp message sent successfully!'

if __name__ == '__main__':
    app.run(debug=True)
