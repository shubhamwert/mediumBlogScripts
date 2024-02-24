import requests 
def getFromUrl(url,**args) -> requests.Response:
    response=requests.get(url=url, **args)
    
    return response