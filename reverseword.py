string = "Test String".split(" ")
reverse = ""
for j in range(len(string)):
    x = []
    for i in range(len(string[j])):
        x.insert(0,string[j][i])
    reverse = reverse + " " + "".join(x)
    print(reverse)