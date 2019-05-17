#!/usr/bin/python
#Dragonborn

import random

def Skyrim(r):
	while True:
		if r:
			sel = random.randint(1, 10)
			if sel == 1: Dragon = "black"
			elif sel == 2: Dragon = "blue"
			elif sel == 3: Dragon = "brass"
			elif sel == 4: Dragon = "bronze"
			elif sel == 5: Dragon = "copper"
			elif sel == 6: Dragon = "gold"
			elif sel == 7: Dragon = "green"
			elif sel == 8: Dragon = "red"
			elif sel == 9: Dragon = "silver"
			elif sel == 10: Dragon = "white"
		else:
			print("A number of your racial abilities are tied to your draconic ancestry.")
			print("What kind of dragon does your character descend from?")
			print("Please indicate by color:")
			print("Dragon\tDamage Type\tBreath Weapon")
			
			print("Black\tAcid\t5' by 30' line (Dex save)")
			print("Blue\tLightning\t5' by 30' line (Dex save)")
			print("Brass\tFire\t5' by 30' line (Dex save)")
			print("Bronze\tLightning\t5' by 30' line (Dex save)")
			print("Copper\tAcid\t5' by 30' line (Dex save)")
			print("Gold\tFire\t15' cone (Dex save)")
			print("Green\tPoison\t15' cone (Con save)")
			print("Red\tFire\t15' cone (Dex save)")
			print("Silver\tCold\t15' cone (Con save)")
			print("White\tCold\t15' cone (Con save)")
			
			Dragon = input()
		
		if Dragon.lower() == "black" or Dragon.lower() == "copper":
			Dam_Type = "Acid"
			Breath = "5' by 30' line (Dex save)"
			break
		elif Dragon.lower() == "blue" or Dragon.lower() == "bronze":
			Dam_Type = "Lightning"
			Breath = "5' by 30' line (Dex save)"
			break
		elif Dragon.lower() == "brass":
			Dam_Type = "Fire"
			Breath = "5' by 30' line (Dex save)"
			break
		elif Dragon.lower() == "gold" or Dragon.lower() == "red":
			Dam_Type = "Fire"
			Breath = "15' cone (Dex save)"
			break
		elif Dragon.lower() == "green":
			Dam_Type = "Poison"
			Breath = "15' cone (Con save)"
			break
		elif Dragon.lower() == "silver" or Dragon.lower() == "white":
			Dam_Type = "Cold"
			Breath = "15' cone (Con save)"
			break
		else:
			print("Invalid dragon color")
	return Dragon.lower(), Dam_Type, Breath
	
def Ancestry(Dragon):
	Name = "Draconic Ancestry"
	Feature = "You are distantly related to " + Dragon + " dragons, which impacts your other racial features."
	return Name, Feature
	
def BreathWeapon(Dam_Type, Breath):
	Name = "Breath Weapon"
	Feature = "You can use your action to exhale destructive energy. It deals damage in an area according to your ancestry. When you use your breath weapon, all creatures in the area must make a saving throw, the type of which is determined by your ancestry. The DC of this saving throw is 8 + your Constitution modifier + your proficiency bonus. A creature takes 2d6 damage on a failed save, and half as much damage on a successful one. The damage increase to 3d6 at 6th level, 4d6 at 11th, and 5d6 at 16th level. After using your breath weapon, you cannot use it again until you complete a short or long rest.\nDamage Type = " + Dam_Type + "\nBreath = " + Breath
	return Name, Feature
	
def Resistance(Dam_Type):
	Name = "Resistance"
	Feature = "You have resistance to " + Dam_Type + " damage."
	return Name, Feature