# Creates user and enables auth
from Config.consts import consts
import userMedium.userUtils as userUtils
import copy
from  bs4 import BeautifulSoup
class user:
    def __init__(self,config):
        self._profile=self.getUserProfile(config)
        r=self.getPublications(config)
        self.blogUrls=self.getAllBlogs(config)
    def getUserProfile(self,config):
        headers=copy.deepcopy(consts.DEFAULT_HEADERS)
        
        headers.update({
            "Authorization": f"Bearer {config.MEDIUM_API_KEY}",
            "Content-Type": "application/json",
        })

        response=userUtils.getFromUrl(f'{consts.MEDIUM_API_URL}{consts.MEDIUM_PATH["aboutMe"]}',headers=headers)
        if response.status_code not in range(400,600):
            response=response.json()
        
        assert response!=None, "Error while fetching profile, please check your api-keys"
        return response["data"]

    def getPublications(self,config):
        headers=copy.deepcopy(consts.DEFAULT_HEADERS)
        
        headers.update({
            "Authorization": f"Bearer {config.MEDIUM_API_KEY}",
            "Content-Type": "application/json",
        })
        response=userUtils.getFromUrl(f'{consts.MEDIUM_API_URL}{consts.MEDIUM_PATH["publications"].replace("USER_ID",self._profile["id"])}',headers=headers)
        if response.status_code not in range(400,600):
            response=response.json()
    
        assert response!=None, "Error while getting publicatons, please check your api-keys"
        return response["data"]
    def getAllBlogs(self,config):
        headers=copy.deepcopy(consts.DEFAULT_HEADERS)
        
        headers.update({
            "Content-Type": "application/json",
        })
        response=userUtils.getFromUrl(f'{consts.MEDIUM_BLOG_PATH}{self.getUserName()}',headers=headers)
        htmlLinks=self.parseBlogs(response.content)
        assert response!=None, "Error while getting blogs,"
        return htmlLinks
    def parseBlogs(self,response):
        # assert False, "Feature under work"
        urls=set()
        bsObject=BeautifulSoup(response,'lxml')
        for a in bsObject.find_all('a', href=True):
            if f'/@{self._profile["username"]}/' in a['href']:
                if ("/about?source=user_profile" not in a["href"]) and ("/followers?source=user_profile " not in a["href"]):

                    urls.add(a["href"].split("?")[0])
        return list(urls)
    def getUserName(self):
        return self._profile["username"]