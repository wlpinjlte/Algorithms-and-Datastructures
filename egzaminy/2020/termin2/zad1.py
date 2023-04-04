from zad1testy import runtests
#f(i,x)-minimalna liczba skoków by dostać się na pole i z zaspasem x(
#f(i,x)=min(f(i+k,x-k+T[k])+1)(k=1...x)

def maks(tab):
    s=0
    for i in tab:
        s+=i
    return s
def f(i,x,A,F):

    if i>=len(A)-1:
        #F[i][x]=0
        return 0
    if F[i][x]!=10**10:
        return F[i][x]
    for j in range(1,x+1):
        if i+j==len(A):
            break
        F[i][x]=min(F[i][x],f(i+j,x-j+A[i+j],A,F)+1)
    return F[i][x]

def zbigniew(A):
    makss=maks(A)
    F=[[10**10 for j in range(makss)]for i in range(len(A))]
    n = len(A)
    return f(0,A[0],A,F)


runtests(zbigniew)
