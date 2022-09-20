#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 13:22:46 2022

@author: craigrupp
"""

## Requests in Python (Import Library)

## https://requests.readthedocs.io/en/latest/?utm_content=000026UJ&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0101ENSkillsNetwork19487395-2022-01-01&utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_term=10006555

# Requests is a Python Library that allows you to send <code>HTTP/1.1</code> requests easily. We can import the library as follows:
import requests

import os 
from PIL import Image
import datetime

# You can make a GET request via the method get to www.ibm.com:
url='https://www.ibm.com/'
r=requests.get(url)

print(type(r))
print(r)
print([r.status_code, r.apparent_encoding, r.reason])

# Request Headers
print(r.request.headers)

# Response headers
print(r.headers)

# Request Body
print(r.request.body)

# Let's see some more response headers
print([r.headers['Content-Type'], r.headers['Content-Length']])

print(r.text[0:100], len(r.text))


# =============================================================================
# You can load other types of data for non-text requests, like images. Consider the URL of the following image:
# 
# =============================================================================
# Use single quotation marks for defining string
url_two='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png'

resp_obj = requests.get(url_two)
print(resp_obj.status_code, resp_obj.headers['Content-Type'])

# Note the Content for the Response Headers gives us a good idea of what we're working with

# An image is a response object that contains the image as a bytes-like object. 
# As a result, we must save it using a file object. First, we specify the file path and name
path=os.path.join(os.getcwd(),'image.png')
path


# We save the file, in order to access the body of the response we use the attribute <code>content</code> then save it using the <code>open</code> function and write <code>method</code>:
with open(path,'wb') as f:
    f.write(resp_obj.content)

Image.open(path)



# =============================================================================
# # Exercises
# =============================================================================

# In the previous section, we used the wget function to retrieve content from the web server as shown below. 
# Write the python code to perform the same task. The code should be the same as the one used to download the image, but the file name should be 'Example1.txt'.

# Set Url
url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt'
#  Specify file path (getcwd), and give name to image
path=os.path.join(os.getcwd(),'example1.txt')
# Get Content
r=requests.get(url)
# Create File Object
with open(path,'wb') as f:
    f.write(r.content)

# Append Time stamp to file and delete line without \n 
with open(path, 'r+') as r_file:
    escaped_lines = r_file.readlines()
    cur_time = datetime.datetime.now()
    cur_time_str = cur_time.strftime("%m-%d-%Y %H:%M:%S")
    fmt_time_str = f"Today's date and time : {cur_time_str}\n"
    r_file.seek(0,0) # Write to Beginning of File
    # Write escaped lines and not lines without
    [r_file.write(x) for x in escaped_lines if x.count('\n') == 1]
    r_file.write(fmt_time_str)
    r_file.truncate()# Delete Anything that follows (not important here but good practice once you're done reading & writing)
   
    
# Check File
with open(path, 'r') as r_check_file:
    print(r_check_file.readlines())


print(datetime.datetime.now(), type(datetime.datetime.now()))


## Request w/URL Parameters

# The Base URL is for http://httpbin.org/ is a simple HTTP Request & Response Service. The URL in Python is given by:
url_get='http://httpbin.org/get'

# To create a Query string, add a dictionary. The keys are the parameter names and the values are the value of the Query string.
payload={"name":"Joseph","ID":"123"}

# Then passing the dictionary payload to the params parameter of the  get() function:
resp_httpbn = requests.get(url_get, params=payload)

# print our received request headers
print(resp_httpbn.request.headers)
print(resp_httpbn.request.path_url, resp_httpbn.request.method, resp_httpbn.request.copy())
# Another way to see args (more clean)
print(resp_httpbn.json()['args'])


## Post Request

# Like a GET request, a POST is used to send data to a server, but the POST request sends the data in a request body. 
# In order to send the Post Request in Python, in the URL we change the route to POST:
url_post='http://httpbin.org/post'

# =============================================================================
# This endpoint will expect data as a file or as a form. A form is convenient way to configure an HTTP request to send data to a server.
# To make a POST request we use the post() function, the variable payload is passed to the parameter  data :
# =============================================================================
r_post=requests.post(url_post,data=payload)


# Comparing the URL from the response object of the <code>GET</code> and <code>POST</code> request we see the <code>POST</code> request has no name or value pairs.
print("POST request URL:",r_post.url )
print("GET request URL:",resp_httpbn.url)


# We can compare the POST and GET request body, we see only the POST request has a body:
print("POST request body:",r_post.request.body)
print("GET request body:",resp_httpbn.request.body)

# We can view the form as well:
r_post.json()['form']





