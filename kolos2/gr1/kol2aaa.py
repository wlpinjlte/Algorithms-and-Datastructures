from kol2atesty import runtests
#f(i)-minimalna gdy dojeżdza marian f(i)=min(tab[i]+g(i-j))   j=1..3
#g(i)-minimalna gdy dojeżdza Jacek  g(i)=min(f(i-j))    j=1..3
odn=[]
odn1=[]
def f(i,F,G,tab):
    global odn
    if i<0:
        return 10**10
    if F[i]!=10**10:
        return F[i]
    z=tab[i]
    ind=(-1)
    for j in range(1,4):

        if F[i]>z+g(i-j,F,G,tab):
            #print(1)
            F[i]=z+g(i-j,F,G,tab)
            ind=i-j
        z+=tab[i-j]
    odn[i]=ind
    return F[i]
def g(i,F,G,tab):
    global odn1
    if i<0:
        return 10**10
    if G[i]!=10**10:
        return G[i]
    ind=(-1)
    for j in range(1,4):
        if G[i]>f(i-j,F,G,tab):
            G[i]=f(i-j,F,G,tab)
            ind=i-j
    odn1[i]=ind
    return G[i]
def indeks(P,ile):
    z=-1
    for i in range(len(P)):
        if P[i][1]==True:
            z+=1
        if z==ile:
            return i
        #ile+=1
def drivers( P, B ):
    global odn,odn1
    PP=P.copy()
    tab=[]#tablica odległośc miedzy punktami kontrolnymi
    P.append((B,True))
    P=sorted(P,key=lambda x:x[0])
    ile=0
    for i in range(len(P)):
        if P[i][1]==True:
            tab.append(ile)
            ile=0
        else:
            ile+=1
    odn=[-1 for i in range(len(tab))]
    odn1=[-1 for i in range(len(tab))]
    F = [10 ** 10 for i in range(len(tab))]
    G = [10 ** 10 for i in range(len(tab))]
    G[0] = 0
    G[1] = 0
    G[2] = 0
    print(g(len(tab)-1,F,G,tab))
    od1=odn.copy()
    od2=odn1.copy()
    #odn1=odn.copy()
    F1 = [10 ** 10 for i in range(len(tab))]
    G1 = [10 ** 10 for i in range(len(tab))]
    odn = [-1 for i in range(len(tab))]
    odn1 = [-1 for i in range(len(tab))]
    G1[0]=0
    G1[1]=0
    G1[2]=0
    docc=[]
    #odn=[-1 for i in range(len(tab))]
    print(f(len(tab)-1,F1,G1,tab))
    if G[len(tab)-1]<=F1[len(tab)-1]:
        #print(1)
        i = len(tab) - 1
        doc = []
        print(od1)
        print(od2)
        while od2[i]>0:
            doc.append(od2[i])
            i=od2[i]
            if i<=0:break
            doc.append(od1[i])
            i=od1[i]
        for i in doc:
            docc.append(indeks(PP,i))
    else:
        i = len(tab) - 1
        doc = []
        print(odn)
        print(odn1)
        while odn[i] > 0:
            doc.append(odn[i])
            i = odn[i]
            print(i)
            if odn1[i]<=0:break
            doc.append(odn1[i])
            i=odn1[i]
            if i<=0:break
            print(i)
        print(doc)
        for i in doc:
            docc.append(indeks(PP, i))
    return docc

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( drivers, all_tests = True )
