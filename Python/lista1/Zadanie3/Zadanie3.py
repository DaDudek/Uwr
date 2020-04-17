def krotsze_linie(n):
    for i in range(n):
        print(" "*n,"*"*n,sep="")
def dluzsza_linia(n):
    for i in range(n):
        print("*"*n*3)
def krzyzyk(n):
    malykrzyzyk(n)
    duzykrzyzyk(n)
    malykrzyzyk(n)

krzyzyk(5)
