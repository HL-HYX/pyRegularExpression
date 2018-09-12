# #!/usr/bin/env python
# # _*_ coding:utf-8 _*_
# import requests
# import re
# # 获取网页源代码
# url = 'https://www.crowdfunder.com/'
# header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'}
#
# # 提取数据
# data = {'q': 'filter', 'page': '1'}
# a = requests.post(url, data=data, headers=header)
# Get_html = re.findall('<div class="card-title">(.*?)</div>', a.text, re.S)
# # print(Get_html)
# print('公司的名称:')
# for index in Get_html:
#     print(index)
#
