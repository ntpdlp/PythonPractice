#! /usr/bin/env python3

import platform

def printHello(username):
    print ("Welcome {} to Python ".format(username))

print ("where should it be printed ?")

def printPythonVersionUsing():
    platformverson =  platform.python_version()
    print ("You are using Python platform version: {}".format(platformverson))

def main(): #just wrap 2 function, so the line #8 will be executed before
    printHello("PhuongNguyen")
    printPythonVersionUsing()
    
if __name__ == "__main__": main()