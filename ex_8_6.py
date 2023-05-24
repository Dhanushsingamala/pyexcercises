#!/usr/bin/env python
"""find all numbers in a string"""
import re

r = r"\((\d+)\)=([^,]+)"
c = re.compile(r)
s = "an array: (1)=3.9836, (2)=4.3E-09, (3)=8766, (4)=.549"
matches = c.findall(s)

# make dictionary a, where a[1]=3.9836 and so on:
a = {}
for match in matches:
    key = match[0]
    value = match[1]
    a[key] = value

sorted_keys = sorted(a.keys(), key=int)
for key in sorted_keys:
    print(f"[{key}]={a[key]}")
