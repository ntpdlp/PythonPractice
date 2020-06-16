
class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, pages, author, price):
        self.title = title
        self.pages = pages
        self.author = author
        self.price = price
        self.__secret = "This is a secret attribute"

    # instance methods are defined like any other function, with the
    # first argument as the object ("self" is just a convention)
    def setDiscount(self, discount):
        self._discount = discount

    def getPrice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price


# create some book instances
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)

# print the price of book1
print(b1.getPrice())

# try setting the discount
print("price origin: {}".format(b2.getPrice()))
b2.setDiscount(0.25)
print("price with discount: {}".format(b2.getPrice()))

# properties with double underscores are hidden by the interpreter
print(b2._discount)
print(b1._discount) #error here because b1 was not setDiscount() => don't have _discount attr
# print(b2.__secret) #error here if trying to access
print(b2._Book__secret)
print(b1._Book__secret)