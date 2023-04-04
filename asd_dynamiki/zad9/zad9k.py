from zad9ktesty import runtests
from math import inf
#F(i,a,b)-maksymlna pojemność do i-tego samochodu przy objętość a podkładu 1 i objętość b podkładu 2
#F(i,a,b)=max(F(i-1,a-T[a],b),F(i-1,a,b-T[b])+1
def f(i,a,b,F,P):
    if F[i][a][b]!=0:
        return F[i][a][b]
    if i==len(P):
        return 0
    if a-P[i]>=0 and b-P[i]>=0:
        F[i][a][b] = max(f(i + 1, a - P[i], b, F, P), f(i + 1, a, b - P[i], F, P)) + 1
    elif a-P[i]>=0 and b-P[i]<0:
        F[i][a][b]=f(i +1, a - P[i], b, F, P)+1
    elif a-P[i]<0 and b-P[i]>=0:
        F[i][a][b]=f(i + 1, a, b - P[i], F, P)+1
    return F[i][a][b]

def prom(P, g, d):
    F=[[[0for z in range(d+1)]for j in range(g+1)]for i in range(len(P))]
    f(0,g,d,F,P)
    print(P,g,d)
    #print(F)
    #print(F[0][g][d])
    #input()
    i=0
    #odczytywanie rozwiązania
    aa=[]
    bb=[]
    a=g
    b=d
    while d-P[i]>=0 or g-P[i]>=0:
        if d-P[i]>=0 and g-P[i]<0:
            bb.append(i)
            d=d-P[i]
        elif g-P[i]>=0 and d-P[i]<0:
            aa.append(i)
            g=g-P[i]
        elif F[i+1][g-P[i]][d]>F[i+1][g][d-P[i]]:
            aa.append(i)
            g=g-P[i]
        else:
            d=d-P[i]
            bb.append(i)
        i+=1
    #print(F[0][a][b]-1)
    if F[0][a][b]-1 in aa:
        return aa
    return bb
runtests ( prom )