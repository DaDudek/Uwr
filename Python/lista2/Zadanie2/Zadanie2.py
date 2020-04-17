def kwadratUp(n):
    print("*"*(2*n+1))
    for i in range(n-1):
        a=i*2
        b=2*n-3-a
        print("*"," "*i,"*"," "*b,"*"," "*i,"*",sep="")

def kwadratMid(n):
    print("*"," "*(n-1),"*"," "*(n-1),"*",sep="")

def kwadratDown(n):
    x = n-2
    y = 1
    for i in range(n-1,0,-1):
        print("*"," "*x,"*"," "*y,"*"," "*x,"*",sep="")
        x=x-1
        y=y+2
    print("*" * (2 * n + 1))
def kwadrat(n):
    kwadratUp(n)
    kwadratMid(n)
    kwadratDown(n)

kwadrat(6)
