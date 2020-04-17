from Wdi.wdi import *
def Zadanie1(): #k i lewy robili sie 0 a prawy 1 przez co to nigdy nie działało
    a=Array(9)
    a[0]=1
    a[1]=3
    a[2] = 6
    a[3] = 8
    a[4] = 10
    a[5] = 12
    a[6] = 14
    a[7] = 30
    a[8] = 100
    i=8
    x = a[8]
    lewy = 0
    prawy = i - 1
    while (lewy <= prawy):
        k=(lewy+prawy) //2
        if(a[k]==x):
            return k
        if (a[k] < x):
            lewy=k+1
        else:
            prawy=k-1
    print(lewy)
    print(k)
def Zadanie2(n):
    #liczba porownan stala =(n/2 *(n-1))
    #liczba podstawien:
    #dla rosnacego: n (uzupełnienie tablicy) + n (przypisanie index min) +3n(koncowka)
    #dla malejacego: n(uzupełnienie tablicy)+3n(koncowka)+suma(od x=0 do x=n z len(x)/2 zaokrąglonego w gore)
    tablica=Array(n)
    for i in range(n):
        tablica[i]=int(input())
    for a in range(n):
        index_min=a
        for b in range(a+1,n):
            if(tablica[b]<tablica[index_min]):
                index_min=b #dominująca
                counter=counter+1
        tmp=tablica[a]
        tablica[a]=tablica[index_min]
        tablica[index_min]=tmp
    print(counter)
def Zadanie3(n):
    # liczba porownan stala =(n/2 *(n-1))
    # liczba podstawien:
    # dla rosnacego: n(uzupełnienie tablicy)
    # dla malejacego: n(uzupełnienie tablicy) +(n/2)*(n-1)*3
    tablica=Array(n)
    for i in range(n):
        tablica[i]=int(input())
    for a in range(n):
        for b in range(n-1):
            if (tablica[b]>tablica[b+1]):
                tmp=tablica[b] #domina
                tablica[b]=tablica[b+1] #domina
                tablica[b+1]=tmp #domina
def Zadanie4(a,k):
    #W(x)=a[0]*(x^k) + a[1]*(x^(k-1)) + ...+ a[k]*(x^0)
    w=0
    for i in range(k+1):
        w=w+(a[i]*(2**(k-i)))
    return w
def Czy_Liczba_pierwsza(n):
    a=2
    while(a*a<=n):
        if (n % a == 0):
            return False
        a=a+1
    return True
def Zadanie5(n):
    tablica = Array(n+1)
    for i in range(n+1):
        tablica[i] = i
    tablica[0]=0
    tablica[1]=0
    a=2
    while(a*a<=n):
        for j in range(a+1,n+1):
            if tablica[j]==0:
                continue
            if(Czy_Liczba_pierwsza(j)):
                if((tablica[j]%a)==0 and tablica[j]!=1):
                    tablica[j]=0
            else:
                tablica[j]=0
        a=a+1
    for j in range(n+1):
        if(tablica[j]!=0):
            tablica[j]=1
    for k in range(n + 1):
        print(tablica[k])
def Zadanie6(m,n):
    zakres=n+1-m
    tablica = Array(zakres)
    for i in range(zakres):
        tablica[i] = m+i
    a=0
    counter=m
    while (a<zakres):
        for k in range(zakres):
            if tablica[k] == 0:
                continue
            if (Czy_Liczba_pierwsza(counter)):
                if ((tablica[k] %counter) == 0 and tablica[k] != 1 and tablica[k]!=counter):
                    tablica[k] = 0
            else:
                tablica[a] = 0
                break
        a = a + 1
        counter=counter+1
    for j in range(0,zakres):
        if (tablica[j] != 0):
            tablica[j] = 1
    for k in range(0,zakres):
        print(tablica[k])
Zadanie6(15,40)