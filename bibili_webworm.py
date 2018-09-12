#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import re
import requests

# url = 'https://www.bilibili.com/'
# # f = open('bibili.txt', 'rb')
# # html = f.read()
# # f.close()
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'}
# # print(html.text)
# # html = html.decode('utf-8')  # python3
a = requests.get('https://www.bilibili.com/video/av28630432/', headers=header)
# html_bili = re.findall('<p class="dm">(.*?)</p>', a.text, re.S)
f = open('pic\\0.wmv', 'wb')
f.write(a.content)
f.close()
