#Collatz
def collatzlen(y):
    length = 0
    while(True):
        if y == 1:
            return length + 1
        elif y % 2 == 0:
            #number is even
            y = y / 2
            length = length + 1
        else:
            #number is odd
            y = 3 * y + 1
            length = length + 1
array = []
for i in range(1000000):
    array.append(collatzlen(i+1))
    print(i)
print(array)
a = max(array)
print([i for i, j in enumerate(array) if j == a])
