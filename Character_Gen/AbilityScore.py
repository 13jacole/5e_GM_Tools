#!/usr/bin/python

import random

#Function for ability scores

def AbilityScores(method):
	if method == 1: #Standard array
		return "Add code for standard array"
	if method == 2: #4d6 drop lowest
		nums = []
		nums.append(random.randint(1, 6))
		nums.append(random.randint(1, 6))
		nums.append(random.randint(1, 6))
		nums.append(random.randint(1, 6))
		nums.sort()
		nums[0] = 0
		
		return sum(nums)