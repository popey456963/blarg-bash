def run(string):
    test = eval(string)
    if test == 8841:
        print("Success!")

string2 = list("79*2245-(79*2-7)")
char = list("1234567890*/+-")
string = list("79*2245-(79*2-7)")

def send():
    global string
    global string2
    global char
    for j in range(len(string)):
        for i in range(len(char)):
            string[j] = char[i]
            print(string)
            #test
            string = string2
            pass
        pass
    
print(char)
print(string)
send()