from zad3ktesty import runtests

def f(i,k,T,F):
    if i-k<0:
        return T[i]
    if F[i]!=10**10:
        return F[i]
    for j in range(1,k+1):
        F[i]=min(F[i],f(i-j,k,T,F)+T[i])
    return F[i]

def ksuma( T, k ):
    F=[10**10for i in range(len(T))]
    maks=10**10
    for i in range(k):
        maks=min(maks,f(len(T)-i-1,k,T,F))
    return maks
runtests(ksuma)