#Mateusz Waga algorytm polega na sprawdzeniu wszystkich możliwych drzew rozpinających (start z najmniejszej karwedzi pod wzgledem odległość) po przetworzeniu drzewa usuwamy pierwszą krawedz i robimy kolejne drzewo algoytm koniczy prace jeżeli znalezienie drzewa rozpinającego nie jest możliwe z danymi krawędziami. Złożoność O(e^2logv)
from zad8testy import runtests
from math import ceil,sqrt
#tablicowe podejscie
parent=[]
rank=[]
# def find(x):
#     global parent
#     if parent[x]!=x:
#         parent[x]=find(parent[x])
#     return parent[x]
#
#
# def union(x,y):
#     global parent
#     x=find(x)
#     y=find(y)
#     if x==y:
#         return 0
#     if rank[x]>rank[y]:
#         parent[y]=x
#     else:
#         parent[x]=y
#         if rank[x]==rank[y]:
#             rank[y]+=1
#     return 1
#
# def kluska(G,n):
#     global parent
#     global rank
#     #G.sorted(key=lambda x:x[2])
#     #n=10
#     parent=[i for i in range(n)]
#     rank=[1for i in range(n)]
#     doc=[]
#     ile=0
#     for i in G:
#         if union(i[0],i[1])==1:
#             ile+=1
#             doc.append(i)
#         if ile>=n-1:
#             return doc
#     return None
#klasowe podejscie
class node():
    def __init__(self):
        self.parent=self
        self.rank=0

def find(x):
    if x.parent!=x:
        x.parent=find(x.parent)
    return x.parent

def union(x,y):
    x=find(x)
    y=find(y)
    if x==y:
        return None
    if x.rank>y.rank:
        y.parent=x
    else:
        x.parent=y
        if x.rank==y.rank:
            y.rank+=1

def MST(tab,n):
    doc=[]
    i=0
    k=0

    nodes=[node()for j in range(n)]

    while k<n-1 and i<len(tab):
        if find(nodes[tab[i][0]])!=find(nodes[tab[i][1]]):
            union(nodes[tab[i][0]],nodes[tab[i][1]])
            doc.append(tab[i])
            k+=1
        i+=1
    if len(doc)<n-1:
        return None
    return doc

def d(a,b):
    return ceil(sqrt((a[0]-b[0])**2+(a[1]-b[1])**2))

def highway( A ):
    tab=[]
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            tab.append([i,j,d(A[i],A[j])])
    tab.sort(key=lambda tab:tab[2])
    min=10**10
    while len(tab)>len(A)-1:
        pom=MST(tab,len(A))
        if pom==None:
            break
        if min>pom[len(pom)-1][2]-pom[0][2]:
            #print(pom)
            min=pom[len(pom)-1][2]-pom[0][2]
        tab.remove(tab[0])
        #tab.pop(0)
    #print(tab)
    return min

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( highway, all_tests = True )