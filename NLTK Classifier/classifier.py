# from KNN.py import Classifier as cl-- this is what will happen


# This module shall do the management surrounding the classifier
def execute_classifier():
	
	
	# 1) Read Document(s) From File
	## Input: File Name as String
	## Output: Document Contents as String
	
	
	# 2) Read the algorithm input data from file (only want to do this once)
	cl.readFromFile
	
	
	### SOME FUTURE WRAPPER CODE ###
	# (Like for multiple layers)
	
	
	# 3) Execute the Particular Algorithm -- (KNN)
	## Input: Document Contents as String
	## Output: Category as String
	out = cl.classify()
	
	
	
	# 4) Print the output category
	print(out)
	
