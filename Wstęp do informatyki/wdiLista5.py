from Wdi.wdi import *
def Zadanie2(n):
    i=1
    silnia=1
    while silnia<=n: # to jest log bo silnia rośnie szybciej niż ciąg 2*2*2*2 więc znajde "i" w mniej obrotów niż log
        i=i+1
        silnia=silnia*i
    silnia=silnia/i
    i=i-1
    tablica=Array(i)
    counter=i
    for j in range(counter):
        tmp=int(n/silnia)
        tablica[j]=tmp
        n=n-(silnia*tmp)
        silnia=silnia/i
        i=i-1
    for k in range(j+1):
        print(tablica[k])
    return tablica
def Zadanie3(n,m):
    counter=1
    while(m!=0):
        if (n < m):
            k = n
            n = m
            m = k
            continue
        ilenp=n%2+m%2
        if ilenp==2:
            n=n-m
            continue
        if ilenp==0:
            counter=counter*2 # powinienem zwracać 2* nwd więc counter zwróci mi przez ile musze ostatnie pomnożyć
            n=n/2
            m=m/2
            continue
        if n%2==0:
            n=n/2
            continue
        else:
            m=m/2
    return n*counter
def Zadanie4(n):
    najm=1
    sred=1
    najw=1
    wynik=0
    if n<=2:
        return 1
    for i in range(3,n+1):
        wynik=najm+sred+najw
        najm=sred
        sred=najw
        najw=wynik
    return wynik

def Zadanie5a(n,m): #fTrec(3,4)==486 #zadanie5a
        if m==0:
            return n
        if n==0:
            return m
        else:
            return Zadanie5a(n-1,m)+2*Zadanie5a(n,m-1)
def Zadanie5b(n,m):
	stara=Array(n+1)
	nowa=Array(n+1)
	for i in range(n+1):
		stara[i]=i
	for p in range(1,m+1):
		nowa[0]=p
		for r in range(1,n+1):
			tmp=stara[r]*2+nowa[r-1]
			nowa[r]=tmp
			stara[r]=nowa[r]
	return(stara[n])
def Zadanie6(k,r): #Pisano Period
    a=0
    b=1
    pozycja=0
    for i in range(r*r):
        c=(a+b)%r
        a=b
        b=c
        if(a==0 and b==1):
            pozycja=i+1
            break
    potrzebny_wyraz = k % pozycja  # np F(2010)%3 == F((2010%8))mod3
    tmp=potrzebny_wyraz
    for j in range(1,potrzebny_wyraz):
        tmp=(a+b)%r
        a=b
        b=tmp
    return tmp

def Zadanie7b(n,m):
    tmp=2
    if(n>m):
        return 1
    while((n**tmp)<m): #znajduje n^2^x > tmp gdzie 2^x to tmp
        tmp=tmp*tmp
    start=1
    end=tmp
    srodek=(start+end)//2
    while(not((n**(srodek-1))<m and (n**(srodek))>=m)):
        if (n**srodek> m):
            end=srodek
            start=start
        else:
            start=srodek
            end=end
        srodek = (start+end)//2
    return srodek

print(Zadanie7b(7,3231421412312))

