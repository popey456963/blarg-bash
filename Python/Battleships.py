import numpy as np
n = (100,100)
a,b,c,d = 1132340,213,313450,401345
array = [1,1,2,2,3,4]
board = np.zeros(n, dtype=np.int)

for i in range(array):
    place(array[i])
    

def place(size):
    temp1 = (a*b+c)%d #X coord
    b = (a*b+c)%d
    temp2 = (a*b+c)%d #Y coord
    b = (a*b+c)%d
    temp3 = (a*b+c)%d #Direction
    b = (a*b+c)%d
    if temp3 % 2 == 0:
        #Number is even - place horizonatally
        for f in range(size):
        
        
    print(b)
print(board)