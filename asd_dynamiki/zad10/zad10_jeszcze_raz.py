from zad10ktesty import runtests
#f(i)-min liczba dywanów z i m^2
#f(i)=min(f(i-j^2)+1)(j=1...sqrt(i))
roz=[]
def f(i,F):
    if F[i]!=10**10:
        return F[i]
    j=1
    while j*j<=i:
        if F[i]>f(i-j*j,F)+1:
            F[i]=min(f(i-j*j,F)+1,F[i])
            roz[i]=(i-j*j,j)
        j+=1
    return F[i]
def dywany ( N ):
    global roz
    roz=[None for i in range(N+1)]
    F=[10**10 for i in range(N+1)]
    F[0]=0
    F[1]=1
    doc=[]
    f(N,F)
    tmp=N
    while roz[tmp]!=None:
        doc.append(roz[tmp][1])
        tmp=roz[tmp][0]
    return doc


runtests(dywany)