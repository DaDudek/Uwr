def silnia(n):
    wynik=1
    if n==0:
        return 1
    for i in range(1,n+1):
        wynik=wynik*i
    return wynik
def HowManyNumbers(n):
    x=silnia(n)
    y=len(str(x)) #ostatni znak długości
    z=str(len(str(x)))[-1]
    test1= (z == "2" and y % 100 != 12)
    test2= (z == "3" and y % 100 != 13)
    test3= (z == "4" and y % 100 != 14)
    if test1 or test2 or test3:
        print(n,"! ma ",len(str(x))," cyfry")
    else:
        print(n,"! ma ",len(str(x))," cyfr")
def Zadanie2():
    for i in range(4,101):
        HowManyNumbers(i)

Zadanie2()

#count=0
#napis=str(x)
#for i in napis:
#    count +=1
#print(count)
# druga metoda na sprawdzanie długości
