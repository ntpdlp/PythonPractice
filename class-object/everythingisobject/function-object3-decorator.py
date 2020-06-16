#! /usr/bin/env python3

def f1(f):
    def f2():
        print("iam f2, before calling another f",end="\n")
        f()
        print("iam f2, after calling another f",end="\n")
    return f2 #return a function == return an object


#f1 is decorator: f3 is the argument input for f1 
@f1
def f3():
    print ("iam f3",end="\n")


def main():
    f3()

if __name__ == "__main__": main()