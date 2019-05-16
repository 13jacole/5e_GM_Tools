#!/usr/bin/python

#imports
import numpy as np
import pandas as pd
from AbilityScore import AbilityScores

######################
#Character Sheet Items
class Ab_Sco:
	def __init__(self, Str, Dex, Con, Int, Wis, Cha):
		self.Str = Str
		self.Dex = Dex
		self.Con = Con
		self.Int = Int
		self.Wis = Wis
		self.Cha = Cha

Ability_Scores = Ab_Sco(0, 0, 0, 0, 0, 0)

Level = 0
Class = ""
Race = ""

class Background:
	def __init__(self, trait, ideal, bond, flaw):
		self.trait = trait
		self.ideal = ideal
		self.bond = bond
		self.flaw = flaw

bg = Background("", "", "", "")

Alignment = ""
Exp = 0
Prof_Bonus = 0
SaveThrow = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
Skills = [[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0]]
#Passive_Percept = 0 #Passive Perception is just 10 + perception mod --> can be calculated on the fly
AC = 0
Initiative = 0
Speed = 0
Max_HP = 0 #No need to calculate current/temp --> generating characters default to max hp
Hit_Die_Type = ""
Hit_Die_Num = 0
Equipment = pd.DataFrame(columns=['Name'])
class Currency:
	def __init__(self, cp, sp, ep, gp, pp):
		self.cp = cp
		self.sp = sp
		self.ep = ep
		self.gp = gp
		self.pp = pp

Money = Currency(0, 0, 0, 0, 0)

class Proficiencies:
	def __init__(self, armor, weapon, language, tool):
		self.armor = armor
		self.weapon = weapon
		self.language = language
		self.tool = tool

Prof = Proficiencies([], [], [], [])

Features = pd.DataFrame(columns=['Name', 'Desc'])

Spells0 = pd.DataFrame(columns=['Prep', 'Name'])
Spells1 = pd.DataFrame(columns=['Prep', 'Name'])
Spells2 = pd.DataFrame(columns=['Prep', 'Name'])
Spells3 = pd.DataFrame(columns=['Prep', 'Name'])
Spells4 = pd.DataFrame(columns=['Prep', 'Name'])
Spells5 = pd.DataFrame(columns=['Prep', 'Name'])
Spells6 = pd.DataFrame(columns=['Prep', 'Name'])
Spells7 = pd.DataFrame(columns=['Prep', 'Name'])
Spells8 = pd.DataFrame(columns=['Prep', 'Name'])
Spells9 = pd.DataFrame(columns=['Prep', 'Name'])
######################

#Ability Scores
def ScoreGen():
	#Flags
	need = True
	while need:
		print("You have chosen to generate new ability scores")
		print("Please choose the number corresponding to your desired score generation method:\n")
		print("1. Standard Array\n")
		print("2. 4d6 drop lowest\n")
		print("3. 3d6\n")
		print("4. Custom scores\n")
		dec = input()
		if dec == "1":
			method = 1
			break
		elif dec == "2":
			method = 2
			break
		elif dec == "3":
			method = 3
			break
		elif dec == "4":
			method = 4
			break
		else:
			print("Invalid method type. Please try again.\n")
			
	while need:
		print("Do you want to randomize your score placement? (Y/N):")
		dec = input()
		if dec.lower() == "y" or dec.lower() == "yes" or dec.lower() == "ye":
			ra = True
			break
		elif dec.lower() == "n" or dec.lower() == "no":
			ra = False
			break
		else:
			print("Invalid input. Please try again")
			
	#Test
	return AbilityScores(method, ra)
	
Score = ScoreGen()
Ability_Scores.Str += Score[0]
Ability_Scores.Dex += Score[1]
Ability_Scores.Con += Score[2]
Ability_Scores.Int += Score[3]
Ability_Scores.Wis += Score[4]
Ability_Scores.Cha += Score[5]

print(Ability_Scores.Str)
print(Ability_Scores.Dex)
print(Ability_Scores.Con)
print(Ability_Scores.Int)
print(Ability_Scores.Wis)
print(Ability_Scores.Cha)