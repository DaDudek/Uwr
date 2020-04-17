from turtle import *
plik=open("niespodzianka.txt")
tracer(0,1)
pu()
lt(90)
fd(400)
rt(90)
pd()
def rysuj_kwadrat(Lista_kolorow):
	kolor_kwadratu=list()
	kolor_kwadratu.append(int(Lista_kolorow[0])/255)
	kolor_kwadratu.append(int(Lista_kolorow[1])/255)
	kolor_kwadratu.append(int(Lista_kolorow[2])/255)
	fillcolor(kolor_kwadratu)
	begin_fill()
	for i in range(5):
		fd(10)
		rt(90)
	end_fill()
	lt(90)
for wiersz in plik:
	wiersz_pikseli=wiersz.split()
	for i in range(len(wiersz_pikseli)):
		piksel=wiersz_pikseli[i][1:-1]
		rysuj_kwadrat(piksel.split(","))
	pu()
	lt(180)
	fd(10*len(wiersz_pikseli))
	lt(90)
	fd(10)
	lt(90)
	pd()
input()
#print(len(lista_wierszy))
    
