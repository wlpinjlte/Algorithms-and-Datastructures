from zad4testy import runtests

def particion(tab,a,b):
    x=tab[b][2]
    i=a-1
    for j in range(a,b):
        if tab[j][2]<=x:
            i+=1
            tab[i],tab[j]=tab[j],tab[i]
    tab[i+1],tab[b]=tab[b],tab[i+1]
    return i+1

def qs(tab,a,b):
    if b-a>0:
        q=particion(tab,a,b)
        qs(tab,a,q-1)
        qs(tab,q+1,b)

def poj(T):
    return (T[2]-T[1])*T[0]

def plecak(i,k,F,T):
    #print(i)
    if F[i][k] != -1: return F[i][k]
    maks = 0
    w = k - T[i][3]
    if w<0:
        return 0
    for j in range(0, i):
        if T[j][2] < T[i][1]:
            maks = max(maks, plecak(j, w, F, T))
    F[i][k] = (T[i][2]-T[i][1])*T[i][0] + maks
    return F[i][k]

def select_buildings(T,p):
    T_p=T.copy()
    qs(T,0,len(T)-1)
    F = [[-1 for j in range(p+1)] for i in range(len(T))]
    #print(T)
    maks=0
    tab=[]
    for i in range(len(T)):
        pom=plecak(i,p,F,T)
        if maks<pom:
            maks=pom
    print(maks)

    return tab

runtests( select_buildings )
