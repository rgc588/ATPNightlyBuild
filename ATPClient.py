import requests
from Log import Log


class ATPClient:
    def __init__(self):
        self.log = Log.logger
        self.headers = {'content-type': 'application/json'}
        self.url = "http://hqswqadb02/atp_api/api/tasks"
        self.response = None
        self.request = None

    def send(self, request):
        json_str = request.toString()
        self.log.info("Request Json: " + json_str)
        self.response = requests.post(url=self.url, json=json_str, headers=self.headers)
        self.request = self.response.request
        self.log.info("Status Code: " + str(self.response.status_code))
        self.log.info("Response: " + self.response.json())
