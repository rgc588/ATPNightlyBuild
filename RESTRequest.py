import requests
import json


class RESTRequest:
    # default request
    def __init__(self):
        pass

    json_map = {}
    json_map["projectId"] = 1120
    json_map["pools"] = [4]
    json_map["skipSku"] = False
    json_map["skipPNumber"] = False
    json_map["skipPlatform"] = False
    json_map["forceDisableSLI"] = False
    json_map["useTOT"] = False
    json_map["winNext"] = False
    json_map["sandbag"] = True
    json_map["codeCoverage"] = False
    json_map["verifier"] = False
    json_map["oemId"] = 0
    json_map["highPriority"] = True
    json_map["driverVersion"] = "378.08"
    json_map["doNotInstallDriver"] = False
    json_map["overrideDriver"] = True
    json_map["jobParameters"] = ""
    json_map["leverageFile"] = ""
    json_map["oldDB"] = False
    json_map["taskFolderIds"] = [114014]
    json_map["customDriverPath"] = r"\\builds\NightlyRestricted-bugfix_main\NV\wddm2-x64\bugfix_main-161031-21317638-sandbag\IS"

    def toString(self):
        return json.dumps(self.json_map)

    def setDriverPath(self, path):
        self.json_map["customDriverPath"] = path

    def setProjectId(self, projectId):
        self.json_map["projectId"] = int(projectId)

    def setPools(self, poolIds):
        ids = [int(i) for i in str(poolIds).split(',')]
        self.json_map["pools"] = ids

    def setFolderId(self, folderIds):
        ids = [int(i) for i in str(folderIds).split(',')]
        self.json_map["taskFolderIds"] = ids
