import math
def dzielniki_liczby(n):
	Lista_dzielnikow=[]
	for i in range(2,n+1):
		if (n%i)==0:
			Lista_dzielnikow.append(i)
	return Lista_dzielnikow
def sprawdz_czy_liczba_pierwsza(liczba):
    pierwiastek = int(math.sqrt(liczba) + 1)
    for j in range(2, pierwiastek):
        if (liczba % j == 0):
            return False
    return True
def znajdz_dzielniki_pierwsze(n):
	Lista_dzielnikow=dzielniki_liczby(n)
	Lista_dzielnikow_pierwszych=[]
	for i in range(len(Lista_dzielnikow)):
		if sprawdz_czy_liczba_pierwsza(Lista_dzielnikow[i]):
			Lista_dzielnikow_pierwszych.append(Lista_dzielnikow[i])
	return Lista_dzielnikow_pierwszych
print(znajdz_dzielniki_pierwsze(1780))
