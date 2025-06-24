#!/usr/bin/env python3
import sys

user = sys.argv[1]
not_z = True
for c in user:
    if c == "z":
        print("z", end="") 
        not_z = False
if not_z:
    print("none\n")
#chmod +x string_are_arrays.py