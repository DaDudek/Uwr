from duze_cyfry import daj_cyfre

def drukuj_cyfre(n):
    tmp =str(n)
    for i in range(len(tmp)):
        x=int(tmp[i])
        for r in daj_cyfre(x):
            print(r)
def przygotuj_drukuj_cyfre_ladniej(n):
    List=[]
    tmp = str(n)
    for i in range(len(tmp)):
        x=int(tmp[i])
        List.append(daj_cyfre(x) )

    return List
def drukuj_cyfre_ladniej(n):
    List=przygotuj_drukuj_cyfre_ladniej(n)
    tmp = str(n)
    lastNum =int(tmp[len(tmp)-1])
    for i in range(5):
        row = ""
        for j in range(lastNum):
            row += List[j][i]
            row +=" "
        print(row)



drukuj_cyfre_ladniej(123456789)