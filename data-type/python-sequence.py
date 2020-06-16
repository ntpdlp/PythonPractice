#! /usr/bin/env python3

#mutable: able to reassignment
def python_mutable_array_list():
    myarr = [1,2,3,4,5]
    myarr[0] = 100
    for x in myarr:
        print (f"{x} ",end=" ", flush=True)
    print("\n")

    print(f"Sum of list is: {sum(myarr)}")
    print(f"Sum of list start with +100 is: {sum(myarr,100)}")
    print(f"Max, Min in list is: {max(myarr)}, {min(myarr)}")

def python_mutable_dict():
    mydict = {'one':1, 'two':2, 'three':3}
    mydict['two'] = 5
    for k,v in mydict.items():
        print (f"<{k}:{v}> ", end="\t")

def python_mutable_dict2():
    mydic = dict(one=1,two=2,three=3)
    for k in mydic:
        print("<{} : {}>".format(k,mydic[k]),end="\t")    

#immutable: not allow to reassignment
def python_immutable_tuple():
    mytuple = (1,2,3,4,5)
    for x in mytuple:
        print (f"{x} ", end=' ')
    return mytuple

def python_immutable_range():
    for x in range(5):
        print (f"{x} ",end=' ')
    
    for y in range (10,15):
        print (f"{y} ", end=' ')

    for z in range (100,150,10):
        print (f"{z} ",end='')



def mutable_immutable():
    #mutable
    print ("\nArray|List", end=': ')
    python_mutable_array_list()
    print ("\nDictionary", end=': ')
    python_mutable_dict()
    python_mutable_dict2()

    #immutable
    print ("\nImmutable Tuple", end=': ')
    mytuple = python_immutable_tuple()
    print ("\nImmutable Range", end=': ')
    python_immutable_range()
    # #TypeError: 'tuple' object does not support item assignment
    # print (mytuple[0])
    # mytuple[0] = 500

def sequence_is_object_type_in_python():
    x = (1,"apple",5.0,[1,2,3],"orange")
    y = x # object y will have same address with object x
    z = ("everything in python","is", "object")
    w = ("everything in python","is", "object") # object w will have same address with object z
    print (f"type() function: x is {type(x)}, y is {type(y)}")
    print (f"id() of these tuples: x is {id(x)} & y is {id(y)}, z is {id(z)} & w is {id(w)}")
    print (f"id() of items in tuples: x[0] is {id(x[0])}, y is {id(y[0])}")
    

def main():
    python_mutable_array_list()
    # mutable_immutable()
    # sequence_is_object_type_in_python()




if __name__ == "__main__":main()