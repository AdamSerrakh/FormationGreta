"""
    Problème du Kebab, utilisant le Design Pattern Decorator
    
    Pour comprendre le contenu du module, lire ceci:
    http://sdz.tdct.org/sdz/le-pattern-decorator-en-python.html

    !!!
    Ignorer la dernière partie 'Decorator et les décorateurs en Python'
    !!!
"""

PRIX_BASE_BURGER = 3.5
PRIX_BASE_KEBAB = 3.0
PRIX_FRITES = 0.5
PRIX_FROMAGE = 0.5
PRIX_MOD_PAIN = 0.2
PRIX_MOD_VIANDE = 0.2
PRIX_MOUTON = 0.8
PRIX_OIGNONS = 0.3
PRIX_POULET = 1.0
PRIX_STEAK = 2.0
PRIX_SALADE = 0.2
PRIX_TOMATES = 0.2

class Sandwich:
    def __init__ (self, sauce):
        self.sauce = sauce
        self._ing = {}

    def __repr__ (self):
        return f"Sandwich sauce {self.sauce}"

    def __str__ (self):
        s = repr(self)
        for key, val in self._ing.items():
            s += f"\n {val['qte']:>2}x {key:<15}{val['prix']*val['qte']:>5.2f} €"
        s += f"\nTotal               {self.prix():>5.2f} €"
        return s

    def prix(self):
        return sum(ingr["prix"] * ingr["qte"] for ingr in self._ing.values())


class Kebab(Sandwich):
    def __init__ (self, sauce):
        super().__init__(sauce)
        self._ing['base'] = { "prix": PRIX_BASE_KEBAB, "qte": 1 }
        self._ing['salade'] = { "prix": PRIX_SALADE, "qte": 1 }
        self._ing['tomates'] = { "prix": PRIX_TOMATES, "qte": 1 }
        self._ing['oignons'] = { "prix": PRIX_OIGNONS, "qte": 1 }
        self._ing['frites'] = { "prix": PRIX_FRITES, "qte": 1 }

    def __repr__ (self):
        return f"Kebab sauce {self.sauce}"


class DecorateurSandwich(Sandwich):
    def __init__ (self, sandwich):
        super().__init__(sandwich.sauce)
        self.sandwich = sandwich
        self._ing = sandwich._ing


class RetraitIngredient(DecorateurSandwich):
    def __init__ (self, sandwich, ingredient):
        super().__init__(sandwich)
        self.retrait = None
        if ingredient in self._ing:
            del self._ing[ingredient]
            self.retrait = ingredient

    def __repr__ (self):
        r = repr(self.sandwich)
        if self.retrait:
            r += f", sans {self.retrait}"
        return r


class Supplement(DecorateurSandwich):
    def __init__ (self, sandwich, ingredient, prix):
        super().__init__(sandwich)
        ing = self._ing.get(ingredient, { "prix": prix, "qte": 0 })
        self.ajout = ingredient
        self._ing[ingredient] = { "prix": ing["prix"], "qte": ing["qte"]+1 }

    def __repr__ (self):
        r = repr(self.sandwich)
        s = f", supplément {self.ajout}"
        if s not in r:
            r += s
        return r


class ModViande(DecorateurSandwich):
    def __init__ (self, sandwich, viande):
        super().__init__(sandwich)
        self.viande = viande
        self.deja_fait = "mod viande" in self._ing.keys()
        if not self.deja_fait:
            self._ing["mod viande"] = { "prix": PRIX_MOD_VIANDE, "qte": 1 }

    def __repr__ (self):
        s = f" mod viande {self.viande}"
        r = repr(self.sandwich).split(",")
        if self.deja_fait:
            for idx, elt in enumerate(r):
                if "mod viande" in elt:
                    r[idx] = s
                    break
        else:
            r.append(s)
        return ",".join(r)



class ModPain(DecorateurSandwich):
    def __init__ (self, sandwich, pain):
        super().__init__(sandwich)
        self.pain = pain
        self.deja_fait = "mod pain" in self._ing.keys()
        if not self.deja_fait:
            self._ing["mod pain"] = { "prix": PRIX_MOD_PAIN, "qte": 1 }

    def __repr__ (self):
        s = f" pain {self.pain}"
        r = repr(self.sandwich).split(",")
        if self.deja_fait:
            for idx, elt in enumerate(r):
                if "pain" in elt:
                    r[idx] = s
                    break
        else:
            r.append(s)
        return ",".join(r)


class Burger(Sandwich):
    def __init__ (self, sauce):
        super().__init__(sauce)
        self._ing['base'] = { "prix": PRIX_BASE_BURGER, "qte": 1 }
        self._ing['steak'] = { "prix": PRIX_STEAK, "qte": 1 }
        self._ing['tomates'] = { "prix": PRIX_TOMATES, "qte": 1 }
        self._ing['oignons'] = { "prix": PRIX_OIGNONS, "qte": 1 }
        self._ing['fromage'] = { "prix": PRIX_FROMAGE, "qte": 1 }
        self._ing['frites'] = { "prix": PRIX_FRITES, "qte": 1 }

    def __repr__ (self):
        return f"Burger sauce {self.sauce}"


def main():
    sand1 = Kebab("harissa")
    print(sand1)
    sand1 = RetraitIngredient(sand1, "oignons")
    print(sand1)
    sand1 = Supplement(sand1, 'frites', PRIX_FRITES)
    print(sand1)
    sand1 = ModViande(sand1, 'dinde')
    print(sand1)
    sand1 = ModViande(sand1, 'boeuf')
    print(sand1)
    sand1 = ModPain(sand1, 'pita')
    print(sand1)
    
    sand2 = Burger("barbecue")
    sand2 = RetraitIngredient(sand2, "oignons")
    sand2 = Supplement(sand2, 'tomates', PRIX_TOMATES)
    sand2 = ModViande(sand2, 'poulet')
    print(sand2)

if __name__ == "__main__":
    main()
