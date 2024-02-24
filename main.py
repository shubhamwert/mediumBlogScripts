import config
import controller as C
import sys
import caution
MENU_ITEMS="""
1). Run Downloader for all blogs
2). Run Downloader for single blog
3). Run Uploader
4). Help
5). Exit
"""
if __name__=='__main__':
    caution.Caution()
    conf=config.CreateNewConfig("config.json")
    con=C.createController(conf)
    print(5*"\n","Opening the Menu")
    print(10*"#")
    print(MENU_ITEMS)
    print(10*"#")
    op=input("Please Select an option : ")
    if op=="1":
        con.startDownloadBlog()
    if op=="2":
        print("Currently available blogs")
        for i,v in enumerate(con.user.blogUrls):
            print(i,v,sep="->")
        i=int(input("Choose one of the blogs : "))
        con.startDownloadSingleBlog(con.user.blogUrls[i])
    if op=="5":
        sys.exit()
    if op=="4":
        print("For full usage checkout /examples/example.md")
    if op=="3":
        con.startUploadBlog(conf)