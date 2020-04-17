file=open("wyniki_wyborow.tsv")
def read_file(file): # zwraca słownik nazwa parti-wynik w danym okregu, lista parti, ile mandatow w danym okregu
    i=0
    electoral_parties = dict()
    list_of_parties=[]
    list_of_mandates=[]
    for lines in file:
        if i==0:
            j=0
            for party in lines.split("\t"):

                if j>2 and j<len(lines.split("\t"))-1: #pierwsze 3 pola mnie nie interesują oraz ostatnie
                    electoral_parties[party]=[]
                    list_of_parties.append(party)
                j=j+1
        else:
            k=0
            for score in lines.split("\t"):
                if k==2:
                    list_of_mandates.append(score)
                if (k > 2 and k<len(lines.split("\t"))-1):  # pierwsze 3 pola mnie nie interesują
                    if score=="–":
                        score=0
                    electoral_parties[list_of_parties[k-3]].append(score)
                k=k+1
        i=i+1
    return electoral_parties, list_of_parties, list_of_mandates
def count_mandate(file):
    electoral_parties,list_of_parties,list_of_mandates=read_file(file)
    dict_of_mandates=dict()
    for parties in list_of_parties: #w tym miejscu zapisuje ile mandatow ma dana partia
        dict_of_mandates[parties]=0
    for counter in range(len(list_of_mandates)): # powtorzenie x razy rozdzielenia mandatow w danym okregu
        list_of_score=[]
        tmp=int(list_of_mandates[counter])+1
        for i in range(tmp): # dzielenie przez nieparzyste ilości mandatów(sainte - lague )
            if i%2==1:
                for parties in list_of_parties: #zmieniam przecinek na kropke zeby dobry format był
                    if "," in str(electoral_parties[parties][counter]):
                        score=float(electoral_parties[parties][counter].replace(",","."))
                    else:
                        score=float(electoral_parties[parties][counter])
                    list_of_score.append([score/(i),parties])
        list_of_score.sort(reverse=True) #odwracam tabele aby posortowac malejąco
        for j in range(int(list_of_mandates[counter])): # przypisuje odpowiednią ilość mandatów dla danej Partii
            tmp=dict_of_mandates[list_of_score[j][1]]
            dict_of_mandates[list_of_score[j][1]]=tmp+1
    print(dict_of_mandates)
count_mandate(file)