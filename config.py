import Config

def CreateNewConfig(pathToConfig: str="./config"):
    config=Config.models.ConfigLoader(pathToConfig)
    return config