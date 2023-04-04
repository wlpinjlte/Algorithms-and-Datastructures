from zad3ktesty import runtests
import sys
sys.setrecursionlimit(3000)
#f(i)-najmniejsza k-suma do i biorąc elemnt i
#f(i)=min(T[i]+f(i-j))(j=1..k)
def f(T,k,i,F):
    #print(1,end='')
    if i<0:
        return 0
    if F[i]!=-1:
        return F[i]
    #pom=T[i]+f(T,k,i-1,F)
    pom=10**10
    for j in range(1,k+1):
        temp=T[i]+f(T,k,i-j,F)
        if pom>temp:
            pom=temp
    F[i]=pom
    return F[i]


def ksuma( T, k ):
    #print(T,k)
    F=[-1 for i in range(len(T))]
    F[0]=T[0]
    min=10**10
    for i in range(len(T)-k,len(T)):
        #print(1)
        f(T,k,i,F)
        if F[i]<min:
            min=F[i]
    #print(F)
    return min
    
runtests ( ksuma )