#!/bin/python3
## This module shall implement the KNN classifier appropriate to the process

## This is organized in a class, so that it may be made interchangeable with any other learning algorithms
## By making each algorithm implementation a Class, we can hide slass variables and interchange algorithms without altering the wrapper code
class Classifier:
	
	# Class Variables
	data = [] # please rename or add more class variables as necessary
	
	## Input: Document as String
	## Output: category name as String
	def classify():
		
		# This particular classifier's preprocessing	
		# 1) Read from file cluster vectors [the other operands] and categories
		# Cluster vectors represented by: op2
		# recommend reading in from csv
		
		
		# 2) Calculate Operand 1 [This document's word freq vector]
		## doc = newDocument()
		## op1 = doc.createOperand() [creates word freq vector]
		
		
		# 3) KNN
		## Implement the KNN algorithm
		## can be implemented here or call function from another file
		## Use function doc.compare(op1,op2) instead of Euclidean distance or whatever distance algorithm
		
		
		# 4) return the name of the category, not just the index 
		pass


	# This function reads in the categorical labels and frequency vectors from a save file
	# places this in "data" class variable for later use in "classify"
	def readFromFile():
		pass
	
	
	
	
	# This function creates the save file from actual training data
	# Recommend CSV form
	def writeToFile():
		pass
