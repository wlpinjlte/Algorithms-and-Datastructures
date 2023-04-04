from egz3atesty import runtests

def snow( T, I ):
    I=sorted(I,key=lambda x:x[1])
    k=0
    for i in range(len(I)):
        pom=1
        for j in range(len(I)):
            if i!=j and I[j][0]<=I[i][1]<=I[j][1]:
                pom+=1
        k=max(k,pom)
    return k
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )
