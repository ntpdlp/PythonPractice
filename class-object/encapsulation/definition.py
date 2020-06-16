class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, defaultAtt=None):
        self.title = title
        self.defaultAtt = defaultAtt


# TODO: create instances of the class
book1 = Book("Brave New World","default attribute")
book2 = Book("War and Peace")

# TODO: print the class and property
print(book1)
print(book1.title) #public instance attribute
print(book1.defaultAtt) 
print(book2.defaultAtt) #None