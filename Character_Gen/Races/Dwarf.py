#!/usr/bin/python
#Dwarf

## Feature Functions ##
def Darkvision():
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

def DwarfTough():
    Name = "Dwarven Toughness"
    Feature = "Your hit point maximum increases by 1, and it increases by 1 every time you gain a level."
    return Name, Feature