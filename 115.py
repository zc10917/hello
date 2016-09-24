import requests
import time
cookies={}
data = {}
with open("cookie", "r") as f:
    for line in f.read().split(";"):
        pair = line.split("=", 1)
        if len(pair) == 2:
            cookies[pair[0]] = pair[1]

with open("data", "r") as fdata:
    for line in fdata.read().split("\n"):
        pair = line.split(":", 1)
        if len(pair) == 2:

            data[pair[0]] = pair[1]
print(cookies)


html = requests.get('http://115.com/?tab=offline&mode=wangpan', cookies = cookies)

print(html.content)
print(int(time.time()))

cookies[3] = int(time.time())