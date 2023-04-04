def skladowe_graf(G):
    time=0
    def dsf_f(S,visited,d,stos):
        nonlocal time
        nonlocal G
        #nonlocal stos
        time+=1
        visited[S]=1
        d[S]=time
        stos.append(S)
        for i in G[S]:
            if visited[i]==0:
                dsf_f(i,visited,d,stos)
        #time+=1
    d=[0 for i in range(len(G))]
    visited=[0 for i in range(len(G))]
    stos=[]
    #pierwszy DFS
    for i in range(len(G)):
        if visited[i]==0:
            dsf_f(i,visited,d,stos)
    #odwrócenie krawędzi
    GG=[[]for i in range(len(G))]
    for i in range(len(G)):
        for j in G[i]:
            GG[j].append(i)
    G=GG
    #DFS_po czasach przetworzenia
    doc=[]
    visited=[0 for i in range(len(G))]
    while stos:
        x=stos.pop()
        if visited[x]==0:
            spojna_skl=[]
            dsf_f(x,visited,d,spojna_skl)
            print(spojna_skl)
            doc.append(spojna_skl)
    return doc
tab=[[1,2,6],[2,3],[4],[4,5,6],[],[6],[5]]
skladowe_graf(tab)