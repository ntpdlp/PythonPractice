#! /usr/bin/env python3

def main():
    mydict1 = dict(one=1,two=2,three=3)
    print_dict(mydict1)
    print(mydict1['one'])
    mydict1['one']=100  #dict: mutable
    print_dict(mydict1)

    animals = {'monkey':10, 'pig':12, 'dragon':14}
    for k,v in animals.items():
        print(f"{k} : {v}")

    print("found!" if "dragon" in animals else "not here!")
    print("found!" if "kahalaba" in animals else "not here!")

    # Problem: if animals['kahalaba'] >> exceptions for dont exist
    # Solution: get >> None if not exists
    print(animals.get("kahalaba"))

    #############################################
    ## ERROR mydict3 ? why?
    ## Expected: key must be "immutable" data type like "string" type. 
    ## Observed: key in int can be changed
    #############################################
    # mydict3 = {1:"one",2:"two",3:"three"}
    # print_dict(mydict3)

def print_dict(dictdata):
    for x in dictdata: print(f"{x}: {dictdata[x]}",end=' ',flush=True)
    print("")

if __name__ == "__main__":main()

        