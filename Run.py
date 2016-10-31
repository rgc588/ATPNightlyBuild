from RESTRequest import RESTRequest
from ATPClient import ATPClient
from Log import Log
import sys

client = ATPClient()
request = RESTRequest()
Log.logger.info("Sending Request...")
client.send(request)

if client.response.status_code != 200:
    sys.exit(1)
else:
    sys.exit(0)
