from zad5testy import runtests

def suma(T):
    s=0
    for i in T:
       s+=i
    return s

def prze(T,F,j,i,ind,indexi):
    if j + i >= len(T) - 1:
        F[len(T) - 1][j-((len(T) - 1)-i)] = min(F[i][j] + 1, F[len(T) - 1][j-((len(T) - 1)-i)])
    for z in range(indexi+1,len(ind)):
        if ind[z]>j+i:
            break
        F[ind[z]][j-(ind[z]-i)+T[ind[z]]]=min(F[i][j]+1,F[ind[z]][j-(ind[z]-i)+T[ind[z]]])

def plan(T):
    s=suma(T)
    F=[[10**10for i in range(s)]for j in range(len(T))]

    F[0][T[0]]=0
    ind=[]
    for i in range(len(T)):
        if T[i]!=0:
            ind.append(i)
    print(s,len(ind))
    for i in range(len(ind)):
        for j in range(s):
            if F[i][j]!=10**10:
                prze(T,F,j,ind[i],ind,i)
    minn=10**10
    for i in range(s):
        if minn>F[len(T)-1][i]:
            minn=F[len(T)-1][i]
    print(minn)
    return [0]

runtests( plan, all_tests = True )