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
    return "KU LEAVE LINE SERVER [SUBORDINATE]"


@app.route("/subordinate_otp")
def otp():
    conn = pymysql.connect(host='128.199.88.139', port=64566, user='root', passwd='ergweprjgwerighjwethjtr2315', db='tenderBartik')
    cur = conn.cursor()
    query = 'SELECT * FROM lineUser'
    cur.execute(query)
    counter = 0
    p = gen_pass()
    for i in cur:
        #print(i[1])
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
    
@app.route("/subordinate_verify/<string:uid>/<string:text>")
def verify(uid,text):
    conn = pymysql.connect(host='128.199.88.139', port=64566, user='root', passwd='ergweprjgwerighjwethjtr2315', db='tenderBartik')
    cur = conn.cursor()
    if len(text) == 5:
        query = 'SELECT * FROM lineUser where otp ="'+text+'" and role="Subordinate"'
        b = cur.execute(query)
        print(b)
        counter = 0
        for i in cur: 
            counter = counter + 1
        temp = 'Invalid message'
        if counter != 0:
            conn = pymysql.connect(host='128.199.88.139', port=64566, user='root', passwd='ergweprjgwerighjwethjtr2315', db='tenderBartik', autocommit=True)
            cur = conn.cursor()
            query = 'UPDATE lineUser SET line_id="'+uid+'" WHERE otp="'+text+'" AND role="Subordinate"'
            a = cur.execute(query)
            print(a)
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
        header = { 'content-type' : contentType, 'Authorization' : authorization }
        r = requests.post( url, data=json.dumps(payload), headers=header ) 
    return "SUBORDINATE VERIFICATION"

@app.route("/list_tasks/<string:uid>")
def tasks(uid):
    conn = pymysql.connect(host='128.199.88.139', port=64566, user='root', passwd='ergweprjgwerighjwethjtr2315', db='tenderBartik')
    cur = conn.cursor()
    query = 'SELECT * FROM lineTask WHERE subordinate=(SELECT id FROM lineUser WHERE line_id="'+uid+'" AND role="Subordinate")'
    cur.execute(query)
    content = ""
    allTasks = []
    for i in cur:
       allTasks.append(i)
    if len(allTasks) == 0:
       content = content + "There is no tasks\n"
    elif len(allTasks) == 1:
       content = content + "There is 1 task\n"
    else:
       content = content + "There are "+str(len(allTasks))+" tasks\n"
    counterT = 0
    for j in allTasks:
       counterT = counterT + 1
       content = content + " - Task name : \n\t"+ j[3] + "\n"
       content = content + " - Start date : \n\t"+ j[4] + "\n"
       content = content + " - End date : \n\t"+ j[5] + "\n"
    payload = {}
    payload['to'] = [uid]
    msg = {}
    msg['type'] = 'text'
    msg['text'] = content[:-1]
    payload['messages'] = [msg]
    header = { 'content-type' : contentType, 'Authorization' : authorization }
    r = requests.post( url, data=json.dumps(payload), headers=header ) 
    return "LIST TASKS"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=22213)

