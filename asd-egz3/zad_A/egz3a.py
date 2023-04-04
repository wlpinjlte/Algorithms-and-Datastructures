from egz3atesty import runtests

def snow( T, I ):
    tab=[0for i in range(T+1)]
    maxx=0
    for i in I:
        for j in range(i[0],i[1]+1):
            tab[j]+=1
            maxx=max(maxx,tab[j])
    return maxx

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = False )
