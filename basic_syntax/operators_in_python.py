#! /usr/bin/env python3

def comparision_6_operator():
    print ("comparison operators 6: == != > >= < <=")
    a,b = 5,17
    if a == b: print (f"{a} == {b}")        
    elif a != b: print (f"{a} != {b}")
    elif a < b: print (f"{a} < {b}")
    elif a > b: print (f"{a} > {b}")
    elif a <= b: print (f"{a} <= {b}")
    elif a >= b: print (f"{a} >= {b}")
    else: print ("comparison operators done!")

def logic_operator():
    print ("Logic operator 3: and or not << >>")

def member_operator():
    print ("Member operator 2: in, not in  ")

def arithmetic_operator():
    print ("Arithmetic operator : + - * / // % ** ")
    print ("{} ** {} = {}".format(2,3,2**3)) #exponent
    print ("{} // {} = {}".format(7,3,7//3)) #int division
    print ("{} % {} = {}".format(7,3,7%3)) #mod
    print ("{} * {} = {}".format(-7,-2,-7*-2)) #multiple 2 negative

def bitwise_operator():
    print ("& | ^ << >>")
    x, y , t = 0x0a, 0x02, 0x0F
    z = x & y
    u = x | y
    w = x ^ t 
    print (f"(hex &): x is {x:04x}, y is {y:04x}, z is {z:04x}")
    print (f"(bin & ): x is {x:08b}, y is {y:08b}, z is {z:08b}")
    print (f"(bin | ): x is {x:08b}, y is {y:08b}, u is {u:08b}")
    print (f"(bin ^): x is {x:08b}, t is {t:08b}, w is {w:08b}") #invert x

    b = 0x03
    c = x << b
    d = x >> b
    print (f"(bin <<): x is {x:08b}, b is {b:08b}, c is {c:08b}") # shilf left 3 bits
    print (f"(bin >>): x is {x:08b}, b is {b:08b}, d is {d:08b}") # shilf right 3 bits

def boolean_operator():
    print("and, or, not, in, not in, is , not is")
    if True or False:
        print ("always take action")
    mylist = {1,2,3,4,5}
    for x in mylist:
        print (f"{x} ",end=' ')

def main():
    # comparision_6_operator()
    # logic_operator()
    # member_operator()
    # arithmetic_operator()
    # bitwise_operator()
    boolean_operator()

if __name__ == "__main__": main()

# Output: bitwise_operator()
# (hex &): x is 000a, y is 0002, z is 0002
# (bin & ): x is 00001010, y is 00000010, z is 00000010
# (bin | ): x is 00001010, y is 00000010, u is 00001010
# (bin ^): x is 00001010, t is 00001111, w is 00000101
# (bin <<): x is 00001010, b is 00000011, c is 01010000
# (bin >>): x is 00001010, b is 00000011, d is 00000001