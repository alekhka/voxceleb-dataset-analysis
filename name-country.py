#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 18:45:00 2017

@author: alekh
"""
import json

with open('countries.json') as data_file:    
    cn = json.load(data_file)

cntrs={}

for c in cn:
    cntrs[c['name']]=c['country-code']
    
codes={30:'USA',145:'UK',16:'Canada',408:'Australia',668:'India',142:'Norway',27:'Ireland',183:'Germany',38:'Italy',664:'New Zealand',96:'Mexico',34:'Sweden',159:'Russia',29:'Spain',35:'Denmark',298:'Chile',29999:'Netherlands',36:'Poland',39:'Switzerland',45:'Portugal',
        40:'Austria',148:'China',155:'Brazil',224:'Croatia',258:'South Africa',334:'Singapore',754:'Trinidad and Tobago',794:'Iran',801:'Israel',843:'Pakistan',854:'Sri Lanka',928:'Philippines',1049:'Sudan',26:'Ireland',9676:'UK',15180:'Russia',16957:'Germany'}
for c in cn:
    cntrs[c['name']]=codes[c['country-code']]
with open('name-country.json', 'w') as fp:
    json.dump(cntrs, fp, sort_keys=True, indent=4)