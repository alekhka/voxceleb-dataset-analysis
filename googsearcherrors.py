#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 10:57:20 2017

@author: alekh
"""
import json
import webbrowser
new=2
maxTabs=30

with open('errors.json') as data_file:
    err = json.load(data_file)


for i,name in enumerate(err):
    query=name.replace("_"," ")
    goog="http://www.google.com/search?q="
    url = goog+query

    #webbrowser.get(using='google-chrome').open(url,new=new)
    if (i+1)%maxTabs==0:

        raw_input("Press Enter to continue...")
