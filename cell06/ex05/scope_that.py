#!/usr/bin/env python3
def add_one(param):
    param += 1
    return param

def main():
    variable = 5
    print("Before calling method: ", variable)

    add_one(variable)
    print("After calling method: ", variable)

if __name__ == "__main__":
    main()
#chmod +x scope_that.py

#Observation : The value of the variable in the main function does not change after calling the add_one function. 
# This is because integers are immutable in Python, and the function creates a new local variable `param` that does not 
# affect the original `variable` in the main function.