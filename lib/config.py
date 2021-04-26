import json


class Config:

    def __init__(self, path):
        self.path = path
        configFile = open(self.path, "r")
        self.data = json.loads(configFile.read())

    def getConfig(self):
        return self.data

    def get(self, key):
        return self.data[key]
