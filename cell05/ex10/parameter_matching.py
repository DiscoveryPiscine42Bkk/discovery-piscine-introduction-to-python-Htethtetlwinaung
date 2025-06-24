#!/usr/bin/env python3
import sys
def main():
    if len(sys.argv) != 2:
        print("none\n")
        return
    
    param = sys.argv[1]
    user_input = input("What was the parameter?")

    if user_input == param:
        print("Good job!\n")
    else:
        print("Nope, sorry...\n")
 
if __name__ == "__main__":
    main()
#chmod +x parameter_matching.py 