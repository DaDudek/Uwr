szyfrogramy=[]
polskie_slowa=dict()


for lines in open("szyfrogramy.txt"):
    tmp = []
    for words in lines.split(" ")[:-1]:
            tmp.append(words)
    szyfrogramy.append(tmp)

"""tworze lista szyfrogramow z pliku"""

for word in open("slowa.txt"):
    word=word.strip()
    if len(word) not in polskie_slowa:
        polskie_slowa[len(word)]=[]
        polskie_slowa[len(word)].append(word)
    else:
        polskie_slowa[len(word)].append(word)

"""wczytuje polskie słowa"""


def permuts(word):
    counter = 1
    result = ""
    dict_of_letter = dict()
    for letter in word:
        if letter not in dict_of_letter:
            dict_of_letter[letter] = counter
            counter=counter+1
        result=result+str(dict_of_letter[letter])+"-"
    result=result[:-1]
    return result


"""kod z ostatniego wykładu"""


def latwe_szyfry(zaszyfrowane):
    wynik=[]
    for words in zaszyfrowane:
        perms=permuts(words)
        tmp=[]
        for e in polskie_slowa[len(words)]:
            if permuts(e)==perms:
                tmp.append(e)
        wynik.append(tmp)
    return wynik


"""biorę zaszyfrowane słowo sprawdzam jego postać permutacyjną i szukam innego z tą samą w zbiorze """


def srednie_szyfry(zaszyfrowane):
    wynik = []
    szyfr=dict()
    for words in zaszyfrowane:
        perms = permuts(words)
        tmp = []
        for e in polskie_slowa[len(words)]:
            if permuts(e) == perms:
                tmp.append(e)
                for i in range(len(e)):
                    if words[i] in szyfr:  # znajomość litery jednoznacznie wyznacza kolejne wystąpienia muszą być takie
                        if e[i]!=szyfr[words[i]]:
                            tmp.remove(e)
                            break

        if len(tmp)==1:
            for i in range(len(words)):
                szyfr[words[i]]=tmp[0][i]
        wynik.append(tmp)
    return wynik


"""sprawdzam czy jakieś słowo ma unikalną postać perm i jeśli tak to wartości liter z niego są jednoznacze"""
for x in latwe_szyfry(szyfrogramy[3]):
    print(x)
print()
for x in latwe_szyfry(szyfrogramy[6]):
    print(x)
print()
for x in srednie_szyfry(szyfrogramy[2]):
    print(x)