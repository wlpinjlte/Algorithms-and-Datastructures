from egzP4atesty import runtests
#f(i)- maks mostów biorąc i-ty most(cofamy się tylko)(czyli że zbioru do i biorąc i)
#f(i)=max(f(k)+1)(k=0...i-1)
def f(i,T,F):
    #print(i)
    if i==0:
        return 0
    if F[i]!=-1:
        return F[i]
    for j in range(i):
        if T[j][0]<=T[i][0] and T[j][1]<=T[i][1]:
            F[i]=max(F[i],f(j,T,F)+1)
    return F[i]
def mosty ( T ):
    F=[-1 for i in range(len(T)+1)]
    T.insert(0,(0,0))
    maks=0
    T=sorted(T)
    #print(len(T))
    for i in range(len(T)):
        maks=max(f(i,T,F),maks)
    return maks

runtests ( mosty, all_tests=True )