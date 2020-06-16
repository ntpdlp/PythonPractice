#! /usr/bin/env python3

################################################
#built-in string class: str 
#class 'MyString' extend from class 'str'
################################################
class MyInverseString(str):
    def __str__(self):
        return self[::-1]

def use_userclass_print_inverse_str():
    a = MyInverseString("helloworld")
    print(a)


def format_string():
    print("hello".upper())
    print("hello".capitalize())

    #difference: find | in
    print ('py' in 'python') # True|False
    print ("python".find("th")) # index if found | -1 if not found
    print ("python".find("smart")) # index if found | -1 if not found

    a = 4 * 4000 * 70000
    b = 1.333 * 9.56
    c, d = 5 , 111999
    print ("{:,}".format(a))
    print (f"{a:,}")
    print ("{:.3f}".format(b))
    print (f"{b:.3f}")
    print ("{:>08} , {:>10}".format(c,d))  # leading by 0 
    print (f"{c:>08} , {d:>10}")

    y = 64
    print ("{}".format(y))
    print ("{:x}0x".format(y))
    print ("{:b}0b".format(y))

    
def func_split_join():
    str = "python is a scripting language with OOP support"
    split_list = str.split()
    print(split_list)
    print(" -- ".join(split_list))

class MyStringPrintStyle:
    def __init__(self, mystr):
        self._mystr = mystr

    def __repr__(self):
        return "repr() func , my override repr: " + self._mystr

    def __str__(self):
        return "str() function, my override str: " + self._mystr

def main():
    # use_userclass_print_inverse_str()
    # format_string()
    # func_split_join()

    customString = MyStringPrintStyle("I love Python")
    print(customString)
    print(repr(customString))

if __name__ == "__main__": main()

