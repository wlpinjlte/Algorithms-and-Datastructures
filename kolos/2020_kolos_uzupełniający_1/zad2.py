from zad2testy import runtests

def DFS(graf):
    visited=[0for i in range(len(graf))]
    low=[0 for i in range(len(graf))]
    parent=[None for i in range(len(graf))]
    d=[0 for i in range(len(graf))]
    time=0
    def dfs_visited(graf,s):
        nonlocal low,visited,time,parent,d
        visited[s]=1
        time += 1
        d[s]=time
        low[s]=time
        for i in graf[s]:
            if visited[i]==0:
                parent[i] = s
                dfs_visited(graf,i)
                low[s]=min(low[i],low[s])
            elif parent[s]!=i:
                low[s]=min(low[s],d[i])
    for i in range(len(graf)):
        if visited[i]==0:
            dfs_visited(graf,i)
    tab=[]
    print(low)
    print(d)
    for i in range(len(graf)):
        if parent[i]==None:
            continue
        if low[i]>=d[parent[i]]:
            tab.append(parent[i])
    return tab
def DFSS(G,s):
    time = 0
    def dsf_f(S, visited, parent):
        nonlocal time
        nonlocal G,s
        time += 1
        visited[S] = 1
        for i in range(len(G)):
            if i==s:
                continue
            if G[S][i]!=0 and visited[i] == 0:
                dsf_f(i, visited, parent)
                parent[i] = S
        time += 1

    parent = [None for i in range(len(G))]
    visited = [0 for i in range(len(G))]
    ile=0
    for i in range(len(G)):
        if i==s:
            continue
        if visited[i] == 0:
            ile+=1
            dsf_f(i, visited, parent)
    return ile

def breaking(G):
    #print(G)
    # G=[
    #     [0,1,0],
    #     [1,0,1],
    #     [0,1,0]
    # ]
    graf=[[]for i in range(len(G))]
    for i in range(len(G)):
        for j in range(len(G)):
            if G[i][j]!=0:
                graf[i].append(j)
    pkt=DFS(graf)
    maks=(-1,-1)
    if len(pkt)==0:
        return None
    for i in pkt:
        if maks[0]<DFSS(G,i):
            maks=(DFSS(G,i),i)
    print(pkt)
    if maks[0]==1:
        return None
    return maks[1]


runtests( breaking )
