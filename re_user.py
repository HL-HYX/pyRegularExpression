# #!/usr/bin/env python
# # _*_ coding:utf-8 _
# import re
# import requests
# # 获取文本内容
# f = open('source.txt', 'rb')
# html = f.read()
# f.close()
# # print(html)
# html = html.decode('utf-8')  # python3
# # 图片下载
# pic_url = re.findall('img src="(.*?)" class="lessonimg"', html, re.S)
# i = 0
# for each in pic_url:
#     print('now downloading:' + each)
#     pic = requests.get(each)
#     fp = open('pic\\%s.jpg'%str(i), 'wb+')
#     fp.write(pic.content)
#     fp.close()
#     i += 1
