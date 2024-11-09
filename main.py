# class person():
#     def __init__(self,name,idnum):
#         self.name = name
#         self.idnum = idnum
#     def display(self):
#         print(self.name)
#         print(self.idnum)

# class Employee(person):
#     def __init__(self, name, idnum, salary, post):
#         self.salary = salary
#         self.post = post
#         person.__init__(self,name,idnum)

    
#     def details(self):
#         print(self.salary)
#         print(self.post)
    
       

# a = Employee("Ashutosh",28,300000,"CEO")

# a.display()
# a.details()   


#activity 2

from abc import ABC,abstractclassmethod

class plant(ABC):

    def move(self):
        pass

class Human(plant):
    def move(self):
          print("I can talk")

h = Human()
h.move()

class Dog(plant):
    def move(self):
          print("I can bark")

d = Dog()
d.move()
