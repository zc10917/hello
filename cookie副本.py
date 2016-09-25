import requests
import re

data = {}
cookies = {}
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"}
header1 = {
    "Upgrade-Insecure-Requests":"1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36",
    "Referer": "http://git.sankuai.com/projects/ANDROID/repos/pay-demo/pull-requests?create&targetBranch=refs%2Fheads%2Foccc&sourceBranch=refs%2Fheads%2Fnew_occcc"}
with open("./cookie.text", "r") as f:
    for line in f.read().split(";"):
        pair = line.split("=", 1)
        if len(pair) == 2:
            cookies[pair[0]] = pair[1]

print(cookies)
with open("data", "r") as fdata:
    for line in fdata.read().split("\n"):
        pair = line.split(":", 1)
        if len(pair) == 2:
            data[pair[0]] = pair[1]
print(data)
url = "http://git.sankuai.com/projects/ANDROID/repos/pay-demo/pull-requests?create"

html = requests.get(url, headers=header, cookies=cookies)

str = str(html.content)
token = re.search("name=\"atl_token\" value=(.*?)>", str).group(1)
data["atl_token"] = token
print(token)
#

html = requests.post(url,data=data,cookies=cookies,headers = header1)

# html = requests.get("http://git.sankuai.com/projects/ANDROID/repos/pay-demo/pull-requests?create&targetBranch=refs%2Fheads%2Foccc&sourceBranch=refs%2Fheads%2Foccccccc",cookies = cookies)
#
#
#
print(html.content)
