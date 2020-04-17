from turtle import *
from random import *
def kwadrat(bok, kolor):
    fillcolor(kolor)
    begin_fill()
    for i in range(4):
        fd(bok)
        rt(90)
    end_fill()
def przejscie_dla_nowego_rzedu(n,k,licznik):
	rt(90)
	fd(k)
	rt(90)
	fd(k*(licznik-2))
	pu()
	fd(k/2)
	pd()
	rt(180)
 
def piramida(n,k):
	kolory= ['red', 'green', 'blue', 'yellow', 'pink','orange']
	licznik=1
	while(n!=0): #ilosz rzedow
		last_color=choice(kolory)
		for i in range(0,licznik): #ilosc kwadratow
			nowy_kolor=choice(kolory)
			while(nowy_kolor==last_color):
				nowy_kolor=choice(kolory)
			last_color=nowy_kolor
			kwadrat(k,nowy_kolor)
			fd(k)
		fd(-k)
		licznik=licznik+1 #zmiana_kolory
		n=n-1
		przejscie_dla_nowego_rzedu(n,k,licznik)
			
piramida(6,20)
input()
