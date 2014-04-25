#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys,os,re

ID=long(sys.argv[0])
if not ID:
	sys.exit(1)

j=1
content='\xc7\xeb\xb7\xa2\xb5\xbd \xb5\xe7\xc4\xd4\xca\xfd\xc2\xeb\xbd\xbb\xd2\xd7 \xb0\xe6'
data=['r','r', '\n', content, '\x17','\n','b', '6', '\n', '\n' 'b','7','\n','\n']

for item in data:
	SendParsedString(ID, item)
print title+'\n'+content
