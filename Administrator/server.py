from flask import Flask, request, jsonify, send_from_directory
import os
import requests
import json
import datetime
import pymysql
import pycurl
import json
import secrets
import string


app = Flask(__name__, static_folder=".", template_folder=".")

conn = pymysql.connect(host='128.199.88.139', port=64566, user='root', passwd='ergweprjgwerighjwethjtr2315', db='tenderBartik')
cur = conn.cursor()

token = open("token.txt","r")
token = token.read()

url = 'https://api.line.me/v2/bot/message/multicast'
contentType = 'application/json'
authorization = 'Bearer '+token[:-1]

@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization, data')
    return response


@app.route("/")
def home():
    return "KU LEAVE LINE SERVER [ADMINISTRATOR]"


@app.route("/administrator_otp")
def otp():
    query = 'SELECT * FROM lineUser'
    cur.execute(query)
    counter = 0
    p = gen_pass()
    for i in cur:
        print(i[1])
        if i[1] == p:
            counter = counter + 1
    if counter == 1:
        otp()
    else:
        return p

def gen_pass():
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(5))
    return password
    
@app.route("/administrator_verify/<string:uid>/<string:text>")
def verify(uid,text):
    conn = pymysql.connect(host='128.199.88.139', port=64566, user='root', passwd='ergweprjgwerighjwethjtr2315', db='tenderBartik')
    cur = conn.cursor()
    if len(text) == 5:
        query = 'SELECT * FROM lineUser where otp ="'+text+'" and role="Administrator"'
        cur.execute(query)
        counter = 0
        for i in cur: 
            counter = counter + 1
        temp = 'Invalid message'
        if counter != 0:
            temp = 'Register successfully'
        payload = {}
        payload['to'] = [uid]
        msg = {}
        msg['type'] = 'text'
        msg['text'] = temp
        payload['messages'] = [msg]
        print(payload)
        header = { 'content-type' : contentType, 'Authorization' : authorization }
        r = requests.post( url, data=json.dumps(payload), headers=header )
    else:
        payload = {}
        payload['to'] = [uid]
        msg = {}
        msg['type'] = 'text'
        msg['text'] = 'Invalid message'
        payload['messages'] = [msg]
        print(payload)
        header = { 'content-type' : contentType, 'Authorization' : authorization }
        r = requests.post( url, data=json.dumps(payload), headers=header ) 
    return "ADMINISTRATOR VERIFICATION"

@app.route("/list_administrator/<string:uid>")
def list_administrator(uid):
    query = ("SELECT fname, lname FROM users WHERE role ='"+"Administrator"+"'")
    cur.execute(query)
    count = 0
    for i in cur:
       print(i[0]+"   "+i[1])
       count = count + 1
    content = ""
    if count == 0:
        content = "There is no administrator\n"
    elif count == 1:
        content = "There is "+str(count)+" administrator\n"
    else:
        content = "There are "+str(count)+" administrators\n"
    count = 0
    cur.execute(query)
    for i in cur:
        count = count + 1
        content = content + str(count) +" : "+ i[0] + "  " +i[1]+"\n" 
    print(content)
    url = 'https://api.line.me/v2/bot/message/multicast'
    contentType = 'application/json'
    authorization = 'Bearer '+token[:-1]
    print(authorization)
    payload = {}
    payload['to'] = [uid]
    msg = {}
    msg['type'] = 'text'
    msg['text'] = content
    payload['messages'] = [msg]
    print(payload)
    header = { 'content-type' : contentType, 'Authorization' : authorization }
    r = requests.post( url, data=json.dumps(payload), headers=header )
    print(r)
    return "LIST ADMINSTRATOR"

@app.route("/list_supervisor/<string:uid>")
def list_supervisor(uid):
    query = ("SELECT fname, lname FROM users WHERE role ='"+"Supervisor"+"'")
    cur.execute(query)
    count = 0
    for i in cur:
       print(i[0]+"   "+i[1])
       count = count + 1
    content = ""
    if count == 0:
        content = "There is no supervisor\n"
    elif count == 1:
        content = "There is "+str(count)+" supervisor\n"
    else:
        content = "There are "+str(count)+" supervisors\n"
    count = 0
    cur.execute(query)
    for i in cur:
        count = count + 1
        content = content + str(count) +" : "+ i[0] + "  " +i[1]+"\n"  
    print(content)
    url = 'https://api.line.me/v2/bot/message/multicast'
    contentType = 'application/json'
    authorization = 'Bearer '+token[:-1]
    print(authorization)
    payload = {}
    payload['to'] = [uid]
    msg = {}
    msg['type'] = 'text'
    msg['text'] = content
    payload['messages'] = [msg]
    print(payload)
    header = { 'content-type' : contentType, 'Authorization' : authorization }
    r = requests.post( url, data=json.dumps(payload), headers=header )
    print(r)
    return "LIST SUPERVISOR"

@app.route("/list_subordinate/<string:uid>")
def list_subordinate(uid):
    query = ("SELECT fname, lname FROM users WHERE role ='"+"Subordinate"+"'")
    cur.execute(query)
    count = 0
    for i in cur:
       print(i[0]+"   "+i[1])
       count = count + 1
    content = ""
    if count == 0:
        content = "There is no subordinate\n"
    elif count == 1:
        content = "There is "+str(count)+" subordinate\n"
    else:
        content = "There are "+str(count)+" subordinates\n"
    count = 0
    cur.execute(query)
    for i in cur:
        count = count + 1
        content = content + str(count) +" : "+ i[0] + "  " +i[1]+"\n"  
    print(content)
    url = 'https://api.line.me/v2/bot/message/multicast'
    contentType = 'application/json'
    authorization = 'Bearer '+token[:-1]
    print(authorization)
    payload = {}
    payload['to'] = [uid]
    msg = {}
    msg['type'] = 'text'
    msg['text'] = content
    payload['messages'] = [msg]
    print(payload)
    header = { 'content-type' : contentType, 'Authorization' : authorization }
    r = requests.post( url, data=json.dumps(payload), headers=header )
    print(r)
    return "LIST SUBORDINATE"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=22211)

