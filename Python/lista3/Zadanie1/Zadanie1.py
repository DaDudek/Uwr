import math
def znajdz_szczesliwe_liczby(zakres,ile_siodemek):
    szczesliwe_liczby=[]
    siodemki="7"*ile_siodemek
    for i in range(1,(zakres+1)):
        if siodemki in str(i):
            szczesliwe_liczby.append(i)
    return szczesliwe_liczby
def znajdz_szczesliwe_liczby_pierwsze(lista):
    szczesliwe_liczby_pierwsze=[]
    lista_szczesliwych_liczb=list(lista)
    for i in range(len(lista_szczesliwych_liczb)):
        counter = 0
        for j in range(2,int(math.sqrt(lista_szczesliwych_liczb[i])+1)):
            if((lista_szczesliwych_liczb[i] % j)==0):
                counter=counter+1
        if counter==0:
            szczesliwe_liczby_pierwsze.append(lista_szczesliwych_liczb[i])
    return szczesliwe_liczby_pierwsze
def wyswietl_szczesliwe_liczby_pierwsze(zakres,ile_siodemek):
    list=znajdz_szczesliwe_liczby_pierwsze(znajdz_szczesliwe_liczby(zakres,ile_siodemek))
    print(list)
    print(len(list))
wyswietl_szczesliwe_liczby_pierwsze(100000,3)
