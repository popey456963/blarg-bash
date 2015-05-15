import os
def testFolder(directory, name):
    if not os.path.exists(directory):
        os.makedirs(directory)
        return("Checking " + name + " ................. False")
    else:
        return("Checking " + name + " .................. True")
def testFile(directory):
    if not os.path.exists(directory, name):
        return("Checking " + name + " ................... False")
    else:
        return("Checking " + name + " .................... True")
        