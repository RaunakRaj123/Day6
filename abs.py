from abc import ABC,abstractmethod
class Quadrilateral:
    @abstractmethod
    def sides(self):
        pass
class Rectangle(Quadrilateral):
    def sides(self):
        print("Rectangle has equal oppsite sides")
class Square(Quadrilateral):
    def sides(self):
        print("Square has equal adjacent sides")
s=Rectangle()
s.sides()
r=Square()
r.sides()
