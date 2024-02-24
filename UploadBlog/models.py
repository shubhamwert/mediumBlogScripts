from Config import consts
from Config import models as configModel
import requests
from UploadBlog.uploadUtils import *
import copy
class MediumBlogUpload:
    def __init__(self,username: str, config: configModel.ConfigLoader,headers: str=None):
        assert (username!=type(str)), "Username must be a string "
        assert (username!=""), "Username cannot be empty "


        if headers==None:
            self.headers = consts.consts.DEFAULT_HEADERS
        else:
            self.headers=headers

        self.config=config
        self.username=username

    def getConfigVal(self,key: str):
        return self.config.get(key)
    
    def getUsername(self):
        return self.username
    
    def processSingleBlog(self,userId: str,filePath: str,conf,title,tags: list[str]=[],status:str="draft"):
        data=loadFromPath(filePath)
        data={
        "title": title,
        "contentFormat": 'markdown' if filePath.split(".")[-1]=='md' else 'html',
        "content": data,
        "tags": tags,
        "publishStatus":status
        }
        r=self.postBlog(data,conf,userId)
        print(r.text)
        assert r.status_code in range(200,300), "Unable to post blog, make sure you have access to publish, Error: "+str(r.status_code)
        writeToFileLocal(filename="/".join(filePath.split("/")[:-1])+"/meta.json",content=r.json())
        
    def postBlog(self,data,config,userId):
        headers=copy.deepcopy(consts.consts.DEFAULT_HEADERS)
        
        headers.update({
            "Authorization": f"Bearer {config.MEDIUM_API_KEY}",
            "Content-Type": "application/json",
        })
        formattedUrl=f'{consts.consts.MEDIUM_API_URL}{consts.consts.MEDIUM_PATH["posts"].replace("USER_ID",userId)}'
        print(formattedUrl)
        response=requests.post(url=formattedUrl,headers=headers,data=json.dumps(data))
        
        return response


    
