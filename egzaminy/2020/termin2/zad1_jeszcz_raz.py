from zad1testy import runtests
#f(i,x)-min liczba skoków do pola i z energią x
#f(i,x)=min(f(i+k,x-k+E[i+k])
def f(i,x,F,E):
    #print(i,x)
    if i+x>=len(E)-1:
        return 1
    if F[i][x]!=10**10:
        return F[i][x]
    for j in range(1,x+1):
        F[i][x]=min(F[i][x],f(i+j,x-j+E[i+j],F,E)+1)
    return F[i][x]
def zbigniew(A):
    F=[[10**10for j in range(len(A))]for i in range(len(A))]
    n = len(A)
    #print(n)
    return f(0,A[0],F,A)


runtests(zbigniew)
