#! /usr/bin/env python3

def f1():
    print("iam f1 function")

# in Python, everything is object. We can assign 
def main():
    x = f1
    x()

if __name__ == "__main__": main()