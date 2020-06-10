#! /usr/bin/env python3

def fibo(n):
    print (f"Fibonacci to {n}")
    f0 , f1 = 0 , 1
    while f0 < n:
        print (f0, end=' ')
        f = f0 + f1
        f0 = f1
        f1 = f

def main():
    fibo(100)

main()


