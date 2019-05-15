#!/usr/bin/python

#imports
from AbilityScore import AbilityScores

#Flags
need = True

#Ability Scores
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
scores = AbilityScores(method, ra)
print(scores)