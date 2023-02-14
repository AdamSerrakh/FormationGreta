""" an exercise to illustrate personnalized exceptions,
    the property decorators and
    alternate constructors
"""
import datetime

class AgeError(Exception):
    """ a personalized Exception for age matters """
    pass

MAXAGE = 120
MINAGE = 0

class Person:
    def __init__(self, name, year = None):
        y0 = datetime.date.today().year
        #
        # smart default for newborn babies
        #
        if year is None:
            year = y0
        #
        # conversion to int
        #
        try:
            y = int(year)
        except:
            raise AgeError(f"Invalid birth year {year}, should be a year number")
        #
        # likelihood
        #
        if y0-y not in range(MINAGE,MAXAGE+1):
            raise AgeError(f"Unlikely birth year {year}")
        #
        # note that there is no such thing as an age field here
        #
        self.name = name
        self.birthYear = int(year)
        

    @property
    def age(self):
        return datetime.date.today().year - self.birthYear

    @age.setter
    def age(self, val):
        try:
            val = int(val)
        except:
            raise AgeError(f"Invalid age {val}, should be a number of years")
        if val < MINAGE:
            raise AgeError(f"Invalid age {val}")
        if val > MAXAGE:
            raise AgeError(f"Unlikely age {val}")
        self.birthYear = datetime.date.today().year - val

    def __str__(self):
        return f"{self.name} born in {self.birthYear}, today aged {self.age}"

    def new(name, age=0):
        """ alternate constructor """
        p = Person(name)
        p.age = age
        return p
    
def main():
    """ a short test """
    p = Person("Georges", "1956")
    print(p)
    p.age = 50
    print(p)
    p1 = Person.new("Georges", 66)
    print(p1)

if __name__ == "__main__":
    main()
