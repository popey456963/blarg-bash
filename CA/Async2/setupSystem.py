import os
def testFolder(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        return("Checking Names Folder ................. False")
    else:
        return("Checking Names Folder .................. True")
def testFolder2(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        return("Checking Wrong Folder ................. False")
    else:
        return("Checking Wrong Folder .................. True")
def testFile(directory):
    if not os.path.exists(directory):
        return("Checking Names File ................... False")
    else:
        return("Checking Names File .................... True")
        