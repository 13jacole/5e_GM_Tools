#!/usr/bin/python

import random

#Function for ability scores

def ScoreGen():

	while True:
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
			
	while True:
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
	#Call Function that generates scores
	
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
			AbSc.append(int(input()))
	# Place scores
	if ra:
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
	
	print("------")
	return AbSc