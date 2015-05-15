import os.path
def csvwriter(data, pathvi):
    path = pathvi + data[1][0] + ".txt"
    fileexists = os.path.isfile("./wrong/" + path) 
    if not fileexists:
        with open(path, "a") as file:
            file.write("No.|Registration|Time|Distance|Speedlimit|Name|AvgSpeed|IsSpeeding|Registration|EOL\n")
            
    with open("./wrong/" + path, "a") as file:
        #myfile.write(str(data))
        for i in range(len(data)):
            file.write(data[i] + "|")
        file.write("EOL\n")