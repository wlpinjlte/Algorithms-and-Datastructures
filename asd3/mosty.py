def Mosty(G):
    time=0
    low = [0 for i in range(len(G))]
    def dsf_f(S,visited,parent,d):
        nonlocal time
        nonlocal G
        nonlocal low
        time+=1
        visited[S]=1
        d[S]=time
        low[S]=time
        for i in G[S]:
            if visited[i]==0:
                parent[i] = S
                dsf_f(i,visited,parent,d)
                low[S]=min(low[S],low[i])#dzieci
            elif i!=parent[S]:#krawedz wsteczna
                low[S]=min(low[S],d[i])
        #time+=1

    parent=[None for i in range(len(G))]
    visited=[0 for i in range(len(G))]
    d=[10**10 for i in range(len(G))]
    #DFS
    for i in range(len(G)):
        if visited[i]==0:
            dsf_f(i,visited,parent,d)
    mosty=[]
    #odczyt mostów
    print(d)
    print(low)
    for i in range(1,len(G)):
        if low[i]==d[i]:
            mosty.append((parent[i],i))

    #punkty artykulacji(w taki sposób)
    # for i in range(len(graf)):
    #     if parent[i]==None:
    #         continue
    #     if low[i]>=d[parent[i]]:
    #         tab.append(parent[i])
    # return tab
    return mosty
# G=[[0, 1, 1, 0, 0, 0, 0, 0, 0],
#       [1, 0, 1, 0, 0, 0, 0, 0, 0],
#       [1, 1, 0, 1, 1, 1, 1, 0, 0],
#       [0, 0, 1, 0, 1, 0, 0, 0, 0],
#       [0, 0, 1, 1, 0, 0, 0, 0, 0],
#       [0, 0, 1, 0, 0, 0, 1, 0, 0],
#       [0, 0, 1, 0, 0, 1, 0, 1, 1],
#       [0, 0, 0, 0, 0, 0, 1, 0, 1],
#       [0, 0, 0, 0, 0, 0, 1, 1, 0]]
# graf=[[]for i in range(len(G))]
# for i in range(len(G)):
#     for j in range(len(G)):
#         if G[i][j]!=0:
#             graf[i].append(j)

tab=[[1,2],[0,3],[0,3,4],[2,5,1],[2],[3,6,7],[5,7],[5,6]]
print(Mosty(tab))


