from egzP8atesty import runtests

def reklamy ( T, S, o ):
    #T.insert(0,(0,0))
    #S.insert(0,0)
    TT=[]
    SS=[]
    for i in range(len(T)):
        if T[i][1]<=o:
            TT.append(T[i])
            SS.append(S[i])
    for i in range(len(TT)):
        TT[i]=((TT[i]),SS[i])
    TT=sorted(TT,key=lambda x:x[0][0])
    maks=0
    for i in range(len(TT)):
        maks=max(TT[i][1],maks)
        for j in range(i,len(TT)):
            if TT[j][0][0]>TT[i][0][1]:
                maks=max(TT[i][1]+TT[j][1],maks)
    return maks

runtests ( reklamy, all_tests=False )