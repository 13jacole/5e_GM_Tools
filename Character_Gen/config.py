#!/usr/bin/python
#Configuration items

import numpy as np
import pandas as pd

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

Size = ""
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