#!/usr/bin/env python3
import sys
def main():
    if len(sys.argv) < 3: 
        print("none\n")
    else:
        for param in reversed(sys.argv[1:]):
            print(param)
        print("\n")
if __name__ == "__main__":
    main()
#chmod +x aff_rev_params.py 