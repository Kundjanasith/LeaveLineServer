from flask import Flask, request, jsonify, send_from_directory
import os
import requests
import json
import datetime
import pymysql
import pycurl
import json

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
    return "KU LEAVE LINE SUPERVISOR]"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=22211)

