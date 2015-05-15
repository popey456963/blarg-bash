import matplotlib.pyplot as plt
from random import randint
dice = int(input("Enter Number of Die"))
round = 0
deaths = []
while dice > 1:
    deathtemp = 0
    round = round + 1
    for i in xrange(dice):
        rand = randint(1,6)
        if rand == 6:
            #print "Dice " + str(i) + " died on round " + str(round)
            dice = dice - 1
            deathtemp = deathtemp + 1
    deaths.append(deathtemp)
print deaths
print "It took " + str(round) + " rounds for all the particles to die!"
with open("results.csv", "a") as myfile:
    myfile.write("appended text")
plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.show()
