from egzP3btesty import runtests 
from queue import PriorityQueue
def find(x,parent):
    if parent[x]!=x:
        parent[x]=find(parent[x],parent)
    return parent[x]
def union(x,y,rank,parent):
    x=find(x,parent)
    y=find(y,parent)
    #print(x,y)
    if x==y:
        return 0
    if rank[x]>rank[y]:
        parent[y]=x
    else:
        parent[x]=y
        if rank[x]==rank[y]:
            rank[y]+=1
    return 1
def kluska(GG,n):
    GG=sorted(GG,key=lambda x:x[2],reverse=True)
    #print(GG)
    iiii=0
    for i in GG:
        iiii+=i[2]
    parent=[i for i in range(n)]
    rank=[1 for i in range(n)]
    mst=[]
    i=0
    ekstra=0
    while i<len(GG):
        if union(GG[i][0],GG[i][1],rank,parent)==1:
            mst.append(GG[i])
        else:
            ekstra=max(ekstra,GG[i][2])
        i+=1
        if len(mst)==n-1:
            break
    if i<len(GG):
        ekstra = max(ekstra, GG[i][2])
    #rint(ekstra)
    for i in mst:
        #print(i[2])
        ekstra+=i[2]
    return iiii-ekstra

def zmiana_grafu(G):
    GG=[]
    for i in range(len(G)):
        for j in range(len(G[i])):
            if i<G[i][j][0]:
                GG.append((i,G[i][j][0],G[i][j][1]))
    return GG
def lufthansa ( G ):
    #print(G)
    GG=zmiana_grafu(G)
    #print(GG)
    return kluska(GG,len(G))

runtests ( lufthansa, all_tests=True )