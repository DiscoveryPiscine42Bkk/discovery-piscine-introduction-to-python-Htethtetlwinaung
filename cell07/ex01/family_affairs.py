#!/usr/bin/env python3
def find_the_redheads(family):
    redheads = []
    for name in family:
        if family[name] == "red":
            redheads.append(name)
    return redheads

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}

print(find_the_redheads(dupont_family))

#chmod +x your_namebook.py