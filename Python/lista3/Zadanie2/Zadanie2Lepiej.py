import math
def sprawdz_czy_liczba_pierwsza(liczba):
    pierwiastek = int(math.sqrt(liczba) + 1)
    for j in range(2, pierwiastek):
        if (liczba % j == 0):
            return False
    return True
def znajdz_liczby_szczesliwe(ile_cyfr,ilosc_siodemek):
    lista=[]
    roznica=ile_cyfr-ilosc_siodemek
    for i in range(10**(roznica-1),(10**roznica)):
        napis=str(i)
        for j in range(roznica+1):
            if(sprawdz_czy_liczba_pierwsza(int(napis[:j]+"7"*ilosc_siodemek+napis[j:]))):
                x=int(napis[:j]+"7"*ilosc_siodemek+napis[j:])
                lista.append(x)
            y=int("7"*ilosc_siodemek+"0"+napis[:-1])
            if(sprawdz_czy_liczba_pierwsza(y)):
                lista.append(y)
    return len(set(lista))
print(znajdz_liczby_szczesliwe(10,7))



