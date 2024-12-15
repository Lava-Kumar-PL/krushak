from twilio.rest import Client

account_sid = os.getenv("twilio_ssid")
auth_token = os.getenv("twilio_token")
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_=os.getenv("twilio_number"),
  body='Hello I am Your Assistant "KrushakAI", How can i Help you Today?',
  to= os.getenv("twilio_toNumber")
)

print(message.sid)