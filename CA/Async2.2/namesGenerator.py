#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Itertools is useful for generating all names
import itertools
#Random generator for names and things
import random

#Make sure file exists
with open('names/names.txt', 'w') as file:
    pass

#Define all letters in the alphabet
l = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#Array with all three letter combinations
values = itertools.combinations_with_replacement(l, r=3)
#Empty array generation
array = []

#Fill array with values from this, "for" goes through all data in array
for i in values:
    #Append to array with said data
    array.append(''.join(i))

#Iterate through data in array
for i in array:
    #Open file in append mode
    with open('names/names.txt', 'a') as file:
        #Random six letter address
        name = random.choice(l) + random.choice(l) + random.choice(l) \
            + random.choice(l) + random.choice(l) + random.choice(l)
        #Array with data
        final = [i, '0', name]
        #Write to file
        file.write('|'.join(final) + '\n')
        #Close file automagically
			