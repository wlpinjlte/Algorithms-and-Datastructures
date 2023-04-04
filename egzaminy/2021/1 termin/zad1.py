from zad1testy import runtests
def partiton(T,a,b,p):
    x=T[b][p]
    i=a-1
    for j in range(a,b):
        if T[j][p]<x:
            i+=1
            T[j],T[i]=T[i],T[j]
    T[i+1],T[b]=T[b],T[i+1]
    return i+1
def qs(T,a,b,p):
    if b>a:
        q=partiton(T,a,b,p)
        qs(T,q+1,b,p)
        qs(T,a,q-1,p)

def chaos_index( T ):
    for i in range(len(T)):
        T[i]=(i,T[i])
    T=sorted(T,key=lambda x:x[1])
    #qs(T,0,len(T)-1)
    print(T)
    k=0
    for i in range(len(T)):
        k=max(k,abs(T[i][0]-i))
    return k


runtests( chaos_index )
