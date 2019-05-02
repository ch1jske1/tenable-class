import requests

url = "https://swapi.co/api/people/1/"

payload = ""
headers = {
    'User-Agent': "PostmanRuntime/7.11.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "09d72a07-24c5-4a69-b3df-9e537737690e,f42105b2-69e1-45fe-bb60-1284b795e912",
    'Host': "swapi.co",
    'cookie': "__cfduid=d764210db620b21e3f9377777e5d427111556814057",
    'accept-encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, data=payload, headers=headers)

print(response.text)

