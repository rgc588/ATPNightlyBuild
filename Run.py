from RESTRequest import RESTRequest
from ATPClient import ATPClient
from Log import Log
import sys

client = ATPClient()
request = RESTRequest()
Log.logger.info("Sending Request...")
client.send(request)

if client.response.status_code == 200:
    Log.logger.info("Task scheduled successfully")
    sys.exit(0)
else:
    Log.logger.info("Failed to schedule task")
    if client.response.status_code == 417:
        Log.logger.info("Status code 417")
    sys.exit(1)
