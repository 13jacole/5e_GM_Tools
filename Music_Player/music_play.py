#!/usr/bin/env python

#imports
import os
import sys
import argparse
import glob
import random as rando
from playsound import playsound

"""
music_play.py: Music Player
       Usage: python music_play.py 
"""

# meta information
__author__ = "Jakob Cole"
__maintainer__ = "Jakob Cole"

#arguments
pa = argparse.ArgumentParser()
pa.add_argument('-l', '--loop', action='store_true',
				help='Flag specifies if music should loop')
				
pa.add_argument('-r', '--random', action='store_true',
				help='Flag specifies whether music will be randomized or not')

pa.add_argument('-p', '--playlist', action='store_true',
				help='Flag specifies whether music will be playlist or song')

args = pa.parse_args()	

#argument parsing
if args.loop:
	loop = True
else:
	loop = False
	
if args.random:
	random = True
else:
	random = False
	
if args.playlist:
	playlist = True
else:
	playlist = False

#skeleton code

currDir = os.getcwd()

if playlist:
	print("What playlist do you want to play?\n")
	print("Please type the name of the subdirectory: \n")
else:
	print("From what playlist do you want to select your song?\n")
	print("Please type the name of the subdirectory: \n")
	
decision = input()
decision = decision.replace(" ", "_")
newDir = currDir + "\\" + decision

print(os.getcwd())

os.chdir(newDir)

mp3List = glob.glob1(newDir,"*.mp3")
mp3Counter = len(mp3List)

if playlist:
	if mp3Counter > 1:
		if random:
			rando.shuffle(mp3List)
		else:
			x = 0
	elif mp3Counter == 1:
		x = 0
	else:
		print("No MP3 files exist in this directory")
		sys.exit()
	if random:
		for each song in mp3List:
			y = True
			while y:
				playsound(mp3List[song])
				y = loop
	else:
		y = True
		while y:
			playsound(mp3List[x])
			y = loop
else:
	if random:
		x = rando.randInt(0, mp3Counter)
	else:
		print("\n")
		print("Songs in this directory:")
		print("\n")
		for idx, song in enumerate(mp3List, start=1):
			print("{}: {}\n".format(idx, song))
		print("Please indicate what song you would like to play\n[Enter the number to the left of the song name]")
		x = input()
		try:
			x = int(x) - 1
		except:
			print("Error: Invalid song number")
			sys.exit()
	y = True
	while y:
		playsound(mp3List[x])
		y = loop