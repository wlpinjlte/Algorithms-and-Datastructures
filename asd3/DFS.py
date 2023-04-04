def DFS(G):
    time=0
    def dsf_f(S,visited,parent):
        nonlocal time
        nonlocal G
        time+=1
        visited[S]=1
        for i in G[S]:
            if visited[i]==0:
                dsf_f(i,visited,parent)
                parent[i]=S
        #time+=1

    parent=[None for i in range(len(G))]
    visited=[0 for i in range(len(G))]
    for i in range(len(G)):
        if visited[i]==0:
            dsf_f(i,visited,parent)

    