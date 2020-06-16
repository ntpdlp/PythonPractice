
class Book:
    # TODO: Properties defined at the class level are shared by all instances
    BOOK_TYPES = ("PAPER", "EBOOK")
    # TODO: double-underscore properties are hidden from other classes: secret field
    __booklist = None

    # static methods do not receive class or instance arguments
    # and usually operate on data that is not instance- or
    # class-specific
    @staticmethod
    def getbooklist():
        if Book.__booklist == None: 
            Book.__booklist = []
        return Book.__booklist

    # class methods receive a class as their argument and can only
    # operate on class-level data
    @classmethod
    def getbooktypes(self):
        return self.BOOK_TYPES

    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def setTitle(self, newtitle):
        self.title = newtitle

    def __init__(self, title, booktype):
        self.title = title
        if not booktype in Book.BOOK_TYPES:
            raise ValueError(f"{booktype} is not correct, in booktypes.")
        else:
            self.booktype = booktype


    def __str__(self):
        return "[Book: " + self.title + ", " + self.booktype + "]"



# TODO: access the class attributes
print("Book types: ", Book.getbooktypes())

# # TODO: Create some book instances
b1 = Book("Title 1", "PAPER")
b2 = Book("Title 2", "EBOOK")

# # TODO: Use the static method to access a secret class field
books = Book.getbooklist()
books.append(b1)
books.append(b2)
for x in books:
    print(x)



