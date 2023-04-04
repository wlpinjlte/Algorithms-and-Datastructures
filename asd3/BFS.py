import queue
def BFS(G,S):
    parent=[None for i in range(len(G))]
    od=[-1 for i in range(len(G))]
    visited=[-1 for i in range(len(G))]
    od[S]=0
    visited[S]=1
    qs=queue.PriorityQueue()
    qs.put(S)
    while not qs.empty():
        x=qs.get()
        for i in G[x]:
            if visited[i]!=1:
                od[i]=od[x]+1
                parent[i]=x
                visited[i]=1
                qs.put(i)
