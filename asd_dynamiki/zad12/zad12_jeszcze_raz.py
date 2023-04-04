from zad12ktesty import runtests
#f(i,k)-min dni zeby otworzyć do drog i przy k firmach
#f(i,k)=min(max(suma(j+1,i),f(j,k-1))(j=0...i-1
def summ(i,j,T):
    s=0
    for z in range(i,j+1):
        s+=T[z]
    return s
def f(i,k,F,T):
    # if k==0:
    #     return 10**10
    if i==0:
        return 0
    if k==1:
        F[i][k]=summ(0,i,T)
        return F[i][k]
    if F[i][k]!=10**10:
        return F[i][k]
    for j in range(i):
        F[i][k]=min(max(summ(j+1,i,T),f(j,k-1,F,T)),F[i][k])
    return F[i][k]
def autostrada( T, k ):
    T.insert(0,0)
    #print(T)
    F=[[10**10for j in range(k+1)]for i in range(len(T))]
    #print(summ(0,len(T)-1,T))
    return f(len(T)-1,k,F,T)

runtests(autostrada)