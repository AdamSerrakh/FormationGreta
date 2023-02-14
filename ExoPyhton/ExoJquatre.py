#!/usr/bin/env python
# coding: utf-8

# In[1]:


v=[1,12,30]
w=[4,23,15]


# In[2]:


def somme(v):
    """Calcule la somme des éléments d'un vecteur"""
    x=0
    for n in v:
        x += n
    return x


# In[3]:


somme(v)


# In[4]:


somme(w)


# In[5]:


def sommeVect(v1,v2):
    """Calcule la somme de deux vecteurs"""
    assert len(v1)==len(v2), "les vecteurs ne sont pas de même dimension"
    return [v1[x]+v2[x] for x in range(len(v1))]


# In[6]:


sommeVect(v,w)


# In[7]:


def sommeVect2(v1,v2):
    """Calcule la somme des éléments de deux vecteurs"""
    return somme(v1)+somme(v2)


# In[8]:


sommeVect2(v,w)


# In[9]:


def scalaire(v,n):
    """Multiplies les éléments d'un vecteur avec un nombre"""
    return [v[i]*n for i in range(len(v))]  


# In[10]:


scalaire(v,5)


# In[11]:


def scalaire2(v,n):
    """Multiplies la somme des éléments avec un nombre"""
    return somme(v)*n


# In[12]:


scalaire2(v,5)


# In[13]:


def scalaireVect(v1,v2):
    """Multiplie deux vecteur entre eux"""
    assert len(v1)==len(v2), "les vecteurs ne sont pas de même dimension"
    return [v1[x]*v2[x] for x in range(len(v1))] 


# In[14]:


scalaireVect(v,w)


# In[15]:


def contient(words, pattern):
    """Vérifie si un caractère est dans une chaine de caratère"""
    for m in words:
        if pattern in m:
            return True
    return False


# In[16]:


maliste =["Riri", "Fifi", "Loulou"]
pattern= "rvre"


# In[17]:


contient(maliste,"lou")


# In[18]:


import math


# In[19]:


def estPremier(n):
    """Dus si un nombre est premier"""
    for x in range(2,int(math.sqrt(1000000))+1):
        if (n%x==0):
            return False
    return True


# In[20]:


def listePremier(n):
    """Donne une liste de nombre premier"""
    return [ i for i in range(2,n) if estPremier(i)] 
        


# In[21]:


estPremier(47)


# In[22]:


print (listePremier(1_000_000), end=" ")


# In[23]:


import random


# In[24]:


def makevec ( n, a=-100, b=+100):
    """Donne une liste de nomre"""
    return [random.randint(a,b) for i in range(n)]


# In[25]:


v1 = makevec(13,0,+100)
v1


# In[26]:


def cherche(x,v):
    """Cherche si un nombre est dans ne liste"""
    for i,j in enumerate(v):
        if j == x:
            return i
    return -1   
def cherche2(x,v):
    return x in v


# In[27]:


cherche(28,v1), cherche(55,v1), cherche2(37,v1), cherche2(7,v1)


# In[28]:


Lchiffre = input("Entrez un nombre ")
x=0
for n in range(len(Lchiffre)):
    x+= int(Lchiffre[n])
x


# In[ ]:





# In[ ]:





# In[ ]:




