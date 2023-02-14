from turtle import *
from math import sin,cos,pi
import random
class Point:
    """ une classe pour des points donnés par leurs coordonnées
        cartésiennes x et y (des flottants !)"""
    def __init__(self, abscisse, ordonnee):
        self.x = abscisse
        self.y = ordonnee

    def __repr__(self):
        #return "Point(%f,%f)"%(self.x,self.y)
        return f"Point({self.x},{self.y})"
        
    def __str__(self):
        """ faire pas la même chose que str """
        return f"({self.x}, {self.y})"

    def dessine(self,color="black"):
        penstate=pen()
        penup()
        goto(self.x,self.y)
        pen(penstate)
        dot(5,color)
        

    def makePoint():
        return Point(random.randint(-400,400),random.randint(-400,+400))

    def __lt__(self, value):
        if isinstance(value, Point):
            if abs(self.x-value.x)<1E-16:
                return self.y < value.y
            else:
                return self.x < value.x
        else:
            raise TypeError(f"Cannot compare Point and {type(value)}")

    def move(self, rho, theta):
        return Point(self.x+rho*cos(theta), self.y+rho*sin(theta))

def main():
    degrees()
    p1 = Point(0,0)
    print(repr(p1))
    assert repr(p1)=="Point(0,0)"
    print(p1)
    assert str(p1)=="(0, 0)"
    l = [Point.makePoint() for i in range(7)]
    print(l)
    print(sorted(l))
    p1.dessine()
    print(p1)
    p2 = p1.move(100,0)
    print(p2)
    p2.dessine()
    p3 = p2.move(100,pi/2)
    print(p3)
    p3.dessine()


if __name__ == '__main__':
    main()
