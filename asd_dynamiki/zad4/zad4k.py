from zad4ktesty import runtests
#F(i,j)-najmniejszy koszt dosatnia się na i,j pole
#F(i,j)=min(F[i-1][j]+T[i][j],F[i][j-1]+T[i][j])
def falisz ( T ):
    F=[[-1 for j in range(len(T))]for i in range(len(T))]
    F[0][0]=T[0][0]
    for i in range(1,len(T)):
        F[0][i]=F[0][i-1]+T[0][i]
        F[i][0]=F[i-1][0]+T[i][0]
    #print(F)
    for i in range(1,len(T)):
        for j in range(1,len(T)):
            F[i][j]=min(F[i-1][j]+T[i][j],F[i][j-1]+T[i][j])
    #print(F)
    return F[len(T)-1][len(T)-1]

runtests ( falisz )
