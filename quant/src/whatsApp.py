# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
client = Client(account_sid, auth_token)


def sendWhatsAppNotification(messageBody):
    message = client.messages.create(
    body=messageBody,
    from_="whatsapp:+14155238886",
    to="whatsapp:+919836820018",
    )
    
    #print(message.body)
