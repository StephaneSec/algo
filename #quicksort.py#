#!/usr/bin/python3
from random import randint

def partition(deb,fin,pivot):
    T[pivot],T[fin]=T[fin],T[pivot]
    j=deb
    for i in range(deb,fin):
        if T[i]<=T[fin]:
            T[i],T[j]=T[j],T[i]
            j+=1
    T[fin],T[j]=T[j],T[fin]
    return j


def quickSort(deb,fin):
    if deb<fin:
        pivot=deb
        pivot=partition(deb,fin,pivot)
        quickSort(deb,pivot-1)
        quickSort(pivot+1,fin)

def randomQuickSort(deb,fin):
    if deb<fin:
        pivot=randint(deb,fin)
        pivot=partition(deb,fin,pivot)
        randomQuickSort(deb,pivot-1)
        randomQuickSort(pivot+1,fin)
        
T=[2,0,3,4,1,5,6,8,21,0,4,-6,8,1,9]
randomQuickSort(0,len(T)-1)
print(T)
