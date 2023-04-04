from egzP5btesty import runtests
def maxx(B):
    maks=0
    for i in B:
        maks=max(i[0],i[1],maks)
    return maks
def zmien_graf(B):
    #print(maxx(B))
    graf=[[]for i in range(maxx(B)+1)]
    for i in B:
        if i[1] not in graf[i[0]]:
            graf[i[0]].append(i[1])
            graf[i[1]].append(i[0])
    return graf
def punkt_art(graf):
    d=[-1for i in range(len(graf))]
    visited=[0for i in range(len(graf))]
    low=[10**10 for i in range(len(graf))]
    parent=[None for i in range(len(graf))]
    time=0
    def dfs(s):
        nonlocal time,graf
        time+=1
        d[s]=time
        low[s]=time
        visited[s]=1
        for i in graf[s]:
            if visited[i]==0:
                parent[i]=s
                dfs(i)
                low[s]=min(low[s],low[i])
            elif parent[s]!=i:
                low[s]=min(low[s],d[i])
    dfs(0)
    #print(d)
    #print(low)
    #print(parent)
    punkty=[]
    for i in range(len(graf)):
        if parent[i]==None:
            continue
        if low[i]>=d[parent[i]]:
            if parent[i] not in punkty:
                punkty.append(parent[i])
    #print(punkty)
    return punkty
def dfss(graf):
    visited=[0for i in range(len(graf))]
    visited[0]=1
    visited[1]=1
    def dfs(s):
        nonlocal visited,graf
        visited[s]=1
        for i in graf[s]:
            if i==0:
                continue
            if visited[i]==0:
                dfs(i)
    dfs(1)
    for i in range(len(graf)):
        if visited[i]==0:
            return 0
    return 1
def koleje ( B ):
    graf=zmien_graf(B)
    print(graf)
    punkty=punkt_art(graf)
    if dfss(graf)==1:
        punkty.remove(0)
    return len(punkty)

runtests ( koleje, all_tests=True)