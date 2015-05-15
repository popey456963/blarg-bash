#!/usr/bin/python3
# -*- coding: utf-8 -*-
import itertools
import random

with open('names/names.txt', 'w') as file:
    pass

l = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
values = itertools.combinations_with_replacement(l, r=3)
array = []

for i in values:
    array.append(''.join(i))

for i in array:
    with open('names/names.txt', 'a') as file:
        name = random.choice(l) + random.choice(l) + random.choice(l) \
            + random.choice(l) + random.choice(l) + random.choice(l)
        final = [i, '0', name]
        file.write('|'.join(final) + '\n')

			