from losowanie_fragmentow import losuj_fragment
def losuj_haslo(n):
    haslo=""
    lenght=n
    while lenght != 0:
        x=losuj_fragment()
        y=len(str(x))
        if lenght - y != 1 and lenght - y >= 0:
            haslo=haslo + x
            lenght=lenght-y
    return haslo

for i in range(10):
    print(losuj_haslo(12))