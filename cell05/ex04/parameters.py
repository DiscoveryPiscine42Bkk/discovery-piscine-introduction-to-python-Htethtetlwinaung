#!/usr/bin/env python3
import sys
def main():
    count = len(sys.argv) - 1  # Exclude script name
    print(f"Number of parameters: {count}.")
if __name__ == "__main__":
    main()
#chmod +x parameters.py