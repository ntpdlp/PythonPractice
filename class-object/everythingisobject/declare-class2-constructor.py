#############################################
## in Python: constructor function => __init__
## property : use **kwargs (dict)
#############################################
class Duck:
    def __init__(self,**kwargs):
        self._sound = kwargs['sound'] if 'sound' in kwargs else "nosound"
        self._name = kwargs['name'] if 'name' in kwargs else "noname"
        self._age = kwargs['age'] if 'age' in kwargs else 0

    #getter
    def sound(self):
        return self._sound   
    def name(self):
        return self._name
    def age(self):
        return self._age

    def printDuck(self):
        if not isinstance(self,Duck):
            raise TypeError("requires Duck object.")
        else:
            print (f"I am {self.name()} {self.age()} month-old, says {self.sound()}")
       

def main():
    duck1 = Duck(sound="quakquak",name="duck1",age=5)
    duck2 = Duck(sound="capcap",name="duck2",age=7)
    duck3 = Duck(sound="uwauwa")
    duck1.printDuck()
    duck2.printDuck()
    duck3.printDuck()


if __name__ == "__main__":main()