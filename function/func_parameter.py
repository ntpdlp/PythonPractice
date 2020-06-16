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

#*args => list parameter
def func_args_parameter(*args):
    if len(args)>0:
        for x in args:
            print (f"{x} ",end=' ')
    print("\n")

#**kwargs => keyword arguments
def func_kwargs_parameter(**kwargs):
    if len(kwargs):
        for k in kwargs:
            print ("{} : {}".format(k,kwargs[k]), end=' , ')

def main():
    fibo(100)
    fibo()      #will use defaut val=30
    # *args : list
    func_args_parameter ("orange","banana")
    func_args_parameter (3,5,7)
    # **kwargs : dict
    testcase_informration = dict(Browser = "Chrome", TC_Name = "TC_Login", Testsuite = "Login")
    func_kwargs_parameter(**testcase_informration)

main()


