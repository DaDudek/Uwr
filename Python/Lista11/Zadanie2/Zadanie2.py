import itertools
xs = 8* "x" + 8*"y" + 8*"z" + 8*"0" + 8*"1"
combo = (list(itertools.combinations(xs, 8)))
table_of_truth = [[0, 0, 0, 0], [0, 0, 0, 1], [0, 1, 0, 1], [0, 1, 1, 0], [1, 0, 0, 0], [1, 0, 1, 1,], [1, 1, 0, 1], [1, 1, 1, 1]]
table_of_score = [0, 1, 1, 0, 0, 1, 1, 1]


def test(x):
    if x[2]:
        w = x[1]
    else:
        w = x[0]

    if x[5]:
        w2 = x[4]
    else:
        w2 = x[3]

    if x[6] or x[7]:
        return w2
    else:
        return w

score = []
for el in combo:
    if len(el) < 8:
        continue
    flaga = True
    for option in table_of_score:
        ustawienie = []
        licznik = 0
        for letter in el:
            if letter == "x":
                ustawienie.append(table_of_truth[licznik][0])
            if letter == "y":
                ustawienie.append(table_of_truth[licznik][1])
            if letter == "z":
                ustawienie.append(table_of_truth[licznik][2])
            if letter == "1":
                ustawienie.append(1)
            if letter =="0":
                ustawienie.append(0)
            licznik += 1
        if option != test(ustawienie):
            flaga = False
    if flaga:
        score.append(el)

print(score)