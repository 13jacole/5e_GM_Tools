#!/usr/bin/python
#Elf

import numpy as np
import pandas as pd
import random

def HighElfCan(r):
    WizCant = pd.read_excel('.\\Spells\\Spells.xlsx', sheet_name='Wizard', index_col=None).astype({'Level':'int'})
    
    # For Testing directly
    #WizCant = pd.read_excel('..\\Spells\\Spells.xlsx', sheet_name='Wizard', index_col=None).astype({'Level':'int'})
    
    WizCant.index = range(1, len(WizCant)+1)
    WizCant = WizCant.loc[WizCant['Level'] == 0]
    
        if r:
            selCant = random.randint(1, len(WizCant))
            print("You now know the " + WizCant.iloc[selCant]['Name'] + " cantrip!")
    else:
        print("You know one cantrip of your choice from the wizard spell list. Intelligence is your spellcasting ability for it.\n")
        
        print("Please select the number of the cantrip you wish to learn\n")
        
        print(WizCant.loc[:, WizCant.columns != 'Level'])

        while True:
            selCant = input()
            if selCant.isnumeric():
                selCant = int(selCant)
                if selCant in WizCant.index:
                    print("You have selected " + WizCant.iloc[selCant]['Name'])
                    break
        
        print("Error -- Please type in the number to the left of the cantrip you wish to learn")
    
    return [1], [WizCant.iloc[selCant]['Name']]

def Darkvision(Sub):
	if Sub == "3":
		Name = "Superior Darkvision"
		Feature = "You can see in dim light within 120 feet as if it were bright light, and in darkness as if it were dim light. You can't descern color in darkness, only shades of gray."
	else:
		Name = "Darkvision"
		Feature = "You can see in dim light within 60 feet as if it were bright light, and in darkness as if it were dim light. You can't descern color in darkness, only shades of gray."
	
	return Name, Feature
    
def KeenSenses():
    Name = "Keen Senses"
    Feature = "You have Proficiency in the Perception skill"
    
    for i in range(len(config.Skills)):
        if config.Skills[i][0] == "Perception":
            config.Skills[i][1] = 1
    
    return Name, Feature
    
def FeyAncestry():
    Name = "Fey Ancestry"
    Feature = "You have advantage on saving throws against being charmed, and magic can't put you to sleep."
    
    return Name, Feature
    
def Trance():
    Name = "Trance"
    Feature = "Elves don't need to sleep. Instead, they meditate deeply, remaining semiconscious, for 4 hours a day. (The Common word for such meditation is 'trance.') While meditating, you can dream after a fashion; such dreams are actually mental exercises that have become reflexive through years of practice. After resting in this way, you gain the same benefit that a human does from 8 hours of sleep."
    
    return Name, Feature
    
def ExtraLanguage(LangKnown, r):
    Options = ["Abyssal","Aquan","Auran","Celestial","Common","Deep Speech","Draconic","Druidic","Dwarvish","Elvish","Giant","Gnomish","Goblin","Gnoll","Halfling","Ignan","Infernal","ORC","Primordial","Sylvan","Terran","Undercommon"]
    
    for Lang in LangKnown:
        Options.remove(Lang)
        
    if r:
        ch = random.randint(1, len(Options))
    else:
        for i in range(1, len(Options)):
            print(str(i) + ")\t" + Options[i] + "\n")
            
        print("You get an extra language! Please type the number of the language you wish to add:")
        
        while true:
            ch = input()
            if ch.isnumeric():
                ch = int(ch)
                if ch > 0 and ch < len(Options):
                    print("You have selected " + Options[ch-1])
                    break
                
        print("Error - Please type the number of the language you wish to add")
        
    config.Prof.language.append(Options[ch-1])
    
def WildMask():
    Name = "Mask of the Wild"
    Feature = "You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena."
    
    return Name, Feature
    
def SunlightSensitive():
    Name = "Sunlight Sensitivity"
    Feature = "You have disadvantage on attack rolls and Wisdom (Perception) checks that rely on sight when you, the target of your attack, or whatever you are tryign to perceive is in direct sunlight."
    
    return Name, Feature
