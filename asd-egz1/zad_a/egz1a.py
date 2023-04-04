#Mateusz Waga alogrytm jest zrobimy w n^4 f(i,j,d)-maks sniegu która można zebrac d dnia od i początku do j konica a wzór rekurencyjny F[i][j][d]=max(F[i][j][d],f(k+1,j,d+1,S,F)+S[k]-d,f(i,k-1,d+1,S,F)+S[k]-d)
from egz1atesty import runtests
#f(i,j,d)-maks sniegu która można zebrac d dnia od i początku do j konica
#f(i,j,d)=max(
def f(i,j,d,S,F):
    if F[i][j][d]!=-1:
        #print(1)
        return F[i][j][d]
    if i>j:
        return 0
    F[i][j][d]=0
    for k in range(i,j+1):
        if S[k]-d<=0:
            continue
        F[i][j][d]=max(F[i][j][d],f(k+1,j,d+1,S,F)+S[k]-d,f(i,k-1,d+1,S,F)+S[k]-d)
    return F[i][j][d]
def maxxx(S):
    maxx=0
    for i in S:
        maxx=max(i,maxx)
    return maxx
def snow( S ):
    #S=[324122,42143,1,423,214,12,42,21,2,3245,124321,24124242,241421,421421241,11244124,2123451,423321,43124242112,4124442,21243241,451221441,22,22,1,1,4231,24]
    print(maxxx(S))
    #S=[1]
    F=[[[-1for z in range(len(S)+1)]for j in range(len(S)+1)]for i in range(len(S)+1)]
    return f(0,len(S)-1,0,S,F)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = False )
