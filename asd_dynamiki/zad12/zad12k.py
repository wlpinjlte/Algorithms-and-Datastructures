from zad12ktesty import runtests 
#F[i][k]-minimalny termin zakoniczenia prac do i-tej gminy z k pracującymi firmami
#F[i][k]=min(max(suma(j+1,i),f(j,k-1)))(j=0...i)
def suma(j,i,T):
    sum=0
    for z in range(j,i):
        sum+=T[z]
    return sum
def f(i,k,F,T):
    if F[i][k]!=10**10:
        return F[i][k]
    if k==0:
        return 10**10
    temp=10**10
    for j in range(i):
        temp=min(temp,max(suma(j,i,T),f(j,k-1,F,T)))
    F[i][k]=temp
    return F[i][k]


def autostrada( T, k ):
    F=[[10**10 for j in range(k+1)]for i in range(len(T)+1)]

    for i in range(0,k+1):
        F[0][i]=0
    #F[0][1]=T[0]
    F[0][0]=0
    f(len(T),k,F,T)

    return F[len(T)][k]

runtests ( autostrada,all_tests=True )