from zad10ktesty import runtests
#F[n]-mnimalna liczba dywanów które potrzeba zeby zapełnić n m^2
#F[n]=min(F[n-i^2]+1)(i=1...sqrt(n))
def f(n,F):
    if F[n]!=10**10:
        return F[n]
    i=1
    while n-i**2>=0:
        F[n]=min(F[n],f(n-i**2,F)+1)
        i+=1
    return F[n]
def dywany ( N ):
    #Tutaj proszę wpisać własną implementację
    F=[10**10 for i in range(N+1)]
    F[0]=0
    F[1]=1
    doc=[]
    f(N, F)
    #print(F)
    while N!=0:
        i=1
        minn=10**10
        ind=1
        while N - i ** 2 >= 0:
            if minn>F[N - i ** 2]:
                ind=i
                minn=F[N - i ** 2]
            i+=1
        N=N-ind*ind
        doc.append(ind)
    #print()
    return doc


runtests( dywany )

