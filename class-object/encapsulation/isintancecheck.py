class Book:
    def __init__(self, title):
        self.title = title


class Newspaper:
    def __init__(self, name):
        self.name = name


# Create some instances of the classes
b1 = Book("The Catcher In The Rye")
b2 = Book("The Grapes of Wrath")
n1 = Newspaper("The Washington Post")
n2 = Newspaper("The New York Times")

# TODO: use type() to inspect the object type
print(type(b1))
print(type(n1))

# TODO: compare two types together
print(type(b1) == type(b2)) #true
print(type(b1) == type(n2)) #false

# TODO: use isinstance to compare a specific instance to a known type
print(isinstance(n1, Newspaper))
print(isinstance(n1,Book)) #False
print(isinstance(b1, Book)) 
print(isinstance(b1,object)) #always true
print(isinstance(n1,object))



