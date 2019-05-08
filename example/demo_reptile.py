#!/usr/bin/env python3

import requests
import re

response = requests.get('https://book.douban.com/subject/30459864/?icn=index-latestbook-subject')

print(response)

result = response.text
title = re.findall(r'<title>(.*?)</title>', result)
text = re.findall(r'<div id="content">([\s\s]*?)</div>', result)

print(title)
print(text)
