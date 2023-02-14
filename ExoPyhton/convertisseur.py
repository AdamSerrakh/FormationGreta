#!/usr/bin/env python
# coding: utf-8

# In[5]:


class Convertisseur:
    def __init__(self,devise1,devise2, taux):
        self.dev1 = devise1
        self.dev2 = devise2
        self.tx = taux
    
    def __str__(self):
        return f'convertisseur {self.dev1} vers {self.dev2} au taux de {self.tx}'
    
    def __repr__(self):
        return f'{self.__class__.__name__}("{self.dev1}","{self.dev2}",{self.tx})'
    
    def convertir(self, montant):
        ''' Ceci est une fonction de conversion qui attend un montant
        exemple : convertir(20) => 14
        '''
        return self.tx*montant
    
def main():
    monconv = Convertisseur("EUR","USD",1.20)
    print(monconv.convertir(50))
    print(monconv)
    print(repr(monconv))
    
if __name__ == '__main__':
    main()


# In[ ]:




