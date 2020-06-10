#! /usr/bin/env python3

def condition_equal_operator():
    name = "python"
    if name=="python":
        print ("python course")
    else:
        print ("no print")    


def comparision_6_operator():
    a,b = 5,17
    if a == b: print (f"{a} == {b}")        
    elif a != b: print (f"{a} != {b}")
    elif a < b: print (f"{a} < {b}")
    elif a > b: print (f"{a} > {b}")
    elif a <= b: print (f"{a} <= {b}")
    elif a >= b: print (f"{a} >= {b}")
    else: print ("comparison operators done!")


def main():
    condition_equal_operator()
    comparision_6_operator()

if __name__ == "__main__": main()