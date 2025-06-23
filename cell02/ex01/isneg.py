#!/usr/bin/env python3
number = input("Enter a number : ")
if int(number) > 0: 
    print("This number is positive.")
elif int(number) < 0:
    print("This number is negative.")
elif int(number) == 0:
    print("This number is both positive and negative.")
#chmod +x isneg.py