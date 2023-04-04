from zad5ktesty import runtests
#F(i,j)-maks zysk z przydziału od i do j
#paczka mentosów
def f(i,j,F,A):
    if F[i][j]!=-1:
        return F[i][j]
    if i+1==j:
        return max(A[i],A[j])
    if i==j:
        return A[i]
    F[i][j]=max(A[i]+min(f(i+2,j,F,A),f(i+1,j-1,F,A)),A[j]+min(f(i+1,j-1,F,A),f(i,j-2,F,A)))
    return F[i][j]
def garek ( A ):
    F=[[-1for j in range(len(A))]for i in range(len(A))]
    return f(0,len(A)-1,F,A)

runtests ( garek )