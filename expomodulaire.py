#! /usr/bin/python
from random import randint

def expo(a,p,n):
    resultat,puissance,w,mult=1,a,p,0
    while w>0:
        if w%2==1:
            resultat=puissance*resultat%n
            mult+=1
        puissance=puissance*puissance%n
        mult+=1
        w=w//2
    return (resultat,mult)

def genere(borneinf,bornesup):
    l=[]
    for k in range(1000):
        l.append(randint(borneinf,bornesup))
    return l

if __name__=='__main__':
    a,n=123,987
    l=genere(2**19,2**20-1)
    moy=[]
    for x in range(1000):
        compteur=0
        for k in l:
            compteur+=expo(a,k,n)[1]
        moyenne=float(compteur/len(l))
        print(moyenne)
        moy.append(moyenne)
   
