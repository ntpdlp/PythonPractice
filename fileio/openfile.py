#! /usr/bin/env python3

import os

def main():
    pwd = os.path.dirname(os.getcwd())
    print(pwd)
    f = open(pwd + "/fileio/textsample.txt","rt") #read text
    # 2 kinds of files (text|t) or (binary|b)
    # 2 actions read|r , write|w 
    # => combination we have 4 types: rt, rb, wt, wb
    for line in f:
        print(line)

if __name__ == "__main__": main()