#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys,os,re
from CopyArticle import copyArticle

ID=long(sys.argv[0])
if not ID:
	sys.exit(1)

j=1
content='\xd6\xd0\xb9\xfa'
data=['r','r', '\n', content, '\x17','\n','b', '6', '\n', '\n' 'b','7','\n','\n']

for item in data:
	SendParsedString(ID, item)
print title+'\n'+content
