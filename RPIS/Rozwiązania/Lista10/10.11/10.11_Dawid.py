'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

import numpy

X = [1,3,4,6,8,9,11,14] # X
Y = [1,2,4,4,5,7,8,9] # Y

srednia_Y = 0
srednia_X = 0
for i in range(len(Y)):
    srednia_Y = srednia_Y + Y[i]
    srednia_X = srednia_X + X[i]
    
srednia_X = srednia_X / len(Y)
srednia_Y = srednia_Y / len(X) 

suma= 0
suma1 = 0

# wzor to sum(a * b) / sum (c)

for i in range(len(Y)):
    a = X[i] - srednia_X
    b = Y[i] - srednia_Y
    suma = suma + (a*b)
    c = a * a
    suma1 = suma1 + c
    
Beta1 = suma/suma1
Beta0 = srednia_Y - (srednia_X * Beta1)
print(Beta0,Beta1) # wynik

blad1 = []
for i in range(len(Y)):
    blad = Beta0 + (Beta1 *X[i]) - Y[i] 
    blad1.append(blad*blad)


    
#Wersja macierzowa

matrixX = []
for i in range(len(X)):
    row = [1,X[i]]
    matrixX.append(row)
    
Xt = numpy.array(matrixX)
Yt = numpy.array(Y)
XTransp = Xt.T
XMultTransp =XTransp.dot(Xt)
XInverse = numpy.linalg.inv(XMultTransp)
tmp = XInverse.dot(XTransp)
score = tmp.dot(Yt) # wynik
print(score)

blad2 = []
for i in range(len(Y)):
    blad = score[0] + (score[1] * X[i])  - Y[i]
    blad2.append(blad*blad)
    
#print(blad1)
#print(blad2)
