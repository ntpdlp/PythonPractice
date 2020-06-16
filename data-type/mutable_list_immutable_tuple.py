#! /usr/bin/env python3

def immutable_list(list):
    def print_list(list):
        for x in list:
            print(f"{x} ",end=' ')
        print("\n")
    
    print_list(list)
    list_size = len(list)
    list[list_size-1] = "newfruit";
    print_list(list)


def main():
    fruits = ["apple","mango","grape","avocado","watermelon"]
    print(fruits[1])
    print(fruits[1:3]) #inclusive 1, exclusive 3 => 2 items ([1],[2])
    fruits.append("peach")
    fruits.remove(fruits[0])
    print(" -> ".join(fruits))
    immutable_list(fruits)

    ## set() same list[] but set can't change data after creation
    setInterface = ("RS232-STD","RS232-WN","USBOEM","USBKB")
    print("; ".join(setInterface))
    print(setInterface[0])



if __name__ == "__main__": main()