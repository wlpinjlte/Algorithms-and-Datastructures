from kol2atesty import runtests
#f(i)-min liczba punktów które musi przejechać gdy dojeżdza mairian do i-tego parkingu
#g(i)-min liczba punktów które musi przejechać gdy dojeżdza jacek do i-tego parkingu
F_od=[]
G_od=[]
def f(i,tab,F,G):
    global F_od
    if i<=0:
        return 10**10
    if F[i]!=10**10:
        return F[i]
    z=tab[i]
    #print(z)
    for j in range(1,4):
        if F[i]>g(i-j,tab,F,G)+z:
            F[i]=g(i-j,tab,F,G)+z
            F_od[i]=i-j
        z+=tab[i-j]
    return F[i]
def g(i,tab,F,G):
    global G_od
    # if i<0:
    #     return 10**10
    if G[i]!=10**10:
        return G[i]
    for j in range(1,4):
        if G[i]>f(i-j,tab,F,G):
            G[i]=f(i-j,tab,F,G)
            G_od[i]=i-j
    return G[i]
def odczyt(tab,P):
    z=0
    il=-1
    doc=[]
    for i in tab:
        while True:
            if P[z][1]==True:
                il+=1
            if i == il:
                doc.append(z)
                z += 1
                break
            z+=1
    return doc
def drivers( P, B ):
    PP=P.copy()
    P=sorted(P,key=lambda x:x[0])
    #print(P)
    P.append((B,True))
    il=0
    tab=[]
    for i in range(len(P)):
        if P[i][1]==False:
            il+=1
        else:
            tab.append(il)
            il=0
    #print(tab)
    #tab.append(0)
    global F_od,G_od
    F_od=[None for i in range(len(tab))]
    G_od=[None for i in range(len(tab))]
    F=[10**10for i in range(len(tab))]
    G=[10**10for j in range(len(tab))]
    G[0]=0
    G[1]=0
    G[2]=0
    GG=g(len(tab)-1,tab,F,G)
    #print(F)
    #print(G)
    kop1=F_od.copy()
    kop2=G_od.copy()
    # print(F_od)
    # print(G_od)
    F_od = [None for i in range(len(tab))]
    G_od = [None for i in range(len(tab))]
    F = [10 ** 10 for i in range(len(tab))]
    G = [10 ** 10 for j in range(len(tab))]
    G[0] = 0
    G[1] = 0
    G[2] = 0
    FF=f(len(tab)-1,tab,F,G)
    tmp = len(tab) - 1
    doc = []
    if GG<=FF:
        F_od=kop1
        G_od=kop2
        #print(GG)
        #print(F_od,G_od)
        while G_od[tmp]!=None:
            doc.append(G_od[tmp])
            tmp=G_od[tmp]
            if F_od[tmp]==None:
                break
            doc.append(F_od[tmp])
            tmp=F_od[tmp]
        #print(doc)
    else:
        #print(FF)
        #print(F_od, G_od)
        while F_od[tmp]!=None:
            doc.append(F_od[tmp])
            tmp=F_od[tmp]
            if G_od[tmp]==None:
                break
            doc.append(G_od[tmp])
            tmp=G_od[tmp]
    return odczyt(doc[::-1],PP)
runtests(drivers, all_tests=True)