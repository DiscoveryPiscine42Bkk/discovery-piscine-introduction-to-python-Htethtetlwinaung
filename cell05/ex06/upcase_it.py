#!/usr/bin/env python3
import sys
def main():
    if len(sys.argv) == 2: 
        print(sys.argv[1].upper())
        print("\n")
    else:
        print("none\n")
if __name__ == "__main__":
    main()
#chmod +x upcase_it.py