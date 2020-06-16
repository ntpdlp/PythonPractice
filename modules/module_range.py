#! /usr/bin/env python3

#/bin/random.py > use the SystemRandom class
import random

def func_for_int_just_one():
    x = random.randrange(50)
    print(x)
    y = random.randrange(500,600,5)
    print(y)
    z = random.randint(800,900)
    print(z)

def func_for_sequence():
    x = list(range(5))
    y = list(range(20))
    random.shuffle(x)
    random.shuffle(y)
    print (x)
    print (y)

    fruits = ["avocado","banana", "orange","strawberry"]
    print(random.choice(fruits))

def main():
    # func_for_int_just_one()
    func_for_sequence()

if __name__ == "__main__": main()