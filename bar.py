#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 18:13:03 2017

@author: alekh
"""

import matplotlib.pyplot as plt
from collections import Counter
import json

with open('countries.json') as data_file:    
    cntrs = json.load(data_file)

c=[]

for d in cntrs:
    c.append(d['country-code'])


def autolabelt(rects):
    """
    For the TOP PLOT
    Attach a text label above each bar displaying its height
    """
    for i,rect in enumerate(rects):
        if i>0:
            break
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2, 1*height+0.5,'%d' % int(height),ha='center', va='bottom')
        
def autolabelb(rects):
    """
    For the BOTTOM PLOT
    Attach a text label above each bar displaying its height
    """
    for i,rect in enumerate(rects):
        if i==0:
            continue
        height = rect.get_height()
        ax2.text(rect.get_x() + rect.get_width()/2, 1.02*height+5,'%d' % int(height),ha='center', va='bottom',rotation='vertical')

cnt=dict(Counter(c))
clist=cnt.values()
clist.sort(reverse=True)
cold=clist[:]

#isle
clist.remove(209)
clist.insert(1,210)
clist.remove(1)
#germany
clist.remove(8)
clist.insert(7,9)
clist.remove(1)
#russia
clist.remove(2)
clist.insert(16,4)
clist.remove(2)
#ireland
clist.remove(15)
clist.insert(6,16)
clist.remove(1)

clist.sort(reverse=True)

cnames=['USA','UK','Canada','Australia','India','Norway','Ireland','Germany','Italy','New Zealand','Mexico','Sweden','Russia','Spain','Denmark','Chile','Netherlands','Poland','Switzerland','Portugal',
        'Austria','China','Brazil','Croatia','South Africa','Singapore','Trinidad & Tobago','Iran','Israel','Pakistan','Sri Lanka','Philippines','Sudan']
font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 6}

#Make dict of conutry counts
ctry_count={}
for i,num in enumerate(clist):
    ctry_count[cnames[i]]=num

#Correcting for the errors
ctry_count['USA']=ctry_count['USA']+35
ctry_count['Ireland']=ctry_count['Ireland']+2
ctry_count['India']=ctry_count['India']+3
ctry_count['Canada']=ctry_count['Canada']+1
ctry_count['Mexico']=ctry_count['Mexico']+2
ctry_count['UK']=ctry_count['UK']+5
ctry_count['Croatia']=ctry_count['Croatia']+2
ctry_count['Philippines']=ctry_count['Philippines']+2
ctry_count['Switzerland']=ctry_count['Switzerland']+1
ctry_count['Spain']=ctry_count['Spain']+1
ctry_count['France']=1
ctry_count['Sweden']=ctry_count['Sweden']+1
ctry_count['Australia']=ctry_count['Australia']+2
ctry_count['Guyana']=1
ctry_count['South Korea']=1
ctry_count['China']=ctry_count['China']+1


cnames=ctry_count.keys()
values=ctry_count.values()
combined = zip(values, cnames)
combined.sort(reverse=True)
clist[:], cnames[:] = zip(*combined)

xaxs = [i for i in range(len(clist))]
plt.figure()
plt.rc('font', **font)
f, (ax, ax2) = plt.subplots(2, 1, sharex=True, gridspec_kw = {'height_ratios':[1, 5]})
b1=ax.bar(xaxs,clist,0.7)
b2=ax2.bar(xaxs,clist,0.7)
ax.set_ylim(790, 805) 
ax2.set_ylim(0, 250) 
ax.spines['bottom'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax.xaxis.tick_top()
ax.tick_params(labeltop='off')  # don't put tick labels at the top
ax2.xaxis.tick_bottom()
d = .015  # how big to make the diagonal lines in axes coordinates
# arguments to pass to plot, just so we don't keep repeating them
kwargs = dict(transform=ax.transAxes, color='k', clip_on=False)
ax.plot((-d, +d), (-4*d, +4*d), **kwargs)        # top-left diagonal
ax.plot((1 - d, 1 + d), (-4*d, +4*d), **kwargs)  # top-right diagonal
autolabelt(b1)
autolabelb(b2)
kwargs.update(transform=ax2.transAxes)  # switch to the bottom axes
ax2.plot((-d, +d), (1 - d, 1 + d), **kwargs)  # bottom-left diagonal
ax2.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)
plt.xticks(xaxs, cnames, rotation='vertical')
plt.ylabel('Number of speakers')
plt.savefig('country.png', format='png', dpi=1000, bbox_inches='tight')