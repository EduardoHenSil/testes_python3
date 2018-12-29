#!/usr/bin/python3
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/postjson', methods=['POST'])
def post():
    print(request.is_json)
    content = request.get_json()
    print(content)
    print(content['id'])
    print(content['name'])
    return "JSON posted"

app.run(host='0.0.0.0', port=5000)
