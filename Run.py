from RESTRequest import RESTRequest
from ATPClient import ATPClient
from Log import Log
import sys
import os

client = ATPClient()
request = RESTRequest()

# read parameter from Env
if os.environ.get("DRIVER_PATH"):
    request.setDriverPath(os.environ.get("DRIVER_PATH"))
else:
    Log.logger.error("DRIVER_PATH is required")
    sys.exit(1)

if os.environ.get("PROJECT_ID"):
    request.setProjectId(os.environ.get("PROJECT_ID"))
else:
    Log.logger.error("PROJECT_ID is required")
    sys.exit(1)

if os.environ.get("FOLDER_ID"):
    request.setFolderId(os.environ.get("FOLDER_ID"))
else:
    Log.logger.error("FOLDER_ID is required")
    sys.exit(1)

if os.environ.get("POOLS"):
    request.setPools(os.environ.get("POOLS"))
else:
    Log.logger.error("POOLS is required")
    sys.exit(1)

Log.logger.info("Sending Request...")
client.send(request)

if client.response.status_code == 200:
    Log.logger.info("Task scheduled successfully")
    sys.exit(0)
else:
    Log.logger.info("Failed to schedule task")
    if client.response.status_code == 417:
        Log.logger.error("Status code 417")
    sys.exit(1)
