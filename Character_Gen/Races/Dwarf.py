#!/usr/bin/python
#Dwarf

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

def StoneCunning():
	Name = "Stonecunning"
	Feature = "Whenever you make an Intelligence (History) check related to the origin of stonework, you are considered proficient in the History skill and add double your proficiency bonus to the check, instead of your normal proficiency bonus."
	return Name, Feature
	
def DuergarResil():
	Name = "Duergar Resilience"
	Feature = "You have advantage on saving throws against illusions and against being charmed or paralyzed."
	return Name, Feature
	
def DuergarMag():
	Name = "Duergar Magic"
	Feature = "When you reach 3rd level, you can cast the enlarge/reduce spell on yourself once with this trait, using only the spell's enlarge option. When you reach 5th level, you can cast the invisibility spell on yourself once with this trait. You don't need material components for either spell, and you can't cast them while you're in direct sunlight, although sunlight has no effect on them once cast. You regain the ability to cast these spells with this trait when you finish a long rest. Intelligence is your spellcasting ability for these spells."
	return Name, Feature
	
def SunSens():
	Name = "Sunlight Sensitivity"
	Feature = "You have disadvantage on attack rolls and on Wisdom (Perception) checks that rely on sight when you, the target of your attack, or whatever you are trying to perceive is in direct sunlight"
	return Name, Feature