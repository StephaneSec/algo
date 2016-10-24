#!/usr/bin/python3
from random import randint,shuffle
from math import sqrt
    
class Mediane:
    def __init__(self,n):
        self.n=n
        self.S=[]
        self.R=[]
        self.create(n)
    

    def create(self,n):
        for x in range(n):
            self.S.append(randint(0,n))
        self.R=self.S[0:int(n**0.75)]
        shuffle(self.R)
        self.randomQuickSort(0,len(self.R)-1)
        a=self.R[int(n**0.75/2-sqrt(n))]
        b=self.R[int(n**0.75/2+sqrt(n))]
        self.P=[]
        for x in range(len(self.S)):
            el=self.S[x]
            if el==a:
                self.rgaS=x
                self.P.append(self.S[x])
            elif el==b:
                self.rgbS=x
                self.P.append(self.S[x])
            elif self.S[x]>a and self.S[x]<b:
                self.P.append(self.S[x])
        set(self.P)
        self.cardP=len(self.P)

    def evaluation(self):
        if (self.rgaS>int(self.n/2)) or (self.rgbS<int(self.n/2)) or (self.cardP>=4*self.n**0.75):
            return False
        else :
#            self.T=self.R
            self.R=self.P
            self.randomQuickSort(0,len(self.R)-1)
            self.P=self.R
            return self.P[int(self.n/2)-self.rgaS+1]


    def partition(self,deb,fin,pivot):
        self.R[pivot],self.R[fin]=self.R[fin],self.R[pivot]
        j=deb
        for i in range(deb,fin):
            if self.R[i]<=self.R[fin]:
                self.R[i],self.R[j]=self.R[j],self.R[i]
                j+=1
        self.R[fin],self.R[j]=self.R[j],self.R[fin]
        return j

    
    def randomQuickSort(self,deb,fin):
        if deb<fin:
            pivot=randint(deb,fin)
            pivot=self.partition(deb,fin,pivot)
            self.randomQuickSort(deb,pivot-1)
            self.randomQuickSort(pivot+1,fin)
        return self.R



    



if __name__=='__main__':
    med=Mediane(100)
    print(med.S)
    print(med.R)
    print(med.rgaS)
    print(med.rgbS)
    print(med.P)
    print(med.cardP)
    print("mediane",med.evaluation())

