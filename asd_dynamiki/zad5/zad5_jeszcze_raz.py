from zad5ktesty import runtests
#f(i,j)-maks zysk z przydziału i,j
#f(i,j)=max(A[i]+min(f(i+1,j-1),f(i+2,j)),A[j]+min(f(i+1,j-1),f(i,j-2)))
def f(i,j,F,A):
    if F[i][j]!=-1:
        return F[i][j]
    if i==j:
        F[i][i]=A[i]
        return A[i]
    if j==i+1:
        F[i][i+1]=max(A[i],A[i+1])
        return max(A[i],A[i+1])
    F[i][j]=max(A[i]+min(f(i+1,j-1,F,A),f(i+2,j,F,A)),A[j]+min(f(i+1,j-1,F,A),f(i,j-2,F,A)))
    return F[i][j]
def garek ( A ):
    F=[[-1for j in range(len(A))]for i in range(len(A))]
    return f(0,len(A)-1,F,A)
runtests ( garek )