#!/usr/bin/python
#Driver Script

#imports
import config #PC variables
from AbilityScore import ScoreGen

import random

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

    availableRaces = ["Dragonborn", "Dwarf", "Elf", "Halfling", "Human", "Gnome", "Half-Elf", "Half-Orc", "Tiefling"]
    print("What race do you want to play as?")
    print("Please use the number to the left of the name\n")
    print("Core")
    for i in len(availableRaces):
        print(str(i) + ". " + availableRaces[i] + "\n")
    
    rdec = input()
    
    if rdec == "1":
        from Races.Dragonborn import *
        config.Race = "Dragonborn"
        
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
            print("Do you want to randomize your Dwarf race options?")
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
        
        #Languages
        config.Prof.language.append("Common")
        config.Prof.language.append("Dwarvish")
        
        #Proficiencies
        config.Prof.weapon.append("battleaxe")
        config.Prof.weapon.append("handaxe")
        config.Prof.weapon.append("light hammer")
        config.Prof.weapon.append("warhammer")
        
        #Universal Features
        Name, Feature = Darkvision()
        config.Features = config.Features.append({'Name' : Name, 'Desc' : Feature}, ignore_index=True)
        
        ## Active Choices ##
        while True:
            if r:
                Sub = random.randint(1, 2)
            else:
                print("Dwarves are a stout and hardy race, with 2 principle subraces:")
                print("Would you like to be a...?\n")
                print("1) Hill Dwarf -- Increased WIS and HP")
                print("2) Mountain Dwarf -- Huge STR boost and armor proficiencies")
                print("\n")
                while True:
                    Sub = input()
                    if Sub.isnumeric():
                        Sub = int(Sub)
                        break
                    print("Error: Invalid Input")
            
            if Sub == 1:
                config.Race = "Hill Dwarf"
                print("You have selected Hill Dwarf")
                config.Ability_Scores.Wis += 1
                config.Max_HP += 1
                Name, Feature = DwarfTough()
                config.Features = config.Features.append({'Name' : Name, 'Desc' : Feature}, ignore_index=True)
                break
            elif Sub == 2:
                config.Race = "Mountain Dwarf"
                print("You have selected Mountain Dwarf")
                config.Ability_Scores.Str += 2
                config.Prof.armor.append("light")
                config.Prof.armor.append("medium")
                break
            else:
                print("Invalid input. Please try again.")
        
        #Make tool choice
        while True:
            if r:
                cho = random.randint(1, 3)
            else:
                print("Dwarves gain tool proficiency with one of the following toolsets:\n")
                print("1)\tSmith's Tools")
                print("2)\tBrewer's Supplies")
                print("3)\tMason's Tools")
                cho = int(input())

            if cho == 1:
                ToolChoice = "smith's tools"
                break
            elif cho == 2:
                ToolChoice = "brewer's supplies"
                break
            elif cho == 3:
                ToolChoice = "mason's tools"
                break
            else:
                print("Invalid input. Please try again")
            
        config.Prof.tool.append(ToolChoice)
        
        #Features
        Name, Feature = Resilience()
        config.Features = config.Features.append({'Name' : Name, 'Desc' : Feature}, ignore_index=True)
        
        Name, Feature = StoneCunning()
        config.Features = config.Features.append({'Name' : Name, 'Desc' : Feature}, ignore_index=True)
        
        print(config.Features)
        break
    elif rdec == "3":
        
        from Races.Elf import *
        while True:
            print("Do you want to randomize your Elf race options?")
            dec = input()
            if dec.lower() == "n" or dec.lower() == "no":
                r = False
                break
            elif dec.lower() == "y" or dec.lower() == "ye" or dec.lower() == "yes":
                r = True
                break
            else:
                print("Error: Invalid input")
                
        ## Universal Pieces ##
            
        #ASI
        config.Ability_Scores.Dex += 2
        
        #Size
        config.Size = "Medium"
        
        #Speed
        config.Speed = 30
        
        #Languages
        config.Prof.language.append("Common")
        config.Prof.language.append("Elvish")
        
        #Universal Features
        Name, Feature = KeenSenses()
        config.Features = config.Features.append({'Name' : Name, 'Desc' : Feature}, ignore_index=True)
        Name, Feature = FeyAncestry()
        config.Features = config.Features.append({'Name' : Name, 'Desc' : Feature}, ignore_index=True)
        Name, Feature = Trance()
        config.Features = config.Features.append({'Name' : Name, 'Desc' : Feature}, ignore_index=True)
        
        ##Active Choices Start Here
        while True:
            if r:
                Sub = random.randint(1, 3)
            else:
                print("Elves are a graceful people heavily in tune with magic, with 6 principle subraces:")
                print("Would you like to be a...?\n")
                print("1) High Elf -- Increased INT, a cantrip, and weapon proficiencies")
                print("2) Wood Elf -- Increased WIS, weapon proficiencies, and extra speed")
                print("3) Drow(Dark Elf) -- Increased CHA, better darkvision, weapon proficiencies, and some magic")
                print("\n")
                while True:
                    Sub = input()
                    if Sub.isnumeric():
                        Sub = int(Sub)
                        break
                    print("Error: Invalid Input")
            
            if Sub == 1:
                config.Race = "High Elf"
                print("You have selected High Elf")
                config.Ability_Scores.Int += 1
                config.Prof.weapon.append("longsword")
                config.Prof.weapon.append("shortsword")
                config.Prof.weapon.append("longbow")
                config.Prof.weapon.append("shortbow")
                config.Spells0['Prep'], config.Spells0['Name'] = HighElfCan(r)
                ExtraLanguage(config.Prof.language, r)
                break
            elif Sub == 2:
                config.Race = "Wood Elf"
                print("You have selected Wood Elf")
                config.Ability_Scores.Wis += 1
                config.Prof.weapon.append("longsword")
                config.Prof.weapon.append("shortsword")
                config.Prof.weapon.append("longbow")
                config.Prof.weapon.append("shortbow")
                config.Speed = 35
                Name, Feature = WildMask()
                config.Features = config.Features.append({'Name' : Name, 'Desc' : Feature}, ignore_index=True)
                break
            elif Sub == 3:
                config.Race = "Dark Elf (Drow)"
                print("You have selected Dark Elf")
                config.Ability_Scores.Cha += 1
                config.Prof.weapon.append("rapier")
                config.Prof.weapon.append("shortsword")
                config.Prof.weapon.append("hand crossbow")
                config.Speed = 35
                Name, Feature = WildMask()
                config.Features = config.Features.append({'Name' : Name, 'Desc' : Feature}, ignore_index=True)
                Name, Feature = SunlightSensitive()
                config.Features = config.Features.append({'Name' : Name, 'Desc' : Feature}, ignore_index=True)
                config.Spells0.loc[len(config.Spells0] = ['1', 'Dancing Lights']
                break
            else:
                print("Invalid input. Please try again.")
        
        
        Name, Feature = Darkvision(Sub)
        config.Features = config.Features.append({'Name' : Name, 'Desc' : Feature}, ignore_index=True)
        
        print(config.Features)
        break
elif rdec == "4":
        
        from Races.Halfling import *
        while True:
            print("Do you want to randomize your Halfling race options?")
            dec = input()
            if dec.lower() == "n" or dec.lower() == "no":
                r = False
                break
            elif dec.lower() == "y" or dec.lower() == "ye" or dec.lower() == "yes":
                r = True
                break
            else:
                print("Error: Invalid input")
                
        ## Universal Pieces ##
            
        #ASI
        config.Ability_Scores.Dex += 2
        
        #Size
        config.Size = "Small"
        
        #Speed
        config.Speed = 25
        
        #Languages
        config.Prof.language.append("Common")
        config.Prof.language.append("Halfling")
        
        #Universal Features
        Name, Feature = LuckyHalf()
        config.Features = config.Features.append({'Name' : Name, 'Desc' : Feature}, ignore_index=True)
        Name, Feature = Brave()
        config.Features = config.Features.append({'Name' : Name, 'Desc' : Feature}, ignore_index=True)
        Name, Feature = NimbleHalf()
        config.Features = config.Features.append({'Name' : Name, 'Desc' : Feature}, ignore_index=True)
        
        ##Active Choices Start Here
        while True:
            if r:
                Sub = random.randint(1, 2)
            else:
                print("Halflings are a diminutive cheerful people, with 2 principle subraces:")
                print("Would you like to be a...?\n")
                print("1) Lightfoot Halfling -- Increased Cha, extra stealthy")
                print("2) Stout Halfling -- Increased Con, resistant to poison")
                print("\n")
                while True:
                    Sub = input()
                    if Sub.isnumeric():
                        Sub = int(Sub)
                        break
                    print("Error: Invalid Input")
            
            if Sub == 1:
                config.Race = "Lightfoot"
                print("You have selected Lightfoot Halfling")
                config.Ability_Scores.Cha += 1
                Name, Feature = NaturalStealth()
                config.Features = config.Features.append({'Name' : Name, 'Desc' : Feature}, ignore_index=True)
                break
            elif Sub == 2:
                config.Race = "Stout"
                print("You have selected Stout Halfling")
                config.Ability_Scores.Con += 1
                Name, Feature = StoutResil()
                config.Features = config.Features.append({'Name' : Name, 'Desc' : Feature}, ignore_index=True)
                break
            else:
                print("Invalid input. Please try again.")
                
elif rdec == "5":
        
        from Races.Human import *
        while True:
            print("Do you want to randomize your Human race options?")
            dec = input()
            if dec.lower() == "n" or dec.lower() == "no":
                r = False
                break
            elif dec.lower() == "y" or dec.lower() == "ye" or dec.lower() == "yes":
                r = True
                break
            else:
                print("Error: Invalid input")
                
        print("Humans are a diverse people with startling potential")
        ## Universal Pieces ##
            
        #ASI
        config.Ability_Scores.Str += 1
        config.Ability_Scores.Dex += 1
        config.Ability_Scores.Con += 1
        config.Ability_Scores.Int += 1
        config.Ability_Scores.Wis += 1
        config.Ability_Scores.Cha += 1
        
        #Size
        config.Size = "Medium"
        
        #Speed
        config.Speed = 30
        
        #Languages
        config.Prof.language.append("Common")
        
        #Universal Features
        Name, Feature = ExtraLanguage()
        config.Features = config.Features.append({'Name' : Name, 'Desc' : Feature}, ignore_index=True)
        
        print(config.Features)
        break
            
elif rdec == "6":
        
        from Races.Gnome import *
        while True:
            print("Do you want to randomize your Gnome race options?")
            dec = input()
            if dec.lower() == "n" or dec.lower() == "no":
                r = False
                break
            elif dec.lower() == "y" or dec.lower() == "ye" or dec.lower() == "yes":
                r = True
                break
            else:
                print("Error: Invalid input")
                
        ## Universal Pieces ##
            
        #ASI
        config.Ability_Scores.Int += 2
        
        #Size
        config.Size = "Small"
        
        #Speed
        config.Speed = 25
        
        #Languages
        config.Prof.language.append("Common")
        config.Prof.language.append("Gnomish")
        
        #Universal Features
        Name, Feature = Darkvision()
        config.Features = config.Features.append({'Name' : Name, 'Desc' : Feature}, ignore_index=True)
        
        Name, Feature = GnomeCunning()
        config.Features = config.Features.append({'Name' : Name, 'Desc' : Feature}, ignore_index=True)
        
        while True:
            if r:
                Sub = random.randint(1, 2)
            else:
                print("Gnomes are a vibrant people with a penchant for tinkering, who have 2 principle subraces")
                print("Would you like to be a...?\n")
                print("1) Forest Gnome -- Increased Dex, illusion cantrip, talk to animals")
                print("2) Rock Knome -- Increased Con, bonus to history, create clockwork devices")
                print("\n")
                while True:
                    Sub = input()
                    if Sub.isnumeric():
                        Sub = int(Sub)
                        break
                    print("Error: Invalid Input")
            
            if Sub == 1: #edits needed starting here
                config.Race = "Forest Gnome"
                print("You have selected Forest Gnome")
                config.Ability_Scores.Cha += 1
                Name, Feature = NaturalStealth()
                config.Features = config.Features.append({'Name' : Name, 'Desc' : Feature}, ignore_index=True)
                break
            elif Sub == 2:
                config.Race = "Stout"
                print("You have selected Stout Halfling")
                config.Ability_Scores.Con += 1
                Name, Feature = StoutResil()
                config.Features = config.Features.append({'Name' : Name, 'Desc' : Feature}, ignore_index=True)
                break
            else:
                print("Invalid input. Please try again.")
        
        print(config.Features)
        break
    else:
        print("Invalid selection. Please try again")
