import os
import json
def writeToFileLocal(filename,content):
    dirName="/".join(filename.split("/")[:-1])
    if not os.path.exists(dirName):
        os.makedirs(dirName)
    if type(content)==dict:
        content=json.dumps(content)
    with open(file=filename,mode="w+") as f:
        f.write(content)
