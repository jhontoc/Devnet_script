import requests
import json


"""
get testing
url = 'https://postman-echo.com/get'
querystring={"test":123}
headers={}
response = requests.request("GET",url,headers=headers,params=querystring)
print(response.text)

"""
"""
post example
url='https://postman-echo.com/post'
payload="hello jhony"
headers={'content-type':'text/plain'}
response=requests.request("POST",url,headers=headers,data=payload)
print(response.text)
"""
#get with basic authentication

url='http://postman-echo.com/basic-auth'
headers = {
    'authorization': 'Basic cG9zdG1hbjpwYXNzd29yZA=='
}
response=requests.request("GET",url,headers=headers)
print(response.text)