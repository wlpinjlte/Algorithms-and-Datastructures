from egzP7btesty import runtests 


def ogrod( S, V ):
    maks=0
    for i in range(len(S)):
        czy_jest=[0for z in range(len(V))]
        czy_jest[S[i]-1]=1
        tmp=V[S[i]-1]
        maks=max(maks,tmp)
        for j in range(i+1,len(S)):
            if czy_jest[S[j]-1]==1:
                tmp-=V[S[j]-1]
                czy_jest[S[j]-1]+=1
            elif czy_jest[S[j]-1]==0:
                tmp+=V[S[j]-1]
                czy_jest[S[j]-1]+=1
            maks=max(maks,tmp)
    return maks
    
runtests(ogrod, all_tests = True)