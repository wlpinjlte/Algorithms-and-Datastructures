from egzP5atesty import runtests 

def inwestor ( T ):
    maks=0
    for i in range(len(T)):
        min=T[i]
        for j in range(i,len(T)):
            if min>T[j]:
                min=T[j]
            maks=max(maks,min*(j-i+1))
    return maks

runtests ( inwestor, all_tests=True )