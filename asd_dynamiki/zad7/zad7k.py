from zad7ktesty import runtests 
#F[i][j]-maks zysk biorąc z (0...i) zbioru przedmioty przy l litrach
#f(i,l)=maks(f(i-1,l),f(i-1,l-k[i])+z[i])
#problem plecakowy
#tutaj jeszcze dochodziło policzenie kosztu podlania co zrobione takim dfs ułomnym reszta czysty plecak
def koszt(T,S,i,j):
    if i<0 or j<0 or i>len(T)-1 or j>len(T[0])-1 or T[i][j]==0 or S[i][j]==0:
        return 0
    #print(1)
    S[i][j]=0
    return T[i][j]+koszt(T,S,i,j-1)+koszt(T,S,i+1,j)+koszt(T,S,i,j+1)+koszt(T,S,i-1,j)

def plecak(F,Z,i,K,l):
    if l<0 or i<0:
        return 0
    if l-K[i]<0:
        F[i][l]=plecak(F,Z,i-1,K,l)
        return F[i][l]
    if F[i][l]!=-1:
        return F[i][l]
    F[i][l]=max(plecak(F,Z,i-1,K,l),plecak(F,Z,i-1,K,l-K[i])+Z[i])
    return F[i][l]

def ogrodnik (T, D, Z, l):
    #print(T)
    K=[None for i in range(len(D))]
    S=[[-1for i in range(len(T[0]))]for j in range(len(T))]
    F=[[-1for i in range(l+1)]for j in range(len(D))]
    for i in range(len(K)):
        K[i]=koszt(T,S,0,D[i])
        #print(T[0][D[i]])
    #print(K)
    return plecak(F,Z,len(D)-1,K,l)

runtests( ogrodnik, all_tests=True )
