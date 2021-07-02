import numpy

temperatura = [9.7,8.4,7.9,8.7,7.5,7.8,8.6,8.4,8.8,8.0,6.7,8.4,8.2,6.8,8.4,7.2]
wysokosc = [130,176,301,288,292,330,220,102,143,65,90,70,100,140,200,120]

srednia_temp = 0
srednia_wys = 0
for i in range(len(temperatura)):
    srednia_temp = srednia_temp + temperatura[i]
    srednia_wys = srednia_wys + wysokosc[i]
    
srednia_wys = srednia_wys/16 
srednia_temp = srednia_temp / 16 

suma= 0
suma1 = 0

# wzor to sum(a * b) / sum (c)

for i in range(len(temperatura)):
    a = wysokosc[i] - srednia_wys
    b = temperatura[i] - srednia_temp
    suma = suma + (a*b)
    c = a * a
    suma1 = suma1 + c
    
Beta1 = suma/suma1
Beta0 = srednia_temp - (srednia_wys * Beta1)
print(Beta0,Beta1)


for i in range(len(temperatura)):
    blad = Beta0 + (Beta1 *wysokosc[i]) - temperatura[i] 
print(blad*blad)

    
#Wersja macierzowa

matrixX = []
for i in range(len(wysokosc)):
    row = [1,wysokosc[i]]
    matrixX.append(row)
    
X = numpy.array(matrixX)
Y = numpy.array(temperatura)
XTransp = X.T
XMultTransp =XTransp.dot(X)
XInverse = numpy.linalg.inv(XMultTransp)
tmp = XInverse.dot(XTransp)
score = tmp.dot(Y)
print(score)
    
for i in range(16):
    blad = score[0] + (score[1] * wysokosc[i])  - temperatura[i]
print(blad*blad)
