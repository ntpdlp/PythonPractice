
class A:
    def __init__(self):
        super().__init__()
        self.foo = "foo"
        self.name = "class A"


class B:
    def __init__(self):
        super().__init__()
        self.bar = "bar"
        self.name = "class B"

class C(A,B):
    def __init__(self):
        super().__init__()

    def showProperties(self):
        print(self.foo)
        print(self.bar)
        print(self.name)

class D(B, A):
    def __init__(self):
        super().__init__()

    def showProperties(self):
        print(self.foo)
        print(self.bar)
        print(self.name)        

def main():
    c = C()
    c.showProperties() # C(A,B) => name = "class A" (A is higher priority)
    print(C.__mro__)

    d = D()
    d.showProperties() # D(B,A) => name = "class B" (B is higher priority)
    print(D.__mro__)

if __name__ == "__main__": main()
