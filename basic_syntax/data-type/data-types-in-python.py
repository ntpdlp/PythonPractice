#! /usr/bin/env python3

class Person:
    def eat(self):
        print ("eat")
    def sleep(self):
        print ("sleep")


def input_type(n):
    type_n = type(n)
    print (f"{n} {type_n}", end="\n",flush=True)


def main():
    #built-in data-type 
    input_type(7)
    input_type(7.0)
    input_type("seven")
    input_type(None)
    input_type(True)
    input_type(False)
    #user defined class data-type
    phuong = Person()
    input_type(phuong)

    a,b,c = 11,55,99
    print (f"{a} , {b}", end='\n')
    print ("{0} , {1}".format(a,b))
    print ("{2} , {1} , {0}".format(a,b,c)) #invert customize
    print ("{2} , {0} , {1}".format(a,b,c)) #invert customize
    print (f"{a<9}  {b<9} ") #False False
    print (f"{a:<9}  {b:<9} ") # :< left    11        55   
    print (f"{a:>09}  {b:>09} ") # :> right, preceding by Zero 0
    

if __name__ == "__main__": main()    


