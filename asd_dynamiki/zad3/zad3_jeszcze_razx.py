from zad3ktesty import runtests
#f(i)-minimalna k-suma biorąc i-ty element
#f(i)=min(f(i-j)+T[i])(j=1...k)
def f(i,T,k,F):
    #print(i)
    if i-k<0:
        return T[i]
    # if i<0:
    #     return 0
    if F[i]!=10**10:
        return F[i]
    for j in range(1,k+1):
        F[i]=min(F[i],f(i-j,T,k,F)+T[i])
    return F[i]

def ksuma( T, k ):
    minn=10**10
    F=[10**10 for i in range(len(T))]
    for i in range(k):
        minn=min(f(len(T)-1-i,T,k,F),minn)
    return minn
runtests(ksuma)