#!/usr/bin/env python

import json
from datetime import datetime

import paho.mqtt.client as mqtt

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import BaseConfig as config
from models import DataPoint

session = None

def on_message(client, userdata, msg):
    """Mock on_message method.

    Arguments:
        client {[type]} -- [description]
        userdata {[type]} -- [description]
        msg {[type]} -- [description]
    """
    client = client
    userdata = userdata
    data = json.loads(msg.payload.decode())
    data_point = DataPoint(
        identifier=data['id'],
        date=datetime.fromisoformat(data['content']['time_of_measurement']),
        temperature_f=data['content']['temperature_f'],
        temperature_c=data['content']['temperature_c'],
        type=data['type']
    )
    session.add(data_point)
    session.commit()


class Storage(object):
    """Class representing storage component.
    """
    def __init__(self):
        uri = config.SQLALCHEMY_DATABASE_URI
        engine = create_engine(uri)
        Session = sessionmaker(bind=engine)
        global session
        session = Session()
        self.client = mqtt.Client()
        self.client.connect(config.BROKER, config.PORT, config.TIMELIVE)
        self.client.subscribe("/data")
        self.client.on_message = on_message

    def start(self):
        self.client.loop_forever()

if __name__ == '__main__':
    storage = Storage()
    storage.start()
