#!/bin/python3

from KJV_preprocess import bible_list, books
from nltk_tools import *

import numpy as np
from numpy import linalg as la

from plotting_tools import *

documents = []
for i in range(0, len(books)):
    documents.append(Document(bible_list[i], books[i]))

#scores = np.empty((len(books),len(books)), float)
scores = [[0 for i in range(len(books))] for j in range(len(books))]
for i in range(0, len(books)):
    for j in range(0,len(books)):
        scores[i][j] = "{0:.3f}".format(documents[i].compare(documents[j]))



##  Trim to Desired Books  ##
# takes list of indexes or name of book
def trim_to_desired_books( scores, books, init_list ):

	# step 1: find index for non int arguments
	indices = []
	for e in init_list:
		if type(e) == str:
			found = False
			for i in range(len(books)):
				if e.lower() in books[i].lower():
					indices.append(i)
					found = True 
					break
					
			if found == False:
				print('Unable to find match for: {e}'.format(e))	
		# if int, simply append to new list		
		elif type(e) == int:
			indices.append(e)
		else:
			print('Bad element: {0}'.format(e))
	indices = sorted(indices) # optional
	
	# step 2: remove unwanted 1st level elements
	new_list = []
	for i in range(len(scores)):
		if i in indices:
			new_list.append(scores[i])
	scores = new_list	
	
	
	# step 3: remove unwanted 2nd level elements
	for i in range(len(scores)):
		new_list = []
		for j in range(len(scores[i])):
			if j in indices:
				new_list.append(scores[i][j])
		scores[i] = new_list
		
	#step 4: do this for lists
	new_list = []
	for i in range(len(books)):
		if i in indices:
			new_list.append(books[i])
	books = new_list	
		
		
		
	return (scores, books)
				

#(scores, books) = trim_to_desired_books(scores, books, ['john','luke','matthew','mark'])
(scores, books) = trim_to_desired_books(scores, books, range(0,6))

createPlot(scores, 'Bible Book Similarity Scores', ( books, books ))


