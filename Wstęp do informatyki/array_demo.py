from wdi import *

printf("Tablica jednowymiarowa\n")

N = 10
A = Array(N) # Tworzenie tablicy

for i in range(N):
  A[i] = i * i # Wpisywanie elementow do tablicy
  
for i in range(N):
  printf("A[%d] == %d\n", i, A[i])
  
printf("Tablica dwuwymiarowa\n")

M1 = 5
M2 = 4

B = Array(M1,M2) # Tworzenie tablicy dwuwymiarowej

for i in range(M1):
  for j in range(M2):
    B[i][j] = i * j # Zapis w tablicy dwuwymiarowej
    
for i in range(M1):
  for j in range(M2):  
    printf("B[%d][%d] == %d\n", i, j, B[i][j]) # odczyt z tablicy dwuwymiarowej
    
        
