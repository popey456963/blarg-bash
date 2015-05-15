with open("data.txt") as f:
    content = f.readlines()
total = 0
for i in content:
    temp = int(i)
    total = total + temp
print(total)
    