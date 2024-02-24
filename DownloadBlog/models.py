from Config import consts
from Config import models as configModel
import requests
from readability import Document
from markdownify import markdownify as md
from DownloadBlog.downloadUtils import *

class MediumBlogDownload:
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
    def start(self, urls: list):
        for url in urls:
            print("Parsing: {url}")
            self.processSingleUrl(url)
    def processSingleUrl(self,url: str):
        status, content=self.downloadBlog(url)
        assert self.getUsername() in url, "Authentication Error, Please make sure you own the content and provide a valid api-token"

        if status not in [200,300]:
            print(f"Unable to process the {url} : response: {status}")
            return
        parsedContent,title=self.parseContent(content)
        writeToFileLocal(f"{self.config.get('saveToDir')}/{title}/README.md",parsedContent)
        metajson={
            "url": url,
            "id": url.split("-")[-1],
            "title":title,
            "publishStatus": "public"
        }
        writeToFileLocal(f"{self.config.get('saveToDir')}/{title}/meta.json",metajson)


    def downloadBlog(self,url) -> list[int,str]:
        assert self.getUsername() in url, "Authentication Error, Please make sure you own the content and provide a valid api-token"
        response=requests.get(url,headers=self.headers)
        if consts.consts.DEBUG:
            print(f"Process {url}: Response: {response}")
        return  response.status_code, response.text
    def parseContent(self,content: str):
        assert self.getUsername() in url, "Authentication Error, Please make sure you own the content and provide a valid api-token"

        d=Document(content)
        return md(d.summary()), d.title()
