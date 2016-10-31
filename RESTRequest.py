import requests
import json


class RESTRequest:
    # default request
    def __init__(self):
        pass

    json_map = {}
    json_map["projectId"] = 1101
    json_map["pools"] = "4"
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
    json_map["highPriority"] = False
    json_map["driverBranch"] = "r370_00"
    json_map["driverVersion"] = "372.90"
    json_map["doNotInstallDriver"] = False
    json_map["overrideDriver"] = True
    json_map["jobParameters"] = ""
    json_map["leverageFile"] = ""
    json_map["oldDB"] = False
    json_map["taskFolderIds"] = [88537]

    def toString(self):
        return json.dumps(self.json_map)
