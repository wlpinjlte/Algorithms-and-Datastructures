from egz1btesty import runtests

def wys(T):
    if T==None:
        return 0
    return max(wys(T.left)+1,wys(T.right)+1)

def liscieOdPoziomu(tab,T,aktP):
    if T==None:
        return
    tab[aktP]+=1
    liscieOdPoziomu(tab,T.left,aktP+1)
    return liscieOdPoziomu(tab,T.right,aktP+1)

def zerowanie(T):
    if T==None:
        return
    T.x=0
    zerowanie(T.left)
    return zerowanie(T.right)

def dfs(T,doc,akt):
    if T==None:
        return 0
    if doc==akt:
        T.x=1
        return 1
    T.x=max(dfs(T.right,doc,akt+1),dfs(T.left,doc,akt+1))
    return T.x

def ciecia(T):
    if T==None:
        return 0
    if T.x==0:
        return 1
    return ciecia(T.left)+ciecia(T.right)

def wyp(T):
    if T==None:
        return
    print(T.x)
    wyp(T.right)
    return wyp(T.left)

def wideentall( T ):
    h=wys(T)
    tab=[0 for i in range(h)]
    liscieOdPoziomu(tab,T,0)
    zerowanie(T)
    max=(1,0)
    for i in range(len(tab)):
        if max[0]<=tab[i]:
            max=(tab[i],i)
    print(tab,max)
    dfs(T,max[1],0)
    return ciecia(T)


runtests( wideentall, all_tests = False )