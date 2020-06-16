#! /usr/bin/env python3

def main():
    print ('foofoofoo',end="\n",flush=True)
    list = range(1,10,2)
    list1 = [x*2 for x in list] #generate a new list
    list2 = [x for x in list if x%2 != 0] #generate a new list
    list3 = [(x,x**2) for x in list if x%3 == 1] #generate a new tuple 
    list4 = {x : x*2 for x in list} #generate dict
    print_list(list)
    print_list(list1)
    print_list(list2)
    print_tuple(list3)
    print(list4)

def print_list(list):
    for x in list: print (f"{x:<8} ",end=' ')
    print ("")

def print_tuple(tuple):
    for x in tuple: print (f"{x}", end=' ')
    print ("\n")

if __name__ == "__main__": 
    main()