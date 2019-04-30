#!/usr/bin/env python

#dependencies
import os
import sys
import argparse
import warnings
import random

import pandas as pd
import numpy as np
#more imports

"""
magic_item_gen.py: Random amgic item selection program
       Usage: python magic_item_sel.py -s major/minor -r common/uncommon/rare/veryrare/legendary -n number of items to be generated (optional -- Default 1) -o Name of output text file
"""

#meta information
__author__ = "Jakob Cole"
__maintainer__ = "Jakob Cole"

#arguments
pa = argparse.ArgumentParser()
pa.add_argument('-s', '--scope', action='store', nargs=1, dest='item_scope',
                help='Item scope - major/minor', required=True)

pa.add_argument('-r', '--rarity', action='store', nargs=1, dest='item_rarity',
                help='Item rarity', required=True)

pa.add_argument('-n', '--num', action='store', nargs=1, dest='number',
                help='number of items outputted')
				
pa.add_argument('-o', '--out', action='store', nargs=1, dest='outFile',
                help='file to output file to', required=True)

args = pa.parse_args()	

item_scope = args.item_scope[0]
item_rarity = args.item_rarity[0]
if args.number is not None:
	number = int(args.number[0])
else:
	number = 1
	
f = open(args.outFile[0], "a+")

#import file
itemfile = str(item_scope) + '_' + str(item_rarity) + '.csv'
my_data = pd.read_csv(itemfile, delimiter=',', header=0)

#Determine item filter decision
print('Do you want to filter by item type? (Y/N): ')
dec = input()

if dec.lower() == 'y' or dec.lower == 'yes':
	print('Using the following list, please select which item types you want to choose from\n')
	print('Selection Number -- Item Type\n')
	
	filt_data = my_data[my_data['Type'].isin(['Armor'])]
	(rows, cols) = filt_data.shape
	if rows > 0:
		print('       1         -- Armor\n')
	filt_data = my_data[my_data['Type'].isin(['Potion'])]
	(rows, cols) = filt_data.shape
	if rows > 0:
		print('       2         -- Potion\n')
	filt_data = my_data[my_data['Type'].isin(['Ring'])]
	(rows, cols) = filt_data.shape
	if rows > 0:
		print('       3         -- Ring\n')
	filt_data = my_data[my_data['Type'].isin(['Rod'])]
	(rows, cols) = filt_data.shape
	if rows > 0:
		print('       4         -- Rod\n')
	filt_data = my_data[my_data['Type'].isin(['Scroll'])]
	(rows, cols) = filt_data.shape
	if rows > 0:
		print('       5         -- Scroll\n')
	filt_data = my_data[my_data['Type'].isin(['Staff'])]
	(rows, cols) = filt_data.shape
	if rows > 0:
		print('       6         -- Staff\n')
	filt_data = my_data[my_data['Type'].isin(['Wand'])]
	(rows, cols) = filt_data.shape
	if rows > 0:
		print('       7         -- Wand\n')
	filt_data = my_data[my_data['Type'].isin(['Weapon'])]
	(rows, cols) = filt_data.shape
	if rows > 0:
		print('       8         -- Weapon\n')
	filt_data = my_data[my_data['Type'].isin(['Wondrous Item'])]
	(rows, cols) = filt_data.shape
	if rows > 0:
		print('       9         -- Wondrous Item\n\n')
	
	print('Please use the number selection column.\n')
	print('If you have more than one item type you want to pick from\n')
	print('please put all applicable numbers\n')
	typefilt = input()
	typefilt = list(typefilt)
	
	typefiltname = []
	if '1' in typefilt:
		typefiltname.append('Armor')
		print('You have selected Armor\n')
	if '2' in typefilt:
		typefiltname.append('Potion')
		print('You have selected Potion\n')
	if '3' in typefilt:
		typefiltname.append('Ring')
		print('You have selected Ring\n')
	if '4' in typefilt:
		typefiltname.append('Rod')
		print('You have selected Rod\n')
	if '5' in typefilt:
		typefiltname.append('Scroll')
		print('You have selected Scroll\n')
	if '6' in typefilt:
		typefiltname.append('Staff')
		print('You have selected Staff\n')
	if '7' in typefilt:
		typefiltname.append('Wand')
		print('You have selected Wand\n')
	if '8' in typefilt:
		typefiltname.append('Weapon')
		print('You have selected Weapon\n')
	if '9' in typefilt:
		typefiltname.append('Wondrous item')
		print('You have selected Wondrous item\n')
	
	item_data = my_data[my_data['Type'].isin(typefiltname)]
else:
	item_data = my_data

f.write(item_scope + " " + item_rarity + "\n")
while number > 0:
	#pick random item
	(rows, cols) = item_data.shape
	x = random.randint(0, (rows-1))
	
	if item_data.iloc[x,3] != 'All':
		print(item_data.iloc[x,0] + " has the following use restriction: " + item_data.iloc[x,3])
		print("Do you want to generate a different item? (Y/N)")
		Rest_Dec = input()
	else:
		Rest_Dec = 'n'
	
	if Rest_Dec.lower() == 'n' or Rest_Dec.lower == 'no':
		if args.outFile is not None:
			f.write('/////////////////\n')
			f.write('Item: ' + item_data.iloc[x, 0] + "\n")
			f.write('Type: ' + item_data.iloc[x, 1] + "\n")
			f.write('Attune: ' + item_data.iloc[x, 2] + "\n")
			f.write('Restrictions: ' + item_data.iloc[x, 3] + "\n")
			f.write('Source: ' + item_data.iloc[x, 4] + "\n")
			f.write('/////////////////\n')
			
		print('/////////////////')
		print(item_data.iloc[x])
		print('/////////////////')
		
		number = number - 1