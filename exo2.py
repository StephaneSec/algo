#! /usr/bin/python3

def expo(a,p,n):
    if p==0:
        return 1
    else :
        return a*expo(a,p-1,n)%n

if __name__=='__main__':
    print(expo(2,20,20))
