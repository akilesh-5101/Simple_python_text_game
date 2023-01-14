# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 16:36:31 2023

@author: Akilesh Venkat
"""
# from gtts import gTTS
import threading
import random
import time
import sys
import pygame as pg
import pdb

pg.mixer.init()
n = 30
game_end = False
test = 0
res_stop = 0
stop = True
difficulty = 1
Command = ["Duck", "Slip Right", "Slip Left", "Block", "Jab", "Straight", "Hooku", "Uppercut"]
y = None
dict={
    'com1': 's',
    'com2': 'd' ,
    'com3': 'a',
    'com4': 'w'
}
score = 0
def run():
    print(f"Time Up, GAME OVER: Score is {score}")
    game_end = True
    print("Press 'y' to continue or any character to exit")
    sys.exit()
    

    
    
# speech = gTTS(text = Command[4])
# speech.save('command5.mp3')
# speech = gTTS(text = Command[5])
# speech.save('command6.mp3')
# speech = gTTS(text = Command[6])
# speech.save('command7.mp3')
# speech = gTTS(text = Command[7])
# speech.save('command8.mp3')

# ACTUAL CODE:
for i in range(n):
    time.sleep(0.5)
    num = random.randint(0, 3)
    filename = 'command'+str(num+1) +'.mp3' 
    value = 'com'+ str(num+1)
    pg.mixer.music.load(filename)
    pg.mixer.music.play()

    time.sleep(1)
    pg.mixer.music.stop()

    t1 = threading.Timer(difficulty, run)
    t1.start()
    y = input()
    t1.cancel()
    if y == dict[value] and game_end == False:
        score = score+1
    elif y == 'y':
        print("New Start")
        score = 0

    elif game_end == False:
        print(f"GAME OVER: Score is {score}")
        sys.exit()
        


    