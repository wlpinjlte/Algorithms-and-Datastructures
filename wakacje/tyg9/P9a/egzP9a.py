from egzP9atesty import runtests

def ASD(T, p, Q, n):
    #print(Q)
    summ=0
    tab=[0for i in range(n)]
    for i in Q:
        if i[0]==0:
            if tab[i[1]]!=0:
                summ+=tab[i[1]]*T.get(i[1])
                tab[i[1]]=0
            T.set(i[1],T.get(i[1])+i[2])
        else:
            for j in range(i[1],i[2]+1):
                # summ+=T.get(j)
                tab[j]+=1
    for i in range(len(tab)):
        if tab[i]!=0:
            #print(tab[i])
            summ+=tab[i]*T.get(i)
    return summ




runtests(ASD, all_tests = True)

