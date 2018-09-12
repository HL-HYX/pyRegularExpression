#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# 导入re库文件

import re

secret_code = 'hadkfalifexxIxxfasdjifja134xxlovexx23345sdfxxyouxx8dfse'

# .的使用实列
a = 'abc123'
b = re.findall('a...', a)
print(b)

# *的使用举例
a = 'absabefa123'
b = re.findall('a*', a)
print(b)

# ?的使用举例
a = 'abcabe123'
b = re.findall('a?', a)
print(b)

# .*的使用举例
b = re.findall('xx.*xx', secret_code)
print(b)

# .*?的使用实例
c = re.findall('xx.*?xx', secret_code)
print(c)

# 使用括号进行操作
a = re.findall('xx(.*?)xx', secret_code)
print(a)
b = ''
for index in a:
    b += index + ' '
print(b)

# 对比findall与search的区别
a = 'abcI123defLoveade'
b = re.search('abc(.*?)123def(.*?)ade', a).group(2)
d = 'abcI123defLoveade'
f = re.findall('abc(.*?)123def(.*?)ade', a)
print(f[0][1])

# sub的使用实例

# 匹配数字('\d+')
a = 'sadewf1223214fsc12cf'
b = re.findall('\d+', a)
print(b)