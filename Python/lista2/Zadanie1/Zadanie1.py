def rightside(k):
    for i in range(k):
        print(" "*k,"#"*k," "*k,"#"*k," "*k,"#"*k," "*k,"#"*k)
def leftside(k):
    for i in range(k):
        print("#" * k, " " * k, "#" * k, " " * k, "#" * k, " " * k, "#" * k," "*k)
def szachownica(n,k):
    for i in range(n):
        rightside(k)
        leftside(k)
szachownica(5,3)
