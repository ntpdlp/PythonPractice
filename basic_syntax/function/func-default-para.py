#! /usr/bin/env python3

def fibo(n=30):
    print (f"Fibonacci to {n}")
    f0 , f1 = 0 , 1
    while f0 < n:
        print (f0, end=' ', flush=True)
        f = f0 + f1
        f0 = f1
        f1 = f
    print ("\n")

def main():
    fibo(100)
    fibo()      #will use defaut val=30

main()


