import queue
def relax(u,v,parent,d,w):
    if d[v]>d[u]+w:
        d[v]=d[u]+w
        parent[v]=u
        return 1
    return 0
def dikstra(G,S):
    qs=queue.PriorityQueue()
    d=[10**10 for i in range(len(G))]
    parent=[None for i in range(len(G))]
    d[S]=0
    qs.put(S)
    while not qs.empty():
        x=qs.get()
        for i in G[x]:
            if relax(x,i[0],parent,d,i[1])==1:
                qs.put(i[0],d[i])
    return d
