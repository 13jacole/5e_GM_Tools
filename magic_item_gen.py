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
       Usage: python magic_item_gen.py -s major/minor -r common/uncommon/rare/veryrare/legendary
"""

#meta information
__author__ = "Jakob Cole"
__version__ = "2019.04.25"
__maintainer__ = "Jakob Cole"
__email__ = "jakobcole13@gmail.com"

#arguments
pa = argparse.ArgumentParser()
pa.add_argument('-s', '--scope', action='store', nargs=1, dest='item_scope',
                help='Item scope - major/minor', required=True)

pa.add_argument('-r', '--rarity', action='store', nargs=1, dest='item_rarity',
                help='Item rarity', required=True)

pa.add_argument('-n', '--num', action='store', nargs=1, dest='number',
                help='number of items outputted')

args = pa.parse_args()	

item_scope = args.item_scope[0]
item_rarity = args.item_rarity[0]
if args.number is not None:
	number = int(args.number[0])
else:
	number = 1

#import file
itemfile = str(item_scope) + '_' + str(item_rarity) + '.csv'
my_data = pd.read_csv(itemfile, delimiter=',', header=0)

#Determine item filter decision
print('Do you want to filter by item type? (Y/N): ')
dec = input()

if dec.lower() == 'y' or dec.lower == 'yes':
	print('Using the following list, please select which item types you want to choose from\n')
	print('Selection Number -- Item Type\n')
	print('       1         -- Armor\n')
	print('       2         -- Potion\n')
	print('       3         -- Ring\n')
	print('       4         -- Rod\n')
	print('       5         -- Scroll\n')
	print('       6         -- Staff\n')
	print('       7         -- Wand\n')
	print('       8         -- Weapon\n')
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
#### add filter code using https://cmdlinetips.com/2018/02/how-to-subset-pandas-dataframe-based-on-values-of-a-column/

while number > 0:
	#pick random item
	(rows, cols) = item_data.shape
	x = random.randint(0, rows)
	
	#Add code to handle filtering out all types (i.e. there are no major legendary potions)
	
	#output
	print('/////////////////')
	print(item_data.iloc[x])
	print('/////////////////')
	
	number = number - 1