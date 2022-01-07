#!/usr/bin/python
#Elf

import numpy as np
import pandas as pd
import random

def HighElfCan():
    WizCant = pd.read_excel('.\\Spells\\Spells.xlsx', sheet_name='Wizard', index_col=None).astype({'Level':'int'})
    
    # For Testing directly
    #WizCant = pd.read_excel('..\\Spells\\Spells.xlsx', sheet_name='Wizard', index_col=None).astype({'Level':'int'})
    
    WizCant.index = range(1, len(WizCant)+1)
    WizCant = WizCant.loc[WizCant['Level'] == 0]
    
    print("You know one cantrip of your choice from the wizard spell list. Intelligence is your spellcasting ability for it.\n")
    
    print("Please select the number of the cantrip you wish to learn\n")
    
    print(WizCant.loc[:, WizCant.columns != 'Level'])
    
    while True:
        selCant = int(input())
        if selCant in WizCant.index:
            break
        else:
            print("Error -- Please type in the number to the left of the cantrip you wish to learn")
    
    return [1], [WizCant.iloc[selCant]['Name']]

