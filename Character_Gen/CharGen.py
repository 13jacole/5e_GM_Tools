#!/usr/bin/python
#Driver Script

#imports
import config #PC variables
from AbilityScore import ScoreGen


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
		from Races.Dwarf import *
		
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
		config.Ability_Scores.Con += 2
		
		#Size
		config.Size = "Medium"
		
		#Speed
		config.Speed = 25
		
		
		print("subraces - tbd")
	else:
		print("Invalid selection. Please try again")
