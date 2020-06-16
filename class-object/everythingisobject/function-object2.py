#! /usr/bin/env python3

def f1(f):
    def f2():
        print("iam f2, before calling another f",end="\n")
        f()
        print("iam f2, after calling another f",end="\n")
    return f2(); #return a function == return an object


def f3():
    print ("iam f3",end="\n")

# in Python, everything is object. We can assign a function as parameter into another function
def main():
    f1(f3)

if __name__ == "__main__": main()