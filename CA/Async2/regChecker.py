#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re
def registration(registration):
    m = re.match('[a-zA-Z]{2}[0-9]{2}[a-zA-Z]{3}', registration)
    if m: 
        return "True"
    else: 
        return "False" # Incorrect Registration