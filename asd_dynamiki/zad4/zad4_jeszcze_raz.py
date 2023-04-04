from zad4ktesty import runtests
#f(i,j)-minimalny koszt dotarcia na pole i j
#f(i,j)=min(f(i-1,j),f(i,j-1))+T[i][j]
def f(i,j,T,F):
    if F[i][j]!=-1:
        return F[i][j]
    F[i][j]=min(f(i-1,j,T,F),f(i,j-1,T,F))+T[i][j]
    return F[i][j]
def falisz(T):
    F=[[-1 for j in range(len(T))]for i in range(len(T))]
    F[0][0]=T[0][0]
    for i in range(1,len(T)):
        F[0][i]=T[0][i]+F[0][i-1]
        F[i][0]=T[i][0]+F[i-1][0]
    return f(len(T)-1,len(T)-1,T,F)
runtests(falisz)