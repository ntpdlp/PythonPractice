#! /usr/bin/env python3

import time

def elapsed_time(f):
    def wrapper():
        t1 = time.time()
        print("doing another action in f function")
        f() 
        t2 = time.time()
        print(f"Elapsed time for calling function {f}: {t2-t1}")
    return wrapper

@elapsed_time
def f3():
    BIG_NUM = 10000
    list = []
    for x in range(BIG_NUM):
        list.append(x)
    print (list)


def main():
    f3()

if __name__ == "__main__": main()