#rozwiązanie działa na opierając się na funkcji F(i,w)-maksymalna pojemność biorąc budynek i z budzetem w F(i,w)=maks(j=0..i-1)(F(j,w-T[i][3])+(T[i][2]-T[i][1])*T[i][3]) gdzie jest warunek by koniec bundyku i był później niż koniec budynku j wynik to maks(i=0...n-1)(F[i][p]) oczywiście sortujemy liste wejściową po konicach akademików(quicksortem)a wynik odczytujemy z Funkcji F biorąc maks(F[i][w]) jeżeli warunek na nienachodzenie akademików jest spełniony złozoność O(nlogn+n^2p+n^3)
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

def plecak(i,w,F,T):
    if F[i][w]!=-1:
        return F[i][w]
    m=0
    if w-T[i][3]<0:
        F[i][w]=0
        return F[i][w]
    for j in range(i):
        if T[j][2]<T[i][1]:
            pom=plecak(j,w-T[i][3],F,T)
            if m<pom:
                m=pom
    F[i][w]=m+(T[i][2]-T[i][1])*T[i][0]
    return F[i][w]

def znaj_index(T,x):
    for i in range(len(T)):
        if T[i]==x:
            return i

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
            maksi=i
    maks_w=znaj_index(T_p,T[maksi])
    #print(maks)
    pocz=T[maksi][1]
    p=p-T[maksi][3]
    tab.append(maks_w)

    flag=True
    while flag:
        maks=0
        flag=False
        for j in range(maksi):
            if pocz>T[j][2]:
                if maks<F[j][p]:
                    flag=True
                    maks=F[j][p]
                    tymi=j
                    maks_w=znaj_index(T_p,T[j])
        if flag:
            maksi=tymi
            tab.append(maks_w)
            p=p-T[maksi][3]
            pocz=T[maksi][1]

    return tab

runtests( select_buildings )