#! /usr/bin/env python3

def for_loop():
    arr = [1,2,3,4,5,6,"One","Two"]
    # for loop
    for i in arr:
        print (f"{i}", end=' ')
    print("\n")

    for x in range(10):
        print(f"{x}",end=' ')
    print("\n")

#for: continue
def for_continue():
    for y in range(50,58):
        if y == 55: continue
        else:
            print(f"{y}",end=' ')


#while
def while_loop():
    n=0
    while n<len(arr):
        print (f"{arr[n]}", end=' ')
        n = n+1
        pass
    print("\n")    

#while: break
def while_break():
    yourpassword = "password"
    yourinput = ""
    try_time = 0
    while yourinput != yourpassword:
        yourinput = input("enter your password: ")
        try_time = try_time + 1
        if try_time == 3: break

def main():
    # for_loop()
    # for_continue()
    # while_loop()
    while_break()

if __name__ == "__main__": main()