#! /usr/bin/env python3

class Duck:
    sound = "quack quack"
    action = "swimming"

    def say(self):
        print (self.sound)
    
    def act(self):
        print (self.action)

def main():
    aduck = Duck()
    aduck.say()
    aduck.act()

if __name__ == "__main__": 
    main()