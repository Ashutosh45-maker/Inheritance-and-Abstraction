  
from abc import ABC,abstractclassmethod

class Coding(ABC):

    def move(self):
        pass

class Game(Coding):
    def move(self):
          print("Coding is my most important organ")

h = Coding()
h.move()

class Project(Coding):
    def move(self):
          print("I am made with the help of python language")

d = Project()
d.move()
