from duze_cyfry_zolw import *
from turtle import *
from random import *
def przejscie_dla_nowej_cyfry():
	pu()
	fd(25)
	rt(-90)
	fd(80)
	rt(90)
	pd()
def Zadanie3(liczba):
	x=str(liczba)
	kolory= ['red', 'green', 'blue', 'yellow', 'pink','orange']
	last_color=choice(kolory)
	for i in range(len(x)):
		nowy_kolor=choice(kolory)
		while(nowy_kolor==last_color):
			nowy_kolor=choice(kolory)
		rysuj_cyfre(int(x[i]),nowy_kolor)
		przejscie_dla_nowej_cyfry()
		last_color=nowy_kolor
Zadanie3(123456789)
input()
