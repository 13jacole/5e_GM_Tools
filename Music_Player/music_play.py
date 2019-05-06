#!/usr/bin/env python

#imports
import os
import sys
import argparse
import glob
import random
from playsound import playsound

#Skeleton code
currDir = os.getcwd()
print("What playlist do you want to play?\n")
decision = input()
decision = decision.replace(" ", "_")
newDir = currDir + "\\" + decision
os.chdir(newDir)

print(os.getcwd())

mp3List = glob.glob1(newDir,"*.mp3")
mp3Counter = len(mp3List)

if mp3Counter > 1:
	x = random.randint(0, (mp3Counter-1))
elif mp3Counter == 1:
	x = 1
else:
	print("No MP3 files exist in this directory")
	sys.exit()
	
playsound(mp3List[x])