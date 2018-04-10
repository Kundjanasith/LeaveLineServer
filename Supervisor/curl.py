import requests
import json

url = 'https://api.line.me/v2/bot/message/multicast'
contentType = 'application/json'
token = 'eeFlGCzjsOKFZ4YE0po8zdfGtwwKaehizZZpUeC8y/HWzQvzmL6A35+ciV8OVi5PcMIrEm+JPEgi6ouu2NZv/jvAHhe7frhE6993E93hWi8apLhBi0BzFyfHGhG7gNIzX9s6yqg+e9z9e8htRau/ywdB04t89/1O/w1cDnyilFU='
authorization = 'Bearer '+token


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
