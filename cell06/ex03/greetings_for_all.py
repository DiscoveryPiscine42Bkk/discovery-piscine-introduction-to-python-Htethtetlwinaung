#!/usr/bin/env python3
def greetings(name="noble stranger"):
    if type(name) != str:
        print("Error! It was not a name.")
    else:
        print(f"Hello, {name}")
    
greetings("Alexandra")
greetings("Wil")
greetings()
greetings(42)
#chmod +x grettings_for_all.py