file=open("wyniki_wyborow.tsv")
def read_file(file): # zwraca słownik nazwa parti-wynik w danym okregu, lista parti, ile mandatow w danym okregu
    i=0
    electoral_parties = dict()
    list_of_parties=[]
    list_of_mandates=[]
    for lines in file:
        if i==0: #wczytuje jakie partie braly udzial w wyborach
            j=0
            for party in lines.split("\t"):
                if j>2 and j<len(lines.split("\t"))-1: #pierwsze 3 oraz ostatnie pole mnie nie interesują
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
                    electoral_parties[list_of_parties[k-3]].append(score) # wynik danej parti jest przesuniety o 3 podczas wczytywania
                k=k+1
        i=i+1
    return electoral_parties, list_of_parties, list_of_mandates
def count_mandate(file):
    electoral_parties,list_of_parties,list_of_mandates=read_file(file) #slownik lista lista
    dict_of_mandates=dict()
    for parties in list_of_parties: #w tym miejscu zapisuje ile mandatow ma dana partia
        dict_of_mandates[parties]=0
    for counter in range(len(list_of_mandates)): # powtorzenie dla kazdego okregu rozdzielenia mandatow w danym okregu
        list_of_score=[]
        tmp=int(list_of_mandates[counter])+1 # potrzebuje o jeden wiecej aby dobrze iterować po tym
        for i in range(tmp): # dzielenie przez ilość mandatów(d'hondt)
            for parties in list_of_parties: #zmieniam przecinek na kropke zeby dobry format był
                if "," in str(electoral_parties[parties][counter]): #wynik danej parti w danym okręgu
                    score=float(electoral_parties[parties][counter].replace(",","."))
                else:
                    score=float(electoral_parties[parties][counter])
                list_of_score.append([score/(i+1),parties])
        list_of_score.sort(reverse=True) #odwracam tabele aby posortowac malejąco
        for j in range(int(list_of_mandates[counter])): # przypisuje odpowiednią ilość mandatów dla danej Partii
            tmp=dict_of_mandates[list_of_score[j][1]] # list_of_score[j][1] zwraca mi nazwe parti
            dict_of_mandates[list_of_score[j][1]]=tmp+1
    print(dict_of_mandates)
count_mandate(file)