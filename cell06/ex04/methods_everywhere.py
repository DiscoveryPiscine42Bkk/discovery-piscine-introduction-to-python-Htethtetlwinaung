#!/usr/bin/env python3
import sys
def shrink(input_string):
    print(input_string[:8])

def enlarge(input_string):
    print(input_string + (8 - len(input_string)) * 'Z')

if len(sys.argv) == 1:
    print("none")
else:
    for arg in sys.argv[1:]:
        if len(arg) < 8:
            enlarge(arg)
        elif len(arg) > 8:
            shrink(arg)
        else:
            print(arg)

#chmod +x methods_everywhere.py