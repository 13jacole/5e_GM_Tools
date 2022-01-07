#!/usr/bin/python
#Human

import numpy as np
import pandas as pd
import random

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
    