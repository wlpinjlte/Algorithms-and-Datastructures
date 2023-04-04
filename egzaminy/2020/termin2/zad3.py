from zad3testy import runtests
def topologiczne(graf):
    visited=[0 for i in range(len(graf))]
    doc=[]
    def dfs(s,graf):
        nonlocal doc,visited
        visited[s]=1
        for i in graf[s]:
            if visited[i]==0:
                dfs(i,graf)
        doc.append(s)
    for i in range(len(graf)):
        if visited[i]==0:
            dfs(i,graf)
    return doc
def tasks(T):
    # tu prosze wpisac implementacje
    graf=[[]for i in range(len(T))]
    for i in range(len(T)):
        for j in range(len(T)):
            if T[i][j]==1:
                graf[i].append(j)
    doc=topologiczne(graf)
    print(doc)
    docc=[]
    for i in range(len(doc)-1,-1,-1):
        docc.append(doc[i])
    return docc  # domyslny wynik [0,1,2,... ]


runtests(tasks)
