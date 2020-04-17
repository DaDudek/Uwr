import time
import math
def czy_pierwsza(n):
    pierwiastek=int(math.sqrt(n)+1)
    for i in range(2,pierwiastek):
        if n%i==0:
            return False
    return True
def sprawdz_czy_szczesliwa(n,k):
    liczba=str(n)
    if "7"*k in liczba:
        if czy_pierwsza(n):
            return True
    return False
def znajdz_szczesliwe_oraz_pierwsze(ile_cyfr,ile_siodemek):
    test=0
    for i in range(10**(ile_cyfr-1),10**(ile_cyfr)):
       if(sprawdz_czy_szczesliwa(i,ile_siodemek)):
           test=test+1
    print(test)
znajdz_szczesliwe_oraz_pierwsze(4,2)
