import requests
import os
from Log import Log


class ATPClient:
    def __init__(self):
        self.log = Log.logger
        self.headers = {'content-type': 'application/json'}
        self.url = r"http://hqswqadb02/atp_api/api/tasks"
        if os.environ.get('HOST'):
            self.log.info("Using Server Host from Env...")
            self.url = os.environ.get('HOST') + r"/api/tasks"
            self.log.info("Server Path: " + self.url)
        self.response = None
        self.request = None

    def send(self, request):
        json_str = request.toString()
        self.log.info("Request Json: " + json_str)
        self.response = requests.post(url=self.url, json=json_str, headers=self.headers)
        self.request = self.response.request
        self.log.info("Status Code: " + str(self.response.status_code))
        self.log.info("Response: " + self.response.json())
