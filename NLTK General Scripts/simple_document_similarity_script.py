#!/bin/python3

from kjv_preprocess import bible_list, books, text_title
from nltk_tools import *


## Add word subtraction, [personally not a fan] -- subtracts important words like Israel and king
## Find all most common words in bible and subtract from following sets
# bible_complete = Document('\n'.join(bible_list), text_title)
# bible_stopwords = bible_complete.return_most_common()
# bible_stopwords = [e[0] for e in bible_stopwords]
bible_stopwords = []

# doc_obj = Document(contents of book<string>, title of book<string>)
genesis = Document(bible_list[0], books[0])
exodus = Document(bible_list[1], books[1])


similarity = genesis.compare(exodus)
print('Texts are ', similarity, ' percent similar' )
