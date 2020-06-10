
#! /usr/bin/env python3

def defalt_bool_inPython(n):
    if n:
        print (f"{n} is default True")
    else:
        print (f"{n} is default False")

def main():
    #False
    defalt_bool_inPython(0)
    defalt_bool_inPython("")
    defalt_bool_inPython(None)
    
    #True
    defalt_bool_inPython(5)
    defalt_bool_inPython("nonemptystring")
    


if __name__ == "__main__": main()