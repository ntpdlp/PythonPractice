#! /usr/bin/env python3

def isPrime(n):
    if n <= 1:
        return False
    for i in range (2,n):
        if n % i == 0:
            return False
    return True

def list_prime(n=10):
    for i in range(n):
        if isPrime(i):
            print(f"{i}",end=' ')

list_prime(20)
print ("\n")
list_prime()