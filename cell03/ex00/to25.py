#!/usr/bin/env python3
number = int(input("Enter a number less than 25 : "))
if number >25:
    print("Error")
else:
    for i in range(number, 26):
        print("Inside the loop, my variable is ", i)
#chmod +x to25.py   