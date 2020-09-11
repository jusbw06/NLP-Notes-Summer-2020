#!/bin/python3
import os, sys

path = path = sys.argv[1]

os.chdir(path)
list_files = sorted(os.listdir(path))
print(list_files)

for e in list_files:
	
	# Open file
	fd = os.open(e,os.O_RDWR)
		
	# Read text
	buff = str(  os.read(fd,11000), "utf-8", "ignore")
	
	# Close File
	os.close(fd)


	print(buff)
