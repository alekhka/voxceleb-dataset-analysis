#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 12:02:20 2017

@author: alekh
"""

import numpy as np
import librosa
import matplotlib.pyplot as mplt
import os
import time
import json

def get_audio_files(path, extension='wav'):
    speak_samples = {}
    samples_speak={}
    sams=[]
    for root, dirnames, filenames in os.walk(path):
        for dirname in dirnames:
            for root2, dirnames2, filenames2 in os.walk(path+dirname):
                speak_samples[dirname]=len(filenames2)
                samples_speak.setdefault(len(filenames2),[]).append(dirname)
                sams.append(len(filenames2))
    return speak_samples,samples_speak

speak_samples,samples_speak=get_audio_files('/media/alekh/01D1725AEE32E130/voxceleb/voxceleb1_wav/')
'''
with open('speak-samples.json', 'w') as fp:
    json.dump(speak_samples, fp, sort_keys=True, indent=4)

with open('samples-speak.json', 'w') as fp:
    json.dump(samples_speak, fp, sort_keys=True, indent=4)'''
