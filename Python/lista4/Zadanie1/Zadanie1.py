from turtle import *
from random import randint, random
import numpy as np
ht()
#18 rzedow z czego 17 tworzy ciąg
speed="fastest"
def kwadrat(bok, kolor):
    fillcolor(kolor)
    begin_fill()
    for i in range(4):
        fd(bok)
        rt(90)
    end_fill()
    fd(bok)

def zmiana_koloru(kolor1,kolor2,waga):
    kolor=[0,0,0]
    kolor[0]=(kolor1[0]*(1-waga))+(kolor2[0]*waga)
    kolor[1]=(kolor1[1]*(1-waga))+(kolor2[1]*waga)
    kolor[2]=(kolor1[2]*(1-waga))+(kolor2[2]*waga)
    return kolor

def obrazek(n,bok):
    ilosc_kwadratow=2+((2*2+(n-2))/2)*(n-1)
    licznik_kwadratow =0
    kolor1=[1.0,1.0,0.0]#żółty
    kolor2=[1.0,0.01,0.55]#różowy
    for k in range(2):
        waga=licznik_kwadratow/ilosc_kwadratow
        kolor=zmiana_koloru(kolor1,kolor2,waga)
        kwadrat(bok,kolor)
        licznik_kwadratow +=1
    rt(90)
    fd(bok)   
    for i in range(2,n):
        for j in range(i):
            waga=licznik_kwadratow/ilosc_kwadratow
            kolor=zmiana_koloru(kolor1,kolor2,waga)
            kwadrat(bok,kolor)
            licznik_kwadratow +=1
        rt(90)
        fd(bok)
    for i in range(n-1):#ostatni rząd
        waga=licznik_kwadratow/ilosc_kwadratow
        kolor=zmiana_koloru(kolor1,kolor2,waga)
        kwadrat(bok,kolor)
        licznik_kwadratow +=1
        
obrazek(18,20)
input()	
