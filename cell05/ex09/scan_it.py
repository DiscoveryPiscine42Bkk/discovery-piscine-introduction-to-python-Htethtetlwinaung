#!/usr/bin/env python3
import sys
def main():
    if len(sys.argv) != 3: 
        print("none\n")
        return
    
    first = sys.argv[1]
    second = sys.argv[2]

    words = second.split()
    count = words.count(first)

    if count > 0:
        print(count)
        print("\n")
    else:
        print("none\n") 
  
if __name__ == "__main__":
    main()
#chmod +x scan_it.py 