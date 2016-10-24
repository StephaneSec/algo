#!/usr/bin/python

from random import randint

class Noeud():
    def __init__(self,n):
        self.statut='actif'
        self.valeur=randint(1,n)
        self.compteur=n

    def tirage(self):
        self.valeur=randint(1,self.compteur)
    

class Ring():
    def __init__(self,n):
        self.liste=[]
        for x in range(n):
            self.liste.append(Noeud(n))


    def listeActifs(self):
        #renvoie la liste des actifs
        l=[]
        for x in self.liste:
            if x.statut=='actif':
                l.append(x)
        return l
            
if __name__=='__main__':
    n=20
    ring=Ring(n)
    for x in ring.liste:
        print(x.valeur,x.statut,x.compteur)

    leader=False
    while not leader:
        for x in ring.listeActifs():
            print(x.valeur)

    
