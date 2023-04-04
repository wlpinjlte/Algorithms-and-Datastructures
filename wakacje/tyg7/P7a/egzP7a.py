from egzP7atesty import runtests
minn=10**10
#brut
def f(i,T,k,tab):
    global minn
    if i==len(T):
        minn=min(minn,k)
        return
    for j in range(len(T)):
        if tab[j]==0:
            if j in T[i]:
                tab[j]=1
                f(i+1,T,k,tab)
                tab[j]=0
            else:
                tab[j]=1
                f(i+1,T,k+1,tab)
                tab[j]=0
    return
def akademik( T ):
    tab=[0for i in range(len(T))]
    global minn
    minn=10**10
    f(0,T,0,tab)
    return minn

runtests ( akademik )