import queue
def prime(G,S):
    qs=queue.PriorityQueue()
    w=[10**10 for i in range(len(G))]
    parent=[None for i in range(len(G))]
    w[S]=0
    for i in range(len(G)):
        qs.put(i)
    while not qs.empty():
        x=qs.get()
        for i in G[x]:
            if w[i[0]]>i[1]:
                w[i[0]]=i[1]
                parent[i[0]]=x
    return parent