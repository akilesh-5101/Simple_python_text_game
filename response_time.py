# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 16:36:31 2023

@author: Akilesh Venkat
"""
from gtts import gTTS
import random
import time
import sys
import pygame as pg
import pdb

pg.mixer.init()
n = 40
s_rate = 5
s = -0.3
Command = ["Duck", "Slip Right", "Slip Left", "Block", "Jab", "Straight", "Hook", "Uppercut", "Shake it"]


t = 2
# speech = gTTS(text = Command[4])
# speech.save('command5.mp3')
# speech = gTTS(text = Command[6])
# speech.save('command7.mp3')
# speech = gTTS(text = Command[6])
# speech.save('command7.mp3')
# speech = gTTS(text = Command[7])
# speech.save('command8.mp3')

# ACTUAL CODE:
for i in range(n):
    num = random.randint(0, 8)
    filename = 'command'+str(num+1) +'.mp3' 
    value = 'com'+ str(num+1)
    pg.mixer.music.load(filename)
    pg.mixer.music.play()
    s = s + (1/pow(s_rate, i))
    time.sleep(t - s)
    pg.mixer.music.stop()


    