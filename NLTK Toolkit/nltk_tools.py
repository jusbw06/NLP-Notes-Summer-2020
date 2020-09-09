#!/bin/python3

import nltk, re, pprint
from nltk import word_tokenize
import numpy as np
from numpy import linalg as la
import string
from nltk.corpus import stopwords
kjv_additional_stpwrds = [ 'thou', 'thee', 'thy', 'unto', '\'s', 'ye', 'yet', 'us', 'lo']

# List
def add_stopwords(stpwrds, new_stpwrds):
    stpwrds = stpwrds + kjv_additional_stpwrds + new_stpwrds
    return stpwrds
        

# Cleans text of punctuation and stopwords
def clean_text(raw_text, stopwords):
    raw_text = raw_text.lower()
    raw_text.replace('\'s','')
    text_list = word_tokenize(raw_text)
    text_list = [word for word in text_list if word.lower() not in stopwords and word not in string.punctuation]
    return text_list

# takes in two lists
# each list shall be of tuples
# each tuple shall have a word in the first index and a frequency in the second index
# method will manually compute and return the cosine similarity of the two vectors
def compute_cosine_similarity(l1, l2):
    
    l1_extracted = [e[0] for e in l1] # extract words (index 0) from lists
    l2_extracted = [e[0] for e in l2]

    from_l1_add = [ (e[0], 0) for e in l1 if e[0] not in l2_extracted] # create list of tuples with zero counts for misses
    from_l2_add = [ (e[0], 0) for e in l2 if e[0] not in l1_extracted]

    # vectors should now be same length, add misses and sort
    l1 = sorted(l1 + from_l2_add) # sort alphabetically
    l2 = sorted(l2 + from_l1_add)

    v1 = [e[1] for e in l1] # extract word counts
    v2 = [e[1] for e in l2]

    v1 = np.array( v1, np.float) # convert to mathematical array
    v2 = np.array( v2, np.float)

    v1 = v1/la.norm(v1) # convert to unit vector
    v2 = v2/la.norm(v2)
    
    return np.dot(v1,v2) # compute dot product
    





# Parent class
class Document:

    # Class attributes

    # Initializer / Instance attributes
    def __init__(self, raw_text, title, stpwords = []):
        self.stopwords = add_stopwords(stopwords.words('english'), stpwords)
        self.doc_title = title
        self.doc_raw_text = raw_text        
        self.word_list = clean_text(self.doc_raw_text, self.stopwords)
        self.text_obj = nltk.Text(self.word_list)
        self.freq_dist = nltk.FreqDist(self.text_obj)


# Does a three step comparison
# 1) compares via individual word frequencies
# 2) compares via presence of certain acronyms
# 3) compares via presence of collocations
# Lastly, applies weights to each of the above before returning final score
    def compare(doc1, doc2):

        weights = np.array([ 3, 1, 3 ], np.int32)
        similarity_values = np.array([0, 0, 0], np.float)
        
        similarity_values[0] = doc1.compare_by_word_freq(doc2)
        similarity_values[1] = doc1.compare_by_acronym(doc2)
        similarity_values[2] = doc1.compare_by_collocation(doc2)
		
        result = (similarity_values[0]*weights[0] + similarity_values[1]*weights[1] + similarity_values[2]*weights[2]) / np.sum(weights)
        
        return result
		

    def compare_by_word_freq(doc1, doc2): # can be expanded to use bigrams and trigrams
    
        l1 = doc1.freq_dist.most_common(50) # extracted list of tuples
        l2 = doc2.freq_dist.most_common(50) # extracted list of tuples
    
        return compute_cosine_similarity(l1,l2)


    def compare_by_collocation(doc1, doc2):
    
        cl1 = doc1.text_obj.collocation_list(100,2) # uses word infreqency formula need be expanded to 
        cl2 = doc2.text_obj.collocation_list(100,2) # returns small value
        
        cl1 = [ ( (e[0] + ' ' + e[1]), 1) for e in cl1] # smash strings together, add freq 1
        cl2 = [ ( (e[0] + ' ' + e[1]), 1) for e in cl2]

        return compute_cosine_similarity(cl1,cl2)
        
    def compare_by_acronym(doc1, doc2):
        
        a1 = re.findall(r'[A-Z|0-9]{2,}',doc1.doc_raw_text) # done on raw text
        a2 = re.findall(r'[A-Z|0-9]{2,}',doc2.doc_raw_text)
        
        a1fd = nltk.FreqDist(a1).most_common(50)
        a2fd = nltk.FreqDist(a2).most_common(50)

        return compute_cosine_similarity(a1fd,a2fd)
        
        
    def return_most_common(self):
        return self.freq_dist.most_common(50)


    def __str__(self):
        return "Title: {0}".format(self.doc_titlename)
