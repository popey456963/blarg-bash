#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
from operator import itemgetter

folder = './wrong/'
files = os.listdir(folder)

for items in range(len(files)):

    print 'Opened ' + files[items]

    with open(folder + files[items]) as file:
        for line in file:
            lines = line.split('|')

    lines.sort(key=itemgetter(1))

    with open(folder + files[items], 'w') as file:
        for line in lines:
            file.write('{0}'.format('|'.join(line)))