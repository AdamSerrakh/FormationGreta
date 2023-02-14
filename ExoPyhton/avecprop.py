class Article:
    TVA = 0.05
    def __init__(self,name,prix_unitaire, quantite):
        self.prix_unitaire = prix_unitaire
        self.quantite = quantite
        self.name = name
    @property
    def a_payer(self):
        return (1+Article.TVA)*self.prix_unitaire*self.quantite

def main():
    a = Article("Crayon", 0.30, 8)
    print(a.a_payer)

main()


    
