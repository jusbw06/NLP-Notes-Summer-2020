#!/bin/python3
import os

path = '/home/justi/Documents/NLTK Project/DocumentFolder'

os.chdir(path)
list_files = sorted(os.listdir(path))
print(list_files)

for e in list_files:
	f = open(e, 'r')
	buff = f.read()
	f.close()
	print(buff)
