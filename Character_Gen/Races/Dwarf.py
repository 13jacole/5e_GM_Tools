#!/usr/bin/python
#Dwarf

import random



def Darkvision(Sub):
	if Sub == "3":
		Name = "Superior Darkvision"
		Feature = "You can see in dim light within 120 feet as if it were bright light, and in darkness as if it were dim light. You can't descern color in darkness, only shades of gray."
	else:
		Name = "Darkvision"
		Feature = "You can see in dim light within 60 feet as if it were bright light, and in darkness as if it were dim light. You can't descern color in darkness, only shades of gray."
	
	return Name, Feature
	
def Resilience():
	Name = "Dwarven Resilience"
	Feature = "You have advantage on saving throws against poison and you have resistance against poison damage"
	return Name, Feature

	