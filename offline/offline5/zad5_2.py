from zad5testy import runtests

def suma(T):
    s=0
    for i in T:
       s+=i
    return s

def prze(T,F,j,i):
    for z in range(1,j+1):
        if i+z==len(T):
            break
        if T[i+z]!=0 or i+z==len(T)-1:
            F[i+z][j-z+T[i+z]]=min(F[i][j]+1,F[i+z][j-z+T[i+z]])

def plan(T):
    s=suma(T)
    F=[[10**3for i in range(s)]for j in range(len(T))]

    F[0][T[0]]=0

    for i in range(len(T)):
        if T[i] != 0:
            for j in range(s):
                if F[i][j]!=10**3:
                    prze(T,F,j,i)
    minn=10**10
    for i in range(s):
        if minn>F[len(T)-1][i]:
            minn=F[len(T)-1][i]
    print(minn)
    return [0]

runtests( plan, all_tests = True )