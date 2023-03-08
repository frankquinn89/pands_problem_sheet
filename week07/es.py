# es.py
# This program takes an input of a text file as a command line argument.
# It reads the text file and outputs the number of e's it contains. I am counting both big E snd small e.
# Author : Frank Quinn

# importing sys package
import sys

# Using sys.argv[1] as sys.argv[0] is the first argument which is the name of .py file
# The .txt file must be located in the same directory as es.py
filename = sys.argv[1]

# Validate it is a .txt file
if filename.endswith(".txt"):
    with open(filename, 'r') as f:
        es = f.read()
        # count small "e" character 
        countSmall = es.count("e")
        # count big E
        countBig = es.count("E")
        # Total e/E 
        total = countSmall + countBig
        print (f"The total amount of e/E in {filename} is {total}")
else:
    # Let user know they have incorrect file type
    print("invalid file type, must be a .txt file")