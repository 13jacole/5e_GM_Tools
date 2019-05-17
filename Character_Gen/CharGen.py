#!/usr/bin/python
#Driver Script

#imports
import config #PC variables
from AbilityScore import ScoreGen

import random

#Ability Scores
Score = ScoreGen()
config.Ability_Scores.Str += Score[0]
config.Ability_Scores.Dex += Score[1]
config.Ability_Scores.Con += Score[2]
config.Ability_Scores.Int += Score[3]
config.Ability_Scores.Wis += Score[4]
config.Ability_Scores.Cha += Score[5]

print(config.Ability_Scores.Str)
print(config.Ability_Scores.Dex)
print(config.Ability_Scores.Con)
print(config.Ability_Scores.Int)
print(config.Ability_Scores.Wis)
print(config.Ability_Scores.Cha)

##########################
# Let's figure out races # Have selection in this script, and call a different piece for each race/subrace that will be imported
##########################

while True:

	print("What race do you want to play as?")
	print("Please use the number to the left of the name\n")
	print("Core")
	print("1. Dragonborn\n")
	print("2. Dwarf\n")
	
	rdec = input()
	
	if rdec == "1":
		from Races.Dragonborn import *
		config.Race = "Dragonborn"
		
		#Randomize
		while True:
			print("Do you want to randomize your Dragonborn race options?")
			dec = input()
			if dec.lower() == "n" or dec.lower() == "no":
				r = False
				break
			elif dec.lower() == "y" or dec.lower() == "ye" or dec.lower() == "yes":
				r = True
				break
			else:
				print("Error: Invalid input")
			
		#ASI
		config.Ability_Scores.Str += 2
		config.Ability_Scores.Cha += 1
		
		#Size
		config.Size = "Medium"
		
		#Speed
		config.Speed = 30
		
		#Languages
		config.Prof.language.append("Common")
		config.Prof.language.append("Draconic")
		
		#Features
		Dragon, Dam_Type, Breath = Skyrim(r)
		print("---")
		
		Name, Feature = Ancestry(Dragon)
		config.Features = config.Features.append({'Name' : Name, 'Desc' : Feature}, ignore_index=True)
		
		Name, Feature = BreathWeapon(Dam_Type, Breath)
		config.Features = config.Features.append({'Name' : Name, 'Desc' : Feature}, ignore_index=True)
		
		Name, Feature = Resistance(Dam_Type)
		config.Features = config.Features.append({'Name' : Name, 'Desc' : Feature}, ignore_index=True)
		
		print(config.Features)
		break
	elif rdec == "2":
		while True:
			print("Do you want to randomize your Dwarf race options?")
			dec = input()
			if dec.lower() == "n" or dec.lower() == "no":
				r = False
				break
			elif dec.lower() == "y" or dec.lower() == "ye" or dec.lower() == "yes":
				r = True
				break
			else:
				print("Error: Invalid input")
		while True:
			if r:
				Sub = random.randint(1, 3)
			else:
				print("Dwarves are a stout and hardy race, with 3 principle subraces:")
				print("Would you like to be a...?\n")
				print("1) Hill Dwarf -- Increased WIS and HP")
				print("2) Mountain Dwarf -- Huge STR boost and armor proficiencies")
				print("3) Duergar (Grey Dwarf) -- Increased STR, better darkvision, some spells, and sunlight sensitivity")
				print("\n")
				Sub = int(input())
			
			if Sub == 1:
				config.Race = "Hill Dwarf"
				print("You have selected Hill Dwarf")
				config.Ability_Scores.Wis += 1
				break
			elif Sub == 2:
				config.Race = "Mountain Dwarf"
				print("You have selected Mountain Dwarf")
				config.Ability_Scores.Str += 2
				break
			elif Sub == 3:
				config.Race = "Duergar - Grey Dwarf"
				print("You have selected Duergar")
				config.Ability_Scores.Str += 1
				break
			else:
				print("Invalid input. Please try again.")
			
		##Dwarf.py can have functions/logic for each subrace. --> pass in Sub
		from Races.Dwarf import *
		#ASI
		config.Ability_Scores.Con += 2
		
		#Size
		config.Size = "Medium"
		
		#Speed
		config.Speed = 25
		
		#Languages
		config.Prof.language.append("Common")
		config.Prof.language.append("Dwarvish")
		
		#Proficiencies
		config.Prof.weapon.append("battleaxe")
		config.Prof.weapon.append("handaxe")
		config.Prof.weapon.append("throwing hammer")
		config.Prof.weapon.append("warhammer")
		
		#Make tool choice
		while True:
			if r:
				cho = random.randint(1, 3)
			else:
				print("Dwarves gain tool proficiency with one of the following toolsets:\n")
				print("1)\tSmith's Tools")
				print("2)\tBrewer's Supplies")
				print("3)\tMason's Tools")
				cho = int(input())

			if cho == 1:
				ToolChoice = "smith's tools"
				break
			elif cho == 2:
				ToolChoice = "brewer's supplies"
				break
			elif cho == 3:
				ToolChoice = "mason's tools"
				break
			else:
				print("Invalid input. Please try again")
			
		config.Prof.tool.append(ToolChoice)
		
		#Features
		Name, Feature = Darkvision(Sub)
		config.Features = config.Features.append({'Name' : Name, 'Desc' : Feature}, ignore_index=True)
		
		Name, Feature = Resilience()
		config.Features = config.Features.append({'Name' : Name, 'Desc' : Feature}, ignore_index=True)
		
		
		
		print("subraces - tbd")
		break
	else:
		print("Invalid selection. Please try again")
