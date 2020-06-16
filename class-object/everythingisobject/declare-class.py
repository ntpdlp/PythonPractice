#! /usr/bin/env python3


class Duck:
    sound = "quack quack"
    name = "Duck Donal"

    def say(self):
        print (self.sound)
    
    def helloiam(self):
        print (self.name)

def myfunc():
    return "this is a function object"

def main():
    #in Python, everything is object. See the way calling function same as the way calling class
    myf = myfunc()
    print(myf)

    duck1 = Duck()
    print("Duck1",end="\r")
    duck1.say()
    duck1.helloiam()
 
    ################################################################
    #what if create another duck2 => its infor as same as duck1. 
    #Problem: We can't change infor for duck2|duck1 ?? how to improve?
    #Solution: provide constructor
    ################################################################
    duck2 = Duck()
    print("Duck2",end="\r")
    duck2.say()
    duck2.helloiam()




if __name__ == "__main__": main()