#! /usr/bin/env python3

#####################################################
## in Python: constructor function => __init__
## property: _sound : private scope property 'sound'
#####################################################

class Duck:
    def __init__(self,sound,name,age):
        self._sound = sound
        self._name = name
        self._age = age

    def getSound(self):
        return self._sound   
    def getName(self):
        return self._name
    def getAge(self):
        return self._age
    def printDuck(self):
        if not isinstance(self,Duck):
            raise TypeError("requires Duck object.")
        else:
            print (f"I am {self.getName()} {self.getAge()} month-old, says {self.getSound()}")
       

def main():
    duck1 = Duck("quakquak","duck1",5)
    print (duck1.getName())
    duck1.printDuck()

    duck2 = Duck("capcap","duck2",7)
    print (duck2.getName())
    duck2.printDuck()



if __name__ == "__main__":main()