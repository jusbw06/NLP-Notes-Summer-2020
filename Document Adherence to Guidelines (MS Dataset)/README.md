# MS Dataset -- Important Tools

**Text Documents:**  
`re`: allows parsing of text for specific text-patterns that may be necessary for certain TR-50 rules.
Please see [w3schools](https://www.w3schools.com/python/python_regex.asp "RegEx")
or [python.org](https://docs.python.org/3/library/re.html "re") for documentation.


**Word Documents(.docx):**  
`python-docx`: allow the creation and editing of word documents. However, does not allow font/format checking in all cases.
Please see [python-docx](https://python-docx.readthedocs.io/en/latest/index.html) for full documentation

**PDF Documents:**  
`pdf-utils`: Library for processing pdf files in python. Includes libraries such as [`Tessaract`](https://tesseract-ocr.github.io/tessdoc/Home.html "Tessaract Homepage") and [`OpenCV`](https://opencv.org/ "OpenCV Homepage") for machine learning appplications.  
`pypdf2`: Basic python toolkit for working with pdf documents  
`python-poppler`: Python toolkit for working with pdf documents on Linux. Binding to the C/C++ package below. Very useful for manipulating documents at the textual level.  
`poppler`: C/C++ library for creating, reading, and manipulating pdf documents on Linux. I recommend using the C++ package, documentation [here](https://poppler.freedesktop.org/api/cpp/). Download this package though your OS package manager: `apt-get`, `pacman`, `rpm`, etc.  

**Note:**  
Please find all python packages at the Python Package Index -- [pypi.org](https://pypi.org/ "https://pypi.org/")
