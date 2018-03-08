#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 15:16:03 2017

@author: alekh
"""


import os
import pywikibot
import json

site = pywikibot.Site("en", "wikipedia") #Set to English Wikipedia
data=[] #To store names and countries
error=[] #To store failed cases

def get_audio_files(path, extension='wav'):
    files = []
    for root, dirnames, filenames in os.walk(path):
        for dirname in dirnames:
            files.append(dirname)
        return files

#Pass path where Voxceleb folders are there:
path='/media/alekh/01D1725AEE32E130/voxceleb/voxceleb1_wav/'
names=get_audio_files(path) #Gets all the directory names in the path. Directory names are the nmaes of people.
er=0 #Number of errors so far

for i,name in enumerate(names):
    page = pywikibot.Page(site, name) #Get the page for the name
    #Try except block because there can be errors:
    try:
        item = pywikibot.ItemPage.fromPage(page) #Get the object of all the property and values for the entity
        itdict=item.get() #Get the values as a dict
        p27=itdict['claims']['P27'][0].toJSON() #Convert the property P27 to JSON
        cntry=p27['mainsnak']['datavalue']['value']['numeric-id'] #Get country code from mainsnak>datavalue>value>numeric-ID
    except:
        #In case of error:
        er=er+1
        error.append(name)
        print "Error for: "+name
        continue
    
    print str(float(i)*100/1251 ) + "% done"
    
    #Append the vlaues into the dict
    data.append({"name":name, "country-code":cntry})

#Save it all to JSON files
with open('countries', 'w') as outfile:
		json.dump(data, outfile)

with open('errors', 'w') as outfile:
		json.dump(error, outfile)