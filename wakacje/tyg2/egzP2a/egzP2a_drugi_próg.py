from egzP2atesty import runtests

def partiton(T,p,l):
    x=T[l][1]
    i=p-1
    for j in range(p,l):
        if T[j][1]<x:
            i+=1
            T[j],T[i]=T[i],T[j]
    T[l],T[i+1]=T[i+1],T[l]
    return i+1


def zdjecie(T, m, k):
    kubelki=[[]for i in range(m)]
    p=0
    it=0
    for i in range(m):
        for j in range(k+p):
            kubelki[p].append(T[it])
            it+=1
        p+=1
    doc=[]
    ii=[k*i+i-1 for i in range(m)]
    ii[0]=0
    kubelki.reverse()
    #print(kubelki)
    while len(kubelki[0])!=0:
        for i in range(len(kubelki)):
            if len(kubelki[i])!=0:
                doc.append(kubelki[i][0])
                kubelki[i].remove(kubelki[i][0])
                #del kubelki[i][0]
    #print(doc)
    return doc


runtests ( zdjecie, all_tests=False )