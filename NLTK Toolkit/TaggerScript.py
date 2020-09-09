#!/bin/python3
import os, nltk

path = '/home/justi/Documents/NLTK Project/DocumentFolder'

os.chdir(path)

f = open('ClassifiedExample.txt', 'r')
buff = f.read()
f.close()
print(buff)

text = nltk.word_tokenize(buff)
tagged_text = nltk.pos_tag(text)
print(tagged_text)

nltk.help.upenn_tagset('RB')
nltk.help.upenn_tagset('MD')
nltk.help.upenn_tagset('JJ')
nltk.help.upenn_tagset('DT')
nltk.help.upenn_tagset('CD')
nltk.help.upenn_tagset('IN')
nltk.help.upenn_tagset('PRP')
nltk.help.upenn_tagset('VB*')
nltk.help.upenn_tagset('NN*')


