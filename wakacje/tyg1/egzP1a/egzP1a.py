from egzP1atesty import runtests 
#f(w,i)-min liczba liter by zapisac napis do miejsca i
def f(W,i,M,D,F):
    if W=='':
        return 0
    if F[i]!=10**10:
        return F[i]
    for j in D:
        if len(W)<len(M[j][1]):
            #print(M[j][1],"elo")
            continue
        #print(W[-len(M[j][1])],M[j][1], "   elo")
        if W[-len(M[j][1]):]==M[j][1]:
            #print(M[j][0])
            F[i]=min(F[i],f(W[:-len(M[j][1])],i-len(M[j][1]),M,D,F)+1)
    return F[i]
def zam(W,M):
    s=""
    for j in W:
        for i in M:
            if j==i[0]:
                s+=i[1]
    return s
def titanic( W, M, D ):
    s=zam(W,M)
    F=[10**10 for i in range(len(s)+1)]
    return f(s,len(s)-1,M,D,F)

runtests ( titanic, recursion=False )