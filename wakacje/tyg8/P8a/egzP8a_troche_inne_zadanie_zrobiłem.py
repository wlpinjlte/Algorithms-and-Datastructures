from egzP8atesty import runtests 
#f(i)-maks zysk biorąc reklame i
#f(i)=max(S[i]+f(j))(gdzie j=0..i-1)(spełniający warunek nie nakładanie się czyli początek i>=koniec j)
#ogolne rozwiązanie jak liczy sie najwieksza ilość
#O(n^2)
def f(i,T,F):
    if i==0:
        return 0
    if F[i]!=-1:
        return F[i]
    for j in range(i):
        if T[j][0][1]<T[i][0][0]:
            F[i]=max(F[i],T[i][1]+f(j,T,F))
    return F[i]
def reklamy ( T, S, o ):
    T.insert(0,(0,0))
    S.insert(0,0)
    TT=[]
    SS=[]
    for i in range(len(T)):
        if T[i][1]<=o:
            TT.append(T[i])
            SS.append(S[i])
    for i in range(len(TT)):
        TT[i]=((TT[i]),SS[i])
    #print(T)
    #print(o)
    TT=sorted(TT,key=lambda x:x[0][1])
    #print(T)
    #print(S)
    maks=0
    F=[-1for i in range(len(TT))]
    #print(TT)
    for i in range(len(TT)):
        maks=max(f(i,TT,F),maks)
    #print(o)
    return maks

runtests ( reklamy, all_tests=True )