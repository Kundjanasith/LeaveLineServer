from flask import Flask, request, jsonify, send_from_directory
import os
import requests
import json
import datetime
import pymysql

app = Flask(__name__, static_folder=".", template_folder=".")

conn = pymysql.connect(host='128.199.88.139', port=64566, user='root', passwd='ergweprjgwerighjwethjtr2315', db='tenderBartik')
cur = conn.cursor()

token = open("token.txt","r")
token = token.read()

@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization, data')
    return response


@app.route("/")
def home():
    return "KU LEAVE LINE SERVER [ADMINISTRATOR]"


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
        content = "\"NoAdministrator\""
    elif count == 1:
        content = "\""+str(count)+"Administrator\""
    else:
        content = "\'\"There are "+str(count)+" administrators\"\'"
    print(content)
    command = "bash list_administrator.sh "+uid+" \'"+content+"\' "+token
    os.system(command)
    '''
    counter = 0
    cur.execute(query)
    for i in cur:
        print(counter)
        counter = counter + 1
        text = ""
        text = str(counter) + ":" + i[0] + "" + i[1]
        print(text)
        os.system("bash list_administrator.sh "+uid+" "+text+" "+token)
        break
    '''
    return "LIST ADMINSTRATOR"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=22211)

