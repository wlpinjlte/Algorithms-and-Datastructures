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

def znaj_index(T,x):
    for i in range(len(T)):
        if T[i]==x:
            return i

def plecak(i,w,b,F,T):
    if i<0:
        return 0
    if F[i][w]!=-1:
        return F[i][w]
    if w-T[i][3]<0:
        F[i][w]=0
        return F[i][w]
    if b>=T[i][1]:
        return plecak(i-1,w,b,F,T)
    F[i][w]=max(plecak(i-1,w,b,F,T),plecak(i-1,w-T[i][3],T[i][2],F,T)+(T[i][2]-T[i][1])*T[i][0])
    return F[i][w]

def select_buildings(T, p):
    qs(T, 0, len(T) - 1)
    F = [[-1 for j in range(p + 1)] for i in range(len(T))]
    # print(T)
    maks = 0
    tab = []

    for i in range(len(T)):
        pom = plecak(i, p,0, F, T)
        if maks < pom:
            maks = pom
    # for i in range(len(T)):
    #     for j in range(p+1):
    #         print(F[i][j])
    print(maks)
    return [0]
runtests( select_buildings )