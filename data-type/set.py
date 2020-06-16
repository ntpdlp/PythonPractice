
#! /usr/bin/env python3

def main():
    a = set("there is always a way")
    b = set("i love what i am doing and i commit to go to the last phase")
    print_set(sorted(a))
    print_set(sorted(b))
    print_set( a | b)
    print_set( a & b)

def print_set(myset):
    for x in myset:
        print(x,end=' ')
    print("\n")

if __name__ == "__main__": main()