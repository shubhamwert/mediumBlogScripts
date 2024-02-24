from DownloadBlog import models as downloadModel
import config
from Config.consts import consts
from userMedium import user as U
from UploadBlog import models as uploadModels

class createController:
    def __init__(self,conf, runners=1):
        self.user=U.user(conf)
        self.runners=runners
        self.downloadManager=[downloadModel.MediumBlogDownload(self.user.getUserName(),config=conf) for i in range(self.runners)]
        self.uploader=uploadModels.MediumBlogUpload(self.user.getUserName(),conf)

    def startDownloadBlog(self):
        for blogUrl in self.user.blogUrls:
            self.startDownloadSingleBlog(blogUrl)
        return
    def startDownloadSingleBlog(self,blogUrl):
        print(f"Getting {consts.MEDIUM_URL}{blogUrl}")
        self.downloadManager[0].processSingleUrl(url=f'{consts.MEDIUM_URL}{blogUrl}')

    def startUploadBlog(self,conf):

        self.uploader.processSingleBlog(userId=self.user._profile["id"],filePath=conf.get("loadFromDir"),conf=conf,title="Test",status="draft")


