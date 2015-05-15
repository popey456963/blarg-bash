#Import things
import os
import sys

#Test for folder existance
def testFolder(directory, name):
    if not os.path.exists(directory):
        #Create the directory
        os.makedirs(directory)
        #Return values
        return("Checking " + name + " ................. False")
    else:
        return("Checking " + name + " .................. True")

#Test for file existance
def testFile(directory, name):
    if not os.path.exists(directory):
        return("Checking " + name + " ................... False")
    else:
        return("Checking " + name + " .................... True")

#Test for correct args
def testargs(args):
    #2 - one for first arg, one for second arg.  Second arg is actual number
    if len(args) == 2:
        return("Testing Args ........................... True")
    else:
        return("Testing Args .......................... False")

#Test whether file exists
fileExists = testFile("./names/names.txt", "Names File")
#Test the args
args = testargs(sys.argv)
#Print things
print("==============Testing Initiated==============")
print(testFolder("./names", "Names Folder"))
print(testFolder("./wrong", "Wrong Folder"))
print(fileExists)
print(args)
print("==============Testing Finished===============")
#Tell user what was wrong
if args == "Testing Args .......................... False":
    carryon = False
    print("No Arguments were given!  Stopping D:")
    print("Example usage is `python3 0server.py 1000000`")
#File dosen't exist!
#Generate it!
if fileExists == "Checking Names File ................... False":
    from namesGenerator import *
