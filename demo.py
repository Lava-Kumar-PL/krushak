from twilio.rest import Client

account_sid = 'AC964b458a2b4c66e2b0fd9de0ab3a148c'
auth_token = '6fd33517a1a0983c9cfd992a0eb0f618'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  body='Hello I am Your Assistant "KrushakAI", How can i Help you Today?',
  to='whatsapp:+917676815877'
)

print(message.sid)