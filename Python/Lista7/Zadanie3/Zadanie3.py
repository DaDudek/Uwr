def usun_zle_znaki(s):
    znaki = ['.', '!', '?', ',', '-', '—', ':', '(', ')', '"', '\'', '\n', '\t', '/']
    for z in znaki:
        s = s.replace(z,'')
    s=s.lower()
    return s

slownik_slow = {}
for wiersz in open('lalka-tom-pierwszy.txt'):
        wiersz = usun_zle_znaki(wiersz)
        for slowo in wiersz.split():
              if slowo not in slownik_slow:
                slownik_slow[slowo] = 1
              else:
                slownik_slow[slowo] += 1


alfa = 2
f = []
for s in slownik_slow:
    ilosc_wystapien = slownik_slow[s]
    waga = (len(s)**alfa)*(ilosc_wystapien)
    f.append((s, ilosc_wystapien, waga))
f.sort(key=lambda x: x[2])
print(f[-10:])

