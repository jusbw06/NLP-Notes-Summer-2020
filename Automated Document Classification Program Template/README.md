# NLTK Classifier Template

The purpose of this program is to provide a modular, straight-forward outline for implementing a document classification tool in Python. This was made with the intention of being able to have interchangeable methods & algorithms.

It is designed to be used as a command-line tool where the programmer can switch between ML/NLP comparison & classification tools via command line. This will allows the programmer to better compare the varying effectivenesses of the different tools and methods used.

*Note*: The project has moved to a new route, prioritizing transformer-based models. This template has not been updated to reflect the changes.

**Files & Folders:**  
`main.py`: This module handles the comand line argument parsing and the initial setup of the program via the `SETTINGS` module.  
`SETTINGS.py`: This modules acts as a "global variables" workspace. All information regarding the configuration of the flow of the program is stored in this module. This module allows the program to remain modular, allowing the insertion and deletion of methods and algorithms into the program without affect any of the code in the other files.  
`classifier.py`: This module is a intermediary between `main.py` and the actual classification tasks. It handles the reading of data, forwarding the data to the selected model, and printing the results.  
`Document/Document.py`: This module allows each text document to be encoded as a python object before undergoing analysis. This allows document analysis methods to be included as part of a document's class definitions. Child classes are defined to provide particular class types distinct functionalities such as specific document similarity functions.  
`KNN & NN`: These folders represent predetermined document classification models taht have not been implemented yet. Each model's main module contains the class called `Classifier` and certain predetermined methods to ensure easy insertion into the larger code and modularity with the rest of the program.  
`TestScripts`: TestCases for the above scripts.
