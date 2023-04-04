from egzP8atesty import runtests
import bisect
#f(i,k)-maks zysk zbioru i przy wzięci już k reklam
def bisect_left(a, x, lo=0, hi=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if a[mid][0][1] < x: lo = mid+1
        else: hi = mid
    return lo
def f(i,F,T,k):
    #print(i,k)
    if i==0:
        return 0
    if k==2:
        return 0
    if F[i][k]!=-1:
        return F[i][k]
    F[i][k]=max(f(i-1,F,T,k),f(min(bisect_left(T,T[i][0][0]-1),i-1),F,T,k+1)+T[i][1])
    return F[i][k]
def reklamy ( T, S, o ):
    T.insert(0,(0,0))
    S.insert(0,0)
    TT=[]
    SS=[]
    for i in range(len(T)):
        if T[i][1]<=o:
            TT.append(T[i])
            SS.append(S[i])
    for i in range(len(TT)):
        TT[i]=((TT[i]),SS[i])
    #print(SS)
    TT=sorted(TT,key=lambda x:x[0][1])
    #print(TT)
    F=[[-1for j in range(len(TT))]for i in range(len(TT))]
    elo=f(len(TT)-1,F,TT,0)
    #print(F)
    return elo
runtests ( reklamy, all_tests=True )