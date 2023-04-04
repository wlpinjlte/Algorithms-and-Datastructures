from zad3testy import runtests
from zad3EK    import edmonds_karp

def fload(T):
    od=[[10**10 for j in range(len(T))]for i in range(len(T))]
    for i in range(len(T)):
        for j in range(len(T)):
            if i==j:
                od[i][j]=0
                continue
            if T[i][j]!=0:
                od[i][j]=T[i][j]
    for i in range(len(T)):
        for j in range(len(T)):
            for z in range(len(T)):
                if od[i][j]>od[i][z]+od[z][j]:
                    od[i][j] = od[i][z] + od[z][j]
    return od

def BlueAndGreen(T, K, D):
    print(T)
    od=fload(T)
    print(od)
    print(K)
    graf=[[0 for j in range(len(T)+2)]for i in range(len(T)+2)]
    for i in range(len(T)):
        for j in range(len(T)):
            if ((K[i]=='G' and K[j]=='B') or (K[i]=='B' and K[j]=='G')) and od[i][j]>=D:
                graf[i][j]=1
    for i in range(len(T)):
        if K[i]=='G':
            graf[len(T)][i]=1
        else:
            graf[i][len(T)+1] = 1
    return edmonds_karp(graf,len(T),len(T)+1)

runtests( BlueAndGreen )
