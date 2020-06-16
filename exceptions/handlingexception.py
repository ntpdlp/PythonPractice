#! /usr/bin/env python3

import sys

def valueerror():
    try:
        num = int('foo')
    except ValueError:
        print ("invalid syntax")

def division_by_zero():
    try:
        num = 5/0
    except ValueError:
        print ("Value Error")
    except ZeroDivisionError:
        print ("division by zero")
    else:
        print ("good")

def unknow_error():
    try:
        num = 5/0
    except:
        print(f"{sys.exc_info()}")
    else:
        print("good")

def main():
    valueerror()
    division_by_zero()
    unknow_error()

if __name__ == "__main__":main()