#! /usr/bin/env python3

from decimal import *

def deal_with_decimal():
    x, y, z = 1.1 , 1.1 , 2.2
    print ("{} + {} = {} is {}".format(x,y,z,x+y==z))

    a, b, c = .1 , .1 , .2
    print ("{} + {} = {} is {}".format(a,b,c,a+b==c))

    j, k = Decimal('.15'), Decimal('.16')
    print ("{} + {} = {}".format(j,k,j+k))



def main():
    a,b=17,5
    print (" {} + {} = {}".format(a,b,a+b))
    print (" {} - {} = {}".format(a,b,a-b))
    print (" {} * {} = {}".format(a,b,a*b))
    print (" {} / {} = {}".format(a,b,a/b))
    print (" {} // {} = {}".format(a,b,a//b))
    print (" {} % {} = {}".format(a,b,a%b))


if __name__ == "__main__": 
    main()
    deal_with_decimal()