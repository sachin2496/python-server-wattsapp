# from twilio.rest import Client

# account_sid = 'AC36e5d266b52677fc40ac49767f7d08cb'
# auth_token = '1a123b9d22066b7af2eb1804822be71b'
# client = Client(account_sid, auth_token)

# message = client.messages.create(
#   from_='whatsapp:+14155238886',
#   body='Your appointment is coming up on July 21 at 3PM',
#   to='whatsapp:+917643927304'
# )

# print(message.sid)


from twilio.rest import Client
from flask import Flask, request

app = Flask(__name__)

@app.route('/submit_form', methods=['POST'])
def submit_form():
    account_sid = 'AC36e5d266b52677fc40ac49767f7d08cb'
    auth_token = ''
    client = Client(account_sid, auth_token)

    name = request.form['contactName']
    email = request.form['contactEmail']
    message = request.form['contactMessage']

    to_whatsapp_number = 'whatsapp:+917643927304'  # Replace with the recipient's WhatsApp number
    from_whatsapp_number = 'whatsapp:+14155238886'  # This is a Twilio Sandbox number

    message_body = f"New message from {name} ({email}):\n{message}"

    client.messages.create(body=message_body, from_=from_whatsapp_number, to=to_whatsapp_number)

    return 'WhatsApp message sent successfully!'

if __name__ == '__main__':
    app.run(debug=True)


