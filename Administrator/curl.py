import requests
import json

url = 'https://api.line.me/v2/bot/message/multicast'
contentType = 'application/json'
token = 'Qdvy5JuxLD7TjNRoPE+h6llvyWsw/3eJViOpefrvuNRqEjiblq89f39GJLd/Kez+JjaizCQIzZU7sqhBViob2VQuYE7fkOfNDohMrLqVq7hNjx0bqbAa4EdIrYSMLrhJiumk6BgyPvngB+egq/ag1gdB04t89/1O/w1cDnyilFU='
authorization = 'Bearer '+token

#payload = '{ 'to': ['U1cda7f491951a136c01015ce7a9d0714'], 'messages': [ {'type':'text','text':'KK'] }'
payload = {}
payload['to'] = ['U1cda7f491951a136c01015ce7a9d0714']
msg = {}
msg['type'] = 'text'
msg['text'] = 'KKK'
payload['messages'] = [msg]
print(payload)
header = { 'content-type' : contentType, 'Authorization': authorization } 
r = requests.post(url, data=json.dumps(payload), headers=header)
print(r)
