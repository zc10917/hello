# coding=utf-8
# author:walker
# date:2013-11-21

from selenium import webdriver
import time
import requests

b = webdriver.Firefox()
# b = webdriver.Ie()
b.delete_all_cookies()
cookies = {}
while True:
    list_cookies = b.get_cookies()  # 这里返回的是一个更多信息的字典列表
    print(list_cookies)
    for s in list_cookies:
        cookies[s['name']] = s['value']
    print(cookies)
    if cookies.has_key('BAIDUID'):
        b.close()
        break
    time.sleep(2)

sn = requests.Session()
requests.utils.add_dict_to_cookiejar(sn.cookies, cookies)
# 或者
requests.get(url, cookies=cookies)