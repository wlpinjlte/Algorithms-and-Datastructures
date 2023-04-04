from zad3testy import runtests
from zad3EK import edmonds_karp
def fload(T):
    od=[[10**10 for j in range(len(T))]for i in range(len(T))]
    for i in range(len(T)):
        for j in range(len(T)):
            if T[i][j]!=0:
                od[i][j]=T[i][j]
    for z in range(len(T)):
        for i in range(len(T)):
            for j in range(len(T)):
                if od[i][j]>od[i][z]+od[z][j]:
                    od[i][j]=od[i][z]+od[z][j]
    return od
def build_graf(od,K,D):
    graf=[[0for j in range(len(od)+2)]for i in range(len(od)+2)]
    for i in range(len(od)):
        for j in range(len(od)):
            if od[i][j]>=D and ((K[i]=="B"and K[j]=='G')or(K[j]=='B'and K[i]=='G')):
                graf[i][j]=1
    for i in range(len(od)):
        if K[i]=="B":
            graf[len(od)][i]=1
        else:
            graf[i][len(od)+1] = 1
    return graf
def BlueAndGreen(T, K, D):
    print(T,K,D)
    od=fload(T)
    graf=build_graf(od,K,D)
    return edmonds_karp(graf,len(graf)-2,len(graf)-1)
runtests(BlueAndGreen)