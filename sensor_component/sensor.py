#!/usr/bin/env python
"""Sensor module.
"""

import json
import random
import uuid
import datetime
import time
import logging

import yaml
import requests

from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from requests.exceptions import HTTPError


class SensorDataPoint():
    """Class representing datapoint from sensor.
    """

    @classmethod
    def create_datapoint(cls, identifier, temperature_f):
        """Create json dump from input data.
        Arguments:
            temperature_f {float} -- Temperature in farenheits.
        Returns:
            string -- returns json containing datapoint information.
        """
        data = dict(
            type='Sensor',
            id=identifier,
            content=dict(
                temperature_f=temperature_f,
                time_of_measurement=datetime.datetime.now().isoformat()
            )
        )
        return json.dumps(data)


class Sensor():
    """Class representing sensor.
    """

    def __init__(self):
        self.identifier = str(uuid.uuid1())
        with open("sensor.yaml", 'r') as stream:
            self.config = yaml.safe_load(stream)

        # add retry logic
        self.session = requests.Session()
        retries = Retry(total=5, backoff_factor=1,
                        status_forcelist=[502, 503, 504])
        self.session.mount('http://', HTTPAdapter(max_retries=retries))


    def start(self):
        """Starts sensor sending data.
        """
        logging.info("Starting sendor with id: %s", self.identifier)
        while True:
            data = SensorDataPoint.create_datapoint(
                self.identifier, random.random()*100)
            url = self.config['api_target']['url']
            try:
                response = requests.post(url, json=data)
                response.raise_for_status()
            except HTTPError as http_error:
                msg = f'HTTP error occurred: {http_error}'
                logging.error(msg)
            except Exception as error:
                msg = f'Unexpected error occurred: {error}'
                logging.error(msg)
            time.sleep(10)


if __name__ == '__main__':
    sensor = Sensor()
    sensor.start()
