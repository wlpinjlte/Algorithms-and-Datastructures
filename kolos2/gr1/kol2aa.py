from kol2atesty import runtests
#f(i)-minimalna gdy dojeżdza marian f(i)=min(tab[i]+g(i-j))   j=1..3
#g(i)-minimalna gdy dojeżdza Jacek  g(i)=min(f(i-j))    j=1..3
def f(i,F,G,tab):
    if i<0:
        return 10**10
    if F[i]!=10**10:
        return F[i]
    z=tab[i]
    for j in range(1,4):
        F[i]=min(F[i],z+g(i-j,F,G,tab))
        z+=tab[i-j]
    return F[i]
def g(i,F,G,tab):
    if i<0:
        return 10**10
    if G[i]!=10**10:
        return G[i]
    for j in range(1,4):
        G[i]=min(G[i],f(i-j,F,G,tab))
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
    F = [10 ** 10 for i in range(len(tab))]
    G = [10 ** 10 for i in range(len(tab))]
    G[0] = 0
    G[1] = 0
    G[2] = 0
    print(g(len(tab)-1,F,G,tab))
    F1 = [10 ** 10 for i in range(len(tab))]
    G1 = [10 ** 10 for i in range(len(tab))]
    G1[0]=0
    G1[1]=0
    G1[2]=0
    print(f(len(tab)-1,F1,G1,tab))
    print(F,G)
    print(F1,G1)
    doc=[]
    j=len(tab)-1
    i=0
    if G[len(tab)-1]<=F1[len(tab)-1]:
        while i<j:
            if G[i]+tab[i+1]==F[i+1]:
                i = i + 1
                doc.append(indeks(PP,i))

            elif G[i]+tab[i+1]+tab[i+2]==F[i+2]:
                i = i + 2
                doc.append(indeks(PP, i))

            else:
                i = i + 3
                doc.append(indeks(PP, i))
            if i>=j:
                break
            if F[i]==G[i+1]:
                i = i + 1
                doc.append(indeks(PP,i))

            elif F[i]==G[i+2]:
                i = i + 2
                doc.append(indeks(PP, i))

            else:
                i = i + 3
                doc.append(indeks(PP, i))

    else:
        while G1[i]>0:
            minn=(10**10,i)
            for j in range(1,4):
                if minn[0]>G1[i-j]:
                    minn=(G1[i-j],i-j)
            doc.append(indeks(PP,minn[1]))
            i=minn[1]
            print(minn[1])
            minn = (10 ** 10, i)
            if G1[i]==0:
                doc.append(indeks(PP, i-1))
                break
            for j in range(1,4):
                if i-j<0:break
                if minn[0]>F1[i-j]:
                    minn=(F1[i-j],i-j)
            doc.append(indeks(PP,minn[1]))
            i=minn[1]
            if G1[i]==0:
                doc.append(indeks(PP, i-1))
                break
        #doc.append(indeks(PP, i))
    return doc

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( drivers, all_tests = True )
# while i < n:
#         if o == 0:
#             if F[o][i] == F[1][i+1]:
#                 i += 1
#                 if i < n: tab.append(Z[i])
#             elif F[o][i] == F[1][i+2]:
#                 i += 2
#                 if i < n: tab.append(Z[i])
#             else:
#                 i += 3
#                 if i < n: tab.append(Z[i])
#             o = 1
#         else:
#             if F[o][i] == C[i+1] - C[i] + F[0][i+1]:
#                 i += 1
#                 if i < n: tab.append(Z[i])
#             elif F[o][i] == C[i+2] - C[i] + F[0][i+2]:
#                 i += 2
#                 if i < n: tab.append(Z[i])
#             else:
#                 i += 3
#                 if i < n: tab.append(Z[i])
#             o = 0