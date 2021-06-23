'''
1. request module is used to get,post etc on internet. While working on internet if we want to get the content of a URL
or post some content on a specific URl etc we need to use this inbuilt request module of python
2. post request - post requests should have one API end point and we need to send some data with such requests
3. data that we send in post requests are always in the form of a dictionary
4. It is not am inbuilt module

'''
import requests

# how to get  the content from a particular from a particular URL
r= requests.get("https://docs.python-requests.org/en/master/")
print(r.text) # this will give out the HTML content of a website in the text format


# how to post a content on a particular URL
url = "https://docs.python-requests.org/en/master/"
data = {
    "p1": 30,
"p2": 40
}
r2 = requests.post(url=url,data=data)

# Doubt : There was a task given in this video which I did not understand