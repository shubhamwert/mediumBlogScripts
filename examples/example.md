## Lets Introduce CI/CD in Medium Blogging

Medium is a bloging too. Usually writing to medium blog is done using an inbuild editor. inbuilt editor is really good and fulfills all needs for writing a blog.

But this method has few limitations

1. The written article is stored at medium only, so in case medium is down or not accessible, you will loose access to your article.
1. If you want to use some other blogging website like say dev.to, you would end-up writing the blog one more time.
1. You cannot choose your favourite editor to work with.

After researching , i found out medium exposes an api for interacting with your profile and blogs. [Medium API](https://github.com/Medium/medium-api-docs). But apprantely its now deprected and not supported. On writting of this article the api endpoint for pulling user profile, and uploading blog still worked

> We are using this api to download the blogs and push new blogs so if in future this stops working, the tool discussed in this blogs may also stop working

> I will try to update if this stops working

As software engineer the etch to implement CI/CD to writing my blogs in medium took over. So this blog discuses how i implemented CI/CD into how i write blogs.

![the project in nutshell](image.png)


## Problem

Lets breakdown problem into smaller parts
1. Download the blogs from medium.
1. Upload the blogs to medium

## Prerequistes
Before proceding you would require a integration token from medium website.
To download the token [settings -> security and apps -> integration token](https://medium.com/me/settings/security)

save it somewhere safe for later.

you can also save it as an env varibale, if you are on a unix based ooperating system you can save it as

```bash
export MEDIUN_API_KEY=<your-api-key>
```



# Download the blog
After researching i found out that medium do not allow downloading your blogs using api.

After exploring, I found 2 methods using which we can download blogs:
1. (RECOMMENDED) You can download your data from medium website. This is recommended method of downloading the your blogs. rest of article remains same once you have your data
    1. You can go to settings -> security and apps -> download your information to download youe information.

    ![alt text](image-1.png)
1. Second way is to use in-built scrapper to scrape your profile and downlod blogs. this has few limitations
    1. Image data is lost. When using this method you may loose the image data and may not recover 100% of blog.
    1. This method is dependent on the medium api to fetch and parse the blogs, if medium api is not supported anymore or deprecated, this will stop working
    1. You can only get publically published blogs.
    1. May contain noise
In next section we will discuss how we are downloading the blogs using medium api, please skip this section if you used recommended way.

## Download logic

We perform following steps:
1. Get user profile from medium api
1. fetch user-name from the response
1. using the username get users profile page with list of blogs
1. extract the links for all the blogs
1. for each blog, fetch the html page


So in nutshell, we use username to fetch the list of publically available blogs and then parse them using 2 libraries readability and markdown. the output is stored in destination you specify in config.

> Caution: in current version of application, you actually looses your images

# Converting To Markdown
Once blogs are downloaded using recommended way or using in-built scrapper, now we can convert our blog from html to markdown format

Steps will be
1. simplify and make it more readable using readability library
1. convert to markdown
1. save to specified folder along side metadata

For increasing readability we are using readabilit library
Lets discuss readability library in brief


### Readablity-lxml
The structure of html can be very complex with nested elements with no proper way of identyfing class id or div. This makes scraping a nightmare. if you are able to identify the required classes, it may change in future.
But in case of blogs which are primarly text, we dont want complete html or other components, we can just fetch the text. Only limitaion there is we loose the context of text. example on conversion to text after removeing attributes there is no difference between an hgeading or a simple line.
To resolve this we can convert the page to readability mode using algorithm. ( If you use firefox you may have seen similar button at left corner of your address bar).

You can checkout complete project at [Github](https://github.com/buriy/python-readability)

Once we have the html we can convert it to markdown. Now we only need to save the files

And Now you have all your blogs stored in the respective directory


## Using Downloader
To use inbuild downloaders, first you need to configure config.json
     ```json
     
     "saveToDir": path to save dir,
    ```

# Uploader
To upload the blogs, put your blof in a folder and provide path in the config.json

```json
"loadFromDir":"download/",

```
