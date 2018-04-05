from flask import Flask, request, jsonify, send_from_directory
import os
import requests
import json
import datetime
import mysql.connector


app = Flask(__name__, static_folder=".", template_folder=".")

cnx = mysql.connector.connect(user='root', database='tenderBartik', host='128.199.88.139', port='64556', password='ergweprjgwerighjwethjtr2315')
cursor = cnx.cursor()


@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization, data')
    return response


@app.route("/")
def home():
    return "KU LEAVE LINE SERVER"


 
if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80)
