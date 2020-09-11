# NLTK Python Scripts

These python scripts were created after reading the [NLTK book](https://www.nltk.org/book/ "NLTK book") as a means to practice using the toolkit.


**Scripts:**  
`simple_document_similarity_script.py`: This script imports the KJV Bible then performs a simple document comparison using the cosine similarity method between Genesis and Exodus.  
`bible_comparison_matrix`: This script imports the `kjv_preprocess` module then computes document simularity comparisons between every book of the Bible, creating a 66x66 comparison matrix. In order to save memory, a limiter function is present to plot on ones specified by the user. Please see `gospel_similarity_matrix` for an example.  
`tagger_script.py`: This script implements a simple python-nltk word tagger. It opens a specified file, then prints the tagged contents.


**Helper Modules:**  
`kjv_preprocess.py`: This module is responsible for downloading the KJV Bible from the Gutenberg corpus and applying the necessary preprocessing techniques for doucment analysis. This module splits the text into its individual books and extracts its titles. Simply do `from kjv_preprocess import books, bible_list` to import a list of the book names in `books` and their respective contents in `bible_list`.  
`plotting_tools.py`: This provides the plotting functionality for the comparison matrices
`nltk_tools.py`: This is the most important of the modules. It contains the `Document` class. The `Document` class allows one to represent each text as a python object. Within this module, a cosine similarity document comparison function is implemented and integrated into the class' `compare` function.  

**Other:**  
`print_files_in_directory_script.py`: This script takes a directory path as a command line argument. This script opens that directory, prints the names of its conatined files, then prints the files' contents.  
`print_nonUTF-8_files_in_directory_script.py`: This script does the same as above; however, this script will work on files with non-UTF-8 characters  