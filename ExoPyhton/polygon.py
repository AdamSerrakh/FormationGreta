""" Module de la classe Polygon """
from point import Point
import time
from turtle import *
import random
from math import pi

def makeColor():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return r,g,b


class Polygone:
    def __init__(self, sommets=[], couleur="black"):
        """ sommets est une liste de points, couleur est une chaîne
            parmi yellow, cyan, blue, red, green, black ..."""
        self.sommets = sommets
        self.couleur = couleur

    def __repr__(self):
        return f"Polygone({self.sommets}, '{self.couleur}')"

    def __str__(self):
        return repr(self)

    def __len__(self):
        return len(self.sommets)

    def dessine(self):
        """ Utilise la tortue pour dessiner le polygone """
        shape("turtle")
        color(self.couleur)
        showturtle()
        time.sleep(1)
        # point de départ
        p0 = self.sommets[0]
        # lever la plume
        penup()
        # aller au point de départ
        goto(p0.x, p0.y)
        # baisser la plume
        pendown()
        begin_fill()
        for p in self.sommets[1:]:
            goto(p.x, p.y)
            p.dessine()
        #revenir au point de départ
        goto(p0.x, p0.y)
        p0.dessine()
        end_fill()
        time.sleep(1)
        hideturtle()


    def rearrange(self):
        """ this transforms the polygon to make it "more convex" """
        n = len(self)//2
        self.sommets.sort()
        self.sommets= self.sommets[0:n]+self.sommets[n:][::-1]


class RegularPolygone(Polygone):
    def __init__(self, depart, n, cote, couleur, direction=0):
        l=[]
        s = depart
        angle = direction * pi / 180
        for i in range(n):
            l.append(s)
            angle = angle + 2 * pi /  n
            s = s.move(cote, angle)
            
        self.sommets = l
        self.couleur = couleur
        self.n = n
        self.origine = depart

    def __len__(self):
        return self.n

def makePolygones():
    colormode(cmode=255)
    for i in range(100):
        p = Polygone([Point.makePoint() for j in range(3,random.randint(4,10))]
                 ,makeColor())
        p.rearrange()
        p.dessine()

def makePolygonesReguliers():
    colormode(cmode=255)
    base =500
    for i in range(100):
        n = random.randint(3,8)
        cote = base / n
        p = RegularPolygone(Point.makePoint(),n,cote, makeColor(),
                            random.randint(1,360))
        p.dessine()

  
def main1():
    poly = Polygone([Point(10,20),Point(110,120),Point(200,300) ,Point(100,300),
                     Point(0,300)], couleur = "red")
    print(poly)
    print(repr(poly))
    print(len(poly))# Doit afficher le nombre de sommets ==> jusqu'à 16h20
    poly.dessine()

def main():
    degrees()
    pr = RegularPolygone(Point(0,0), 4, 100, 'red')
    print(pr)
    pr.dessine()

if __name__ == '__main__':
    makePolygonesReguliers()
                    
    
