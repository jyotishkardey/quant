# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
client = Client(account_sid, auth_token)


def sendWhatsAppNotification(messageBody,enable_whatsapp_Notification):
    if enable_whatsapp_Notification == False:
        return
    message = client.messages.create(
    body=messageBody,
    from_="whatsapp:+14155238886",
    to="whatsapp:+919836820018",
    )
    
    #
if __name__ == "__main__":
    print('Quant WhatsApp Module Invoked')