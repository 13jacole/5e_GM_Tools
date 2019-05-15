#!/usr/bin/python

import random

#Function for ability scores

def AbilityScores(method, rando):
	AbSc = [] # Str, Dex, Con, Int, Wis, Cha
	
	# Generate scores
	if method == 1: #Standard array
		AbSc = [15, 14, 13, 12, 10, 8]
	if method == 2: #4d6 drop lowest
		for x in range(0, 6):
			nums = []
			nums.append(random.randint(1, 6))
			nums.append(random.randint(1, 6))
			nums.append(random.randint(1, 6))
			nums.append(random.randint(1, 6))
			nums.sort()
			nums[0] = 0
			Score = sum(nums)
			AbSc.append(Score)
	if method == 3: #3d6
		for x in range(0, 6):
			nums = []
			nums.append(random.randint(1, 6))
			nums.append(random.randint(1, 6))
			nums.append(random.randint(1, 6))
			Score = sum(nums)
			AbSc.append(Score)
	if method == 4: #Custom
		for x in range(0, 6):
			print("Please enter score " + str(x+1) + "\n")
			AbSc.append(input())
	# Place scores
	if rando:
		random.shuffle(AbSc)
	else:
		Sc = AbSc
		AbSc = []
		Ab = ["Str", "Dex", "Con", "Int", "Wis", "Cha"]
		
		while len(Ab) > 0:
			print("Scores\n")
			print("--")
			for x in range(0, len(Sc)):
				print(str(Sc[x]))
				print("--")
			print("\nPlease indicate which of the above scores you want to assign as your "+Ab[0]+ " Score: ")
			dec = int(input())
			if int(dec) in Sc: 
				AbSc.append(dec)
				Sc.remove(dec)
				del Ab[0]
			else:
				print("Not a valid value. Please try again.")
		
	return AbSc