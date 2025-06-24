#!/usr/bin/env python3
import sys
def main():
    if len(sys.argv) > 1: 
        print(sys.argv[1])
        print("\n")
    else:
        print("none\n")
if __name__ == "__main__":
    main()
#chmod +x aff_first_param.py