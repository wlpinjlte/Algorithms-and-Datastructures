from zad3testy import runtests
def dfs(graf):
    visited=[0for i in range(len(graf))]
    pkt=[]
    def dfs_vis(s):
        nonlocal pkt,visited,graf
        for i in graf[s]:
            if visited[i]==0:
                visited[i]=1
                dfs_vis(i)
        pkt.append(s)
    for i in range(len(graf)):
        if visited[i]==0:
            visited[i]=1
            dfs_vis(i)
    return pkt
def tasks(T):
    graf=[[]for i in range(len(T))]
    for i in range(len(T)):
        for j in range(len(T)):
            if T[i][j]==1:
                graf[j].append(i)
            # elif T[i][j]==0:
            #     #graf[j].append(i)
            #     #graf[i].append(j)
    return dfs(graf)

runtests(tasks)