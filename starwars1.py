import http.client

conn = http.client.HTTPConnection("swapi,co")

payload = ""

headers = {
    'User-Agent': "PostmanRuntime/7.11.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "09d72a07-24c5-4a69-b3df-9e537737690e,e84bf914-c574-4f8d-b6fa-816452f0253e",
    'Host': "swapi.co",
    'cookie': "__cfduid=d764210db620b21e3f9377777e5d427111556814057",
    'accept-encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

conn.request("GET", "api,people,1,", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
