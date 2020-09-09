#!/bin/python3

### Important output variables ###
# text_title -- KJV
# old_testament & new_testament -- testament titles
# books -- list of strings; contains book titles
# bible_list -- list of strings; contains individual book contents

import nltk, re
from nltk.corpus import gutenberg

#gutenberg.raw,words,sents

bible_raw = gutenberg.raw("bible-kjv.txt") # string

# Titles & Headers
# Find all Headers
books = re.findall(r'\n{2,3}[^0-9a-zA][^0-9]*(?:Book|Proverbs|Ecclesiastes|Song|Testament|Gospel|Revelation|Ezra|Epistle|Prophet|Hosea|Amos|Obadiah|Jonah|Micah|Nahum|Habakkuk|Zephaniah|Haggai|Zechariah|Malachi|Lamentations|Acts|Joel).*\n{2,3}', bible_raw)

# Title of Work
text_title = bible_raw[:bible_raw.find("\n")]

# Replace all Headers with pipe
for i in range(0,len(books)):
    bible_raw = bible_raw.replace(books[i],"|")

# Split at pipe, Place text in lists
bible_list = bible_raw.split("|") 
bible_list.pop(0); # remove title

# Extract New & Old Testament Titles
t = books[0].split("\n")
for i in range(0,t.count("")):
    t.remove("")
old_testament = t[0]
books[0] = t[1]

t = books[39].split("\n")
for i in range(0,t.count("")):
    t.remove("")
new_testament = t[0]
books[39] = t[1]


# Strip Leading and Trailing newlines from Titles & Headers
for i in range(0,len(books)):
    books[i] = books[i].strip("\n")
    books[i] = books[i].rstrip("\n")
    books[i] = books[i].replace("\n"," ") # replace other newlines with spaces

# Extract Verse Numbers
# delete all verse numberings
for i in range(0, len(bible_list)):
    verse_labels = re.findall(r'[0-9]+:[0-9]+', bible_list[i]) ## Here add [\n]?...[\s]? later
    for j in range(0,len(verse_labels)):
        bible_list[i] = bible_list[i].replace(verse_labels[j],"",1)
        
        
### Important output variables ###
# text_title -- KJV
# old_testament & new_testament -- testament titles
# books -- list of strings; contains book titles
# bible_list -- list of strings; contains individual book contents
