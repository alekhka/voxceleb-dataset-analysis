#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 15:16:03 2017

@author: alekh
"""

import numpy as np
import librosa
import matplotlib.pyplot as mplt
import os
import time
import json
def get_audio_files(path, extension='wav'):
	files = []
	for root, dirnames, filenames in os.walk(path):
		for filename in filenames:
			files.append(os.path.join(root, filename))
	return files

f="/media/alekh/01D1725AEE32E130/voxceleb/voxceleb1_wav/Aamir_Khan/5ablueV_1tw_0000001.wav"


y, sr = librosa.load(f)

start=time.clock()
flnms=get_audio_files('/media/alekh/01D1725AEE32E130/voxceleb/voxceleb1_wav/')
min=max=len(y)
lens=[]
data=[]
str2=time.clock()
for i,fn in enumerate(flnms):
    
    a, sr = librosa.load(fn)
    ln=len(a)
    if (ln<min):
        min=ln
        flmin=fn
    if (ln>max):
        max=ln
        flmax=fn
    data.append({"file":fn, "length":ln})
    
    if i%100==0:
        print i
        en1=time.clock()
        t = en1-str2
        print t
        print "ETA: " + str((153516-i)*t/100)
        str2=time.clock()

with open('lengths', 'w') as outfile:
		json.dump(data, outfile)
        
aud = np.array(y)

mplt.plot(aud)
end=time.clock()
print end-start