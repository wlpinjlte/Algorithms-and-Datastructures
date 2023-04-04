from egzP4atesty import runtests 
#brut
wynik=0
def f(i,T,l,p,m):
    global wynik
    if i==len(T):
        return
    if T[i][0]>=l and T[i][1]>=p:
        wynik=max(wynik,m+1)
        f(i+1,T,T[i][0],T[i][1],m+1)
    f(i+1,T,l,p,m)
def mosty ( T ):
    global wynik
    T=sorted(T)
    #print(T)
    wynik=0
    f(0,T,0,0,0)
    return wynik

runtests ( mosty, all_tests=True )