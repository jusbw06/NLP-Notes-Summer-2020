# Document Adherence to Guidelines (MS Dataset) -- Important Tools

**Text Documents:**  
`re`: This package allows the parsing of text for specific user-defined text-patterns. This pacakge is necessary for checking a MS document's adherence to certain TR-50 rules.
Please see [w3schools](https://www.w3schools.com/python/python_regex.asp "RegEx")
or [python.org](https://docs.python.org/3/library/re.html "re") for documentation.


**Word Documents(.docx):**  
`python-docx`: This package allows for the creating and editing of word documents. However, this package does not always detect fonts or formats when reading documents saved from Microsoft Word. This makes it problematic for use in checking for document adherence to TR-50 format-related rules.
Please see [python-docx](https://python-docx.readthedocs.io/en/latest/index.html) for full documentation

**PDF Documents:**  
`pdf-utils`: Library for processing pdf files in python. Includes libraries such as [`Tessaract`](https://tesseract-ocr.github.io/tessdoc/Home.html "Tessaract Homepage") and [`OpenCV`](https://opencv.org/ "OpenCV Homepage") for machine learning appplications.  
`pypdf2`: Basic python toolkit for working with pdf documents.  
`python-poppler`: Python toolkit for working with pdf documents on Linux. This package binds to the C/C++ package below. It is very useful for manipulating documents at the textual level.  
`poppler`: C/C++ library for creating, reading, and manipulating pdf documents on Linux. I recommend using the C++ package, documentation [here](https://poppler.freedesktop.org/api/cpp/). Download this package though your OS package manager: `apt-get`, `pacman`, `rpm`, etc.  

**Note:**  
Please find all python packages at the Python Package Index -- [pypi.org](https://pypi.org/ "https://pypi.org/")
