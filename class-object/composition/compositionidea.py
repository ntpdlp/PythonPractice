
class Book:
    def __init__(self, title, price, author=None):
        self.title = title
        self.price = price
        self.author = author

        self.chapters = []

    def addchapter(self, name, pages):
        self.chapters.append((name, pages))

class Author:
    def __init__(self,authorfname, authorlname):
        self.authorfname = authorfname
        self.authorlname = authorlname

    def __str__(self):
        return self.authorfname + ' ' + self.authorlname


def main():
    author1 = Author("Leo", "Tolstoy")
    b1 = Book("War and Peace", 39.0, author1)
    b1.addchapter("Chapter 1", 125)
    b1.addchapter("Chapter 2", 97)
    b1.addchapter("Chapter 3", 143)
    print(b1.title)
    print(b1.author)

if __name__ == "__main__":main()