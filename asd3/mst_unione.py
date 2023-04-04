parent=[]
rank=[]

def find(x):
    global parent
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]


def union(x,y):
    global parent
    x=find(x)
    y=find(y)
    if x==y:
        return 0
    if rank[x]>rank[y]:
        parent[y]=x
    else:
        parent[x]=y
        if rank[x]==rank[y]:
            rank[y]+=1
    return 1

def kluska(G):
    global parent
    global rank
    G.sorted(key=lambda x:x[2])
    n=10
    parent=[i for i in range(n)]
    rank=[1for i in range(n)]
    doc=[]
    ile=0
    for i in G:
        if union(i[0],i[1])==1:
            ile+=1
            doc.append(i)
        if ile>=n-1:
            return doc
    return None