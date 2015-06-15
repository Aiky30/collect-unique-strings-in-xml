Collect all unique text in an XML file
=============
A Python script to collect all unique strings / terms in an xml file. A script is also included to create a new XML file from any additional columns in the spreadsheet generated by the parsing script.

The scripts included are a work in progress and were originally created and used to assist a client with translations in an XML file that was over 10,000 lines long.

Planned enhancements
-----------
* Input and output files entered via the CLI
* Set column count with a list of column names set via the CLI
* Set the output file type and append the relevant extension to the file

Requirements
-----------
* Python 2.7
* xlwt (Required for initially searching an XML file - parse.py)
* xlrd (Required for creating an XML from a populated XSL file - write.py)

Recommendations
-----------
Install in a Virtual enviroment (http://docs.python-guide.org/en/latest/dev/virtualenvs/)
Use PIP to install dependencies (https://pypi.python.org/pypi/pip)

Configuration of parse.py
-----------
Edit the following lines in "parse.py" to set the source and output files.
```
sourceFile = "[PATH_TO_FILE][FILENAME].xml"; 
outputFile = "[PATH_TO_FILE][FILENAME].xls";
```
Configuration of write.py
-----------
Edit the following lines in "write.py" to set the seed (populated XSL file), source (original XML file used as the input file from parse.py) and output (new none existent file).
```
seed = "[PATH_TO_FILE][FILENAME].xls"
sourceFile = "[PATH_TO_FILE][FILENAME].xml"; 
outputFile = "[PATH_TO_FILE][FILENAME].xml";
```

Usage
-----

To run the parsing script, enter into a Bash terminal

'''
[PATH_TO_PYTHON] parse.py
'''

To run the generating script, enter into a Bash terminal

'''
[PATH_TO_PYTHON] write.py
'''
