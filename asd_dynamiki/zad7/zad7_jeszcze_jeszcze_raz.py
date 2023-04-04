from zad7ktesty import runtests

def koszt(T,S,i,j):
    if i<0 or j<0 or i>len(T)-1 or j>len(T[0])-1 or T[i][j]==0 or S[i][j]==0:
        return 0
    #print(1)
    S[i][j]=0
    return T[i][j]+koszt(T,S,i,j-1)+koszt(T,S,i+1,j)+koszt(T,S,i,j+1)+koszt(T,S,i-1,j)

def plecak(F,i,k,Z,koszt):
    if k<0:
        return -10**10
    if i==len(F):
        return 0
    if F[i][k]!=-1:
        return F[i][k]
    F[i][k]=max(plecak(F,i+1,k,Z,koszt),plecak(F,i+1,k-koszt[i],Z,koszt)+Z[i])
    return F[i][k]


def ogrodnik(T, D, Z, l):
    S=[[1for j in range(len(T[0]))]for i in range(len(T))]
    F=[[-1 for j in range(l+1)]for i in range(len(D))]
    k=[0for i in range(len(D))]
    for i in range(len(D)):
        k[i]=koszt(T,S,0,D[i])
    #print(k)
    return plecak(F,0,l,Z,k)


runtests(ogrodnik)