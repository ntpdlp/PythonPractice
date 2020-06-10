#! /usr/bin/env python3

x = 5
y = 15

if x < y :
    print (f"{x} smaller than {y}")
    z = 60
else:
    print (f"{x} larger than {y}")


def main():
    w = 79
    print ("main function here haha ...")

#in Python, Block is defined by indention
#but indention doesn't define scope.  Only def function can define its scope
print (f"we can get z : {z}") #block, just indention
print (f"we can not get w : {w}") #inside defined function
