#Mateusz Waga alogrytm jest zrobimy w n^4 f(i,j,d)-maks sniegu która można zebrac d dnia od i początku do j konica a wzór rekurencyjny F[i][j][d]=max(F[i][j][d],f(k+1,j,d+1,S,F)+S[k]-d,f(i,k-1,d+1,S,F)+S[k]-d)
from egz1atesty import runtests

def snow( S ):
    S=sorted(S,reverse=True)
    #print(S)
    counter=0
    suma=0
    for i in range(len(S)):
        if S[i]-counter<=0:
            break
        suma+=S[i]-counter
        counter+=1
    return suma

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )
