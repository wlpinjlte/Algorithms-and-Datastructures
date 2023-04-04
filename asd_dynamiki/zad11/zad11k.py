from zad11ktesty import runtests
#f(i,a,b)-min róźnica przy załadunku a i załunku b do i-tego elemnetu
#przez sume prefiksową nie potrzebujemy drugiego parametru bo wiemy że b=sum[i]-a
#pierwsze podejście bez sum prefiksowych
def f(i,a,b,T,F):
    if F[i][a][b]!=10**10:
         return F[i][a][b]
    if i==len(T):
        return abs(a-b)
    F[i][a][b]=min(f(i+1,a+T[i],b,T,F),f(i+1,a,b+T[i],T,F))
    return F[i][a][b]

#z sumami prefiksowymi(właściwe)
def f2(i,a,T,F,S):
    if i==len(T):
        return abs(S[i-1]-2*a)
    if F[i][a]!=10**10:
        return F[i][a]
    F[i][a]=min(f2(i+1,a+T[i],T,F,S),f2(i+1,a,T,F,S))
    return F[i][a]
#bez dynamika
def f3(i,a,T,S):
    if i==len(T):
        return abs(S[i-1]-2*a)
    return min(f3(i+1,a+T[i],T,S),f3(i+1,a,T,S))
#maksymalna wartość + sumy prefiksowe
def maks(T,p):
    sum=0
    for i in T:
        sum += i
        p.append(sum)
    return sum

def kontenerowiec(T):
    #Tutaj proszę wpisać własną implementację
    prefiks=[]
    n=maks(T,prefiks)
    F=[[10**10for z in range(n+1)]for i in range(len(T))]

    return f2(0,0,T,F,prefiks)

runtests ( kontenerowiec )