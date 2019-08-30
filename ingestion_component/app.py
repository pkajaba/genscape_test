#!/usr/bin/env python
import flask
import json
from flask import Flask, request
import paho.mqtt.client as paho

# config 
app = Flask(__name__)

BROKER = "mqtt"
PORT = 1883
CLIENT = paho.Client("admin")
CLIENT.connect(BROKER, PORT)

@app.route('/', methods=['POST'])
def datapoints():
    data = json.loads(request.json)
    data['content']['temperature_c'] = (data['content']['temperature_f'] - 32) * 5/9
    ret = CLIENT.publish("/data", json.dumps(data))
    return data

if __name__ == '__main__':
    app.run(host="0.0.0.0")
