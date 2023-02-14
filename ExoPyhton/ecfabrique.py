import random

def random_immat():
    def randomString(n):
        def randomLetter():
            alphabet = "ABCDEFGHJKLMNPQRSTUVWXYZ"
            return alphabet[random.randint(0,23)]

        return "".join([randomLetter() for i in range(n)])
    return randomString(2)+str(random.randint(100,9999))+randomString(2)


class CarFactory:
    def makeCar(self):
        raise NotImplementedError


class Car:
    def __init__(self, marque, modele, immat):
        self.marque = marque
        self.modele = modele
        self.immat = immat
        
    def __str__(self):
        return f"{self.marque}, {self.modele}, {self.immat}"

class PeugeotCar(Car):
    def __init__(self, modele, immat):
        super().__init__("Peugeot", modele, immat)


class ToyotaCar(Car):
    def __init__(self,modele, immat):
        super().__init__("Toyota", modele, immat)


class PeugeotFactory(CarFactory):
    def makeCar(self):
        modele = random.choice(["208", "308", "3008"])
        immat = random_immat()
        c = PeugeotCar(modele, immat)
        return c

class ToyotaFactory(CarFactory):
    def makeCar(self):
        modele = random.choice(["Yaris", "Auris", "Prado"])
        immat = random_immat()
        c = ToyotaCar(modele, immat)
        return c
        
def main():
    pf = PeugeotFactory()
    tf = ToyotaFactory()
    parc = []
    for i in range(10):
        x = random.randint(0,1)
        if x:
            c = pf.makeCar()
        else:
            c = tf.makeCar()
        parc.append(c)
    print("Count of cars: ",len(parc))
    for car in parc:
        print(car)

        
if __name__ == '__main__':
    main()




