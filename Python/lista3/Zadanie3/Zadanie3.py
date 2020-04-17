def usun_nawiasy(slowo):
    tekst=""
    lista=list(slowo)
    i=0
    while i< len(lista):
        if (lista[i]=="("):
            while(lista[i]!=")"):
               i=i+1
        if lista[i]!= ")":
            tekst=tekst+lista[i]
        i=i+1
    print(tekst)
usun_nawiasy("(testc) (dfsfsdf) (sdad ) Ala ma kota (perskiego) tralalala! (kolejne)(tescik) testy")
