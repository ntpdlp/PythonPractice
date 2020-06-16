#############################################
## in Python: constructor function => __init__
## property : use **kwargs (dict)
#############################################
class Duck:
    def __init__(self,**kwargs):
        self._sound = kwargs['sound'] if 'sound' in kwargs else "chipchipchip"
        self._name = kwargs['name'] if 'name' in kwargs else "Alice"
        self._age = kwargs['age'] if 'age' in kwargs else "1"

    def sound(self,sound = None):
        if sound: self._sound = sound
        return self._sound   
    def name(self,name = None):
        if name: self._name = name
        return self._name
    def age(self,age = None):
        if age: self._age = age
        return self._age
    def printDuck(self):
        if not isinstance(self,Duck):
            raise TypeError("requires Duck object.")
        else:
            print (f"I am {self.name()} {self.age()} month-old, says {self.sound()}")
       

def main():
    # sound,name,age : belongs to object 
    # we call : encapsulation
    duck1 = Duck(sound="quakquak",name="duck1",age=5)
    duck2 = Duck(sound="capcap",name="duck2",age=7)
    duck3 = Duck(sound="roprop",name="duck3")
    duck4 = Duck(name="duck4")
    duck5 = Duck()

    duck3.sound("gowgowgowgow")
    duck4.age(20)

    ducks = []
    ducks.append(duck1)
    ducks.append(duck2)
    ducks.append(duck3) #sound is set gowgowgowgow
    ducks.append(duck4) #age is set
    ducks.append(duck5)

    for x in ducks: x.printDuck()


if __name__ == "__main__":main()