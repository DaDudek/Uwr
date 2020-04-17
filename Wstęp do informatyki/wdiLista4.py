from Wdi.wdi import *


def Zadanie1a(n):
    if (n%2)==0:
        return n
    else:
        return n*(-1) #liniowa
def Zadanie1b(n):
    tmp=0
    for i in range(1,n+1):
        x=(-1)**i
        y=x/i
        tmp=tmp+y
    return tmp  #liniowa
def Zadanie1c(n,x):
    x_do_i=x
    tmp=x
    for i in range(2,n+1):
        x_do_i=x_do_i*x
        y=i*x_do_i
        tmp=tmp+y
    return tmp  #liniowa
def NWD(a,b):
    n = a
    m = b
    if n < m:
        k = m
        m = n
        n = k  # NWW=(a*b)/NWD
    while m > 0:
        k = n % m
        n = m
        m = k
    return n
def Zadanie2a(a,b):
    return NWD(a,b)
def Zadanie2b(a,b):
    x=a/NWD(a,b)
    y=b/NWD(a,b)
    return x,y
def Zadanie3(n):
    Tablica=Array(n)
    for i in range(n):
        Tablica[i]=int(input())
    nwd=NWD(Tablica[i],Tablica[i-1])
    a=i-2
    while a>-1:
        nwd=NWD(Tablica[a],nwd)
        a=a-1
    print(nwd)
def Zadanie4(n,k):
    Lista_dzielnikow_pierwszych=Array(n)
    counter=0
    i=1
    while(n>1):
        if(n%i)==0:
            Lista_dzielnikow_pierwszych[counter]=i
            counter=counter+1
            n=n/i
            i=1
        i=i+1
    for a in range(len(k)):
        if k[a] in Lista_dzielnikow_pierwszych:

    for j in range(counter):
        print(Lista_dzielnikow_pierwszych[j])
    return Lista_dzielnikow_pierwszych
def Zadanie5(n):
    flaga=True
    tmp=""
    while(n>0):
        x=n%2
        n=int(n/2)
        tmp=tmp+str(x) #binarna od końca
    print(tmp)
    for i in range(len(tmp)):
        if(tmp[i] != tmp[-(i+1)]):
            flaga=False
    return flaga
def Zadanie6(n):
    Tablica=Array(10)
    for i in range(10):
        Tablica[i]=0 #licznik cyfr
    x=len(str(n))
    for j in range(x):
        y=str(n)[j] #j cyfra liczby podanej na wejsciu
        Tablica[int(y)]=1
    counter=0
    for k in range(10):
        if(Tablica[k]==1):
            counter=counter+1
    return counter
Zadanie4(100,2)