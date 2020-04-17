from turtle import *
from random import *
kolory=["red","green","yellow","orange","purple","pink","blue"]

def kwadrat(bok):
    begin_fill()
    for i in range(4):
      fd(bok)
      rt(90)
    end_fill()
 
def murek(s,bok):
  licznik=0
  for a in s:
     if a == 'f':
         kwadrat(bok)
         fd(bok)
     elif a == 'b': #edytuje ten
         color("black",kolory[licznik%6])
         licznik=licznik+1
         kwadrat(bok)
         fd(bok)         
     elif a == 'l':
         bk(bok)
         lt(90)
     elif a == 'r':
        rt(90)
        fd(bok)

        
color('black', 'yellow')

ht()
tracer(0,0) # szybkie rysowanie     
#murek('fffffffffrfffffffffflfffffffffrfffffl',10)   
#murek(4 * 'fffffr', 14)
#murek("bbblbbb",20)
murek("bbbbbbblblbbbbbbrbrbbbbbb"+2*"lblbbbbbbrbrbbbbbb",15)
pu()
goto(300,300)
pd()
murek("bblbblbbblbbbblbbbbblbbbbbblbbbbbbblbbbbbbbblbbbbbbbbb",15)
#lblb
input()    
update() # uaktualnienie rysunku

