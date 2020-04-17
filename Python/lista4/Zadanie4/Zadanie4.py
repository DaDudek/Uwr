def sito(a,zakres):
    tablica=[]
    for i in range(a,zakres+1):
        tablica.append(i)
    if(0 in tablica):
        tablica.remove(0)
    if (1 in tablica):
        tablica.remove(1)
    for i in tablica:
        for j in range(2, zakres):
            if (i * j) in tablica:
                #szybsze rozwiązanie to tablica.remove(i*j) bez dodatkowej pętli
                for k in range(len(tablica)):
                    if tablica[k]==i*j:
                        tablica[k]=0
    return tablica
def palindromy(a,b):
    palindromiczne=[]
    tab=sito(a,b)
    for i in tab:
        słowo1=str(i)
        słowo2=""
        for i in range(len(słowo1)):
            słowo2=słowo2+słowo1[len(słowo1)-1-i]
        if (słowo1==słowo2):
            if słowo1 !="0":
                palindromiczne.append(słowo1)
    return palindromiczne
tab=sito(0,11)
tab1=palindromy(0,500)
print(tab)
print(tab1)
