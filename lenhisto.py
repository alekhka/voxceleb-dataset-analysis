#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 02:10:19 2017

@author: alekh
"""
import json
from collections import Counter
import matplotlib.pyplot as plt
with open('lengths.json') as data_file:    
    lengths = json.load(data_file)
    
l=[]
dicti = {}
dicti2={}
for lens in lengths:
    l.append(lens['length'])
    dicti[lens['file'][53:]]=lens['length']
    dicti2.setdefault(lens['length'],[]).append(lens['file'][53:])

with open('file-len.json', 'w') as fp:
    json.dump(dicti, fp, sort_keys=True, indent=4)
with open('len-files.json', 'w') as fp:
    json.dump(dicti2, fp, sort_keys=True, indent=4)
'''
cnt=Counter(l)
cnt=dict(Counter(l))
c=cnt.values()
c.sort(reverse=True)
xaxs = [i for i in range(1155)]
labels=[i for i in range(87320,3195489,518028)]
xaxs2=[i*0.1 for i in range(0,11551,1925)]
plt.figure()
plt.bar(xaxs,c)
plt.xlabel('Length')
plt.ylabel('Count')
#plt.xlim(87000, 3195500)
plt.xticks(xaxs2, labels, rotation='vertical')
plt.savefig('lengthhisto.png', format='png', dpi=1000, bbox_inches='tight')'''