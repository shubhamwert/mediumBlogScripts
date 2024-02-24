import Config.consts as consts
import json
import os
class ConfigLoader:
    def __init__(self,config):
        self._config={
            "saveToDir": "download/"
        }
        if type(config)==dict:
            self._config.update(config)
        if type(config)==str:
            self._config.update(self.loadFromPath(config))
        self.loadAPIKey()
    def get(self,key):
        return self._config[key]
    def getApiKey(self):
        return self.MEDIUM_API_KEY
    def loadFromPath(self,path: str):
        with open(path, mode='r') as f:
            return json.load(f)
    def loadAPIKey(self):
        self.MEDIUM_API_KEY=os.environ.get("MEDIUM_API_KEY",self._config.get("MEDIUM_API_KEY"))
    