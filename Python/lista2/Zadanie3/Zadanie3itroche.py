from math import sqrt,pow
def wyrysuj_kolko(lista,a,b):
    List=lista
    spacebar = " " * b
    for i in range(a):
        List[i].insert(0,spacebar)
        for j in range(a+1):
            print(List[i][j],sep="",end="")
        print()
def stworz_kolko(a):
    List=[]
    promien=a/2
    for i in range(1, (a + 1)):
        list = []
        for j in range(1, (a + 1)):
            dlugosc=sqrt(pow((i-int((a/2)+1)),2)+pow(j-(int((a/2)+1)),2)) #pierwiastek z x1^2+x2^2 -y
            if(dlugosc< promien):
                list.append("#")
            else:
                list.append(" ")
        List.append(list)

    return List
def rysuj_kolko(a,b):
    kolko=stworz_kolko(a)
    wyrysuj_kolko(kolko,a,b)

def balwanek(a,b,c):
    rysuj_kolko(a,int(((c-a)/2)))
    rysuj_kolko(b,int(((c-b)/2)))
    rysuj_kolko(c,0)

balwanek(3,5,7)
