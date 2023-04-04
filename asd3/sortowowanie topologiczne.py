def Sorttop(G):
    time=0
    def dsf_f(S,visited,parent,doc):
        nonlocal time
        nonlocal G
        time+=1
        visited[S]=1
        for i in G[S]:
            if visited[i]==0:
                dsf_f(i,visited,parent,doc)
                parent[i]=S
        doc.append(S)
        time+=1
    doc=[]
    parent=[None for i in range(len(G))]
    visited=[0 for i in range(len(G))]
    dsf_f(0,visited,parent,doc)#start z wierzchołka zero
    return doc

tab=[[1,2,6],[2,3],[4],[4,5,6],[2],[],[]]
print(Sorttop(tab))
