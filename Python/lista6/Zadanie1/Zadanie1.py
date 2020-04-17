from turtle import *
import random
import numpy as np
from duze_cyfry import daj_cyfre

tracer(0,1)

    
BOK = 20

def move(x, y):
    pu()
    goto(x, y)
    pd()
    
def kwadracik(x, y, kolor):
    fillcolor([float(x) for x in kolor])
    move(BOK * x, BOK * y)
    begin_fill()
    for i in range(4):
        fd(BOK)
        rt(90)
    end_fill()

uzyte = set()
nowe = set()
for i in range(1000):
    x = random.randint(-30,30)
    y = random.randint(-30,30)
    c = random.randint(1,9)
    for j in range(5):
        for k in range(len(daj_cyfre(c)[j])):
            if daj_cyfre(c)[j][k] == '#':
               	nowe.add((x+k,y+5-j)) #dodaje te wspolrzedne x które maja # i poruszam się z góry na dół 
                      
    if len(nowe & uzyte) == 0:
        uzyte.update(nowe)
        
        kolor = np.random.rand(3)                      
        for xk, yk in nowe:
            kwadracik(xk, yk, kolor)
    update()
    nowe.clear()        

print ("Koniec!")            
input() 
