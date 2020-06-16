#! /usr/bin/env python3

class Person:
    def __init__(self,**kwargs):
        if 'name' in kwargs: self._name = kwargs['name']
    
    def name(self,n = None):
        if n: self._name = n
        return self._name

    def printInfo(self,**kwargs):
        print (f"name={self.name()}")

class Employee(Person):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        if 'title' in kwargs: self._title = kwargs['title']
        if 'salary' in kwargs: self._salary = kwargs['salary']

    def title(self,t = None):
        if t: self._title = t
        return self._title

    def salary(self,s = None):
        if s: self._salary = s
        return self._salary

    def printInfo(self,**kwargs):
        print(f"name={super().name()} , title={self.title()} and salary={self.salary()}")

        
def main():
    person1 = Person(name="Alen") 
    employee1 = Employee(name="Quynh",title="Java dev",salary=100)
    employee1.salary(500)
    person1.printInfo()
    employee1.printInfo()

if __name__ == "__main__": main()