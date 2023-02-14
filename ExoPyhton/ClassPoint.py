#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math

class Point:
    def __init__(self, ab, ordo):
        #assert type(ab)==float and type(ordo)==float, "Les coordonnées doivent être exprimée en flotants"
        self.x = float(ab)
        self.y = float(ordo)
    def __str__(self):
        return f'absisse {self.x} ordonnée {self.y}'
    def __repr__(self):
        return f'{__class__.__name__}({self.x},{self.y})'
    def move(self, rho, theta):
        """ l'angle thetha est eprimé en degrés """
        return Point(round(self.x + rho * math.cos(math.pi*theta/180),5), round(self.y + rho * math.sin(math.pi*theta/180),5))
    def milieu(self, unpoint):
        return Point((self.x+unpoint.x)/2,(self.y+unpoint.y)/2)
    def distance(self, unpoint):
        return math.sqrt((self.x-unpoint.x)**2+(self.y-unpoint.y)**2)
    
    
def main():
    monpoint = Point(0,0)
    print(monpoint)
    print(repr(monpoint))
    print(monpoint.move(1,180))
    point2 = Point(0,1)
    print(monpoint.milieu(point2))
    print(monpoint.distance(point2))

if __name__ == '__main__':
    main()


# In[ ]:




