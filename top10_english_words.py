# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 2:23:50 2017

@author: satyam
"""
import operator

file = open('counts','r')
d = {}
for line in file:
	x = line.split('\t')
	a = x[0]
	b = x[1]
	c = len(b)-1
	b = b[:c]
	d[a] = b


newd = dict(sorted(d.items(), key=lambda x: int(x[1]), reverse=True)[:10])
print(newd)
