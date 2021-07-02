'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
import numpy

temperatura = [9.7,8.4,7.9,8.7,7.5,7.8,8.6,8.4,8.8,8.0,6.7,8.4,8.2,6.8,8.4,7.2]
szerokosc = [51.11,
50.6647222222222,
50.2641666666667,
50.0613888888889,
50.0336111111111,
50.8741666666667,
51.7766666666667,
52.4083333333333,
51.9397222222222,
53.4380555555556,
54.3475,
53.125,
52.2322222222222,
53.1352777777778,
51.2480555555556,
53.7730555555556,
]
dlugosc = [17.0222222222222,
17.9269444444444,
19.0236111111111,
19.9383333333333,
22.0047222222222,
20.6333333333333,
19.4547222222222,
16.9341666666667,
15.505,
14.5422222222222,
18.6452777777778,
18.0011111111111,
21.0083333333333,
23.1455555555556,
22.5702777777778,
20.4761111111111,
]



matrixX = []
for i in range(len(dlugosc)):
    row = [1,dlugosc[i],szerokosc[i]]
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
    blad = score[0] + (score[1] * dlugosc[i]) + (score[2] * szerokosc[i]) - temperatura[i]
    print(blad*blad)


