from zad6testy import runtests
import queue
def bfs(G,s):
    n=len(G)
    visited=[0 for i in range(n)]
    d=[10**10 for i in range(n)]
    parent=[[] for j in range(n)]
    d[s]=0
    visited[s]=1
    qs=queue.PriorityQueue()
    qs.put((d[s],s))
    while not qs.empty():
        dd,w=qs.get()
        for i in G[w]:
            if visited[i]==0:
                visited[i]=1
                d[i]=dd+1
                parent[i].append(w)
                qs.put((d[i],i))
            elif d[i]==dd+1:
                parent[i].append(w)
                visited[i]+=1
    return d,parent
def ss(t,d,parent,tab):
    if parent[t]==[]:
        return
    for i in parent[t]:
        if (i,t) not in tab[d]:
            tab[d].append((i,t))
            ss(i,d-1,parent,tab)
def longer( G, s, t ):
    print(s,t)
    d,parent=bfs(G,s)
    #dt=bfs(G,t)
    tab=[[]for i in range(d[t]+1)]
    ss(t,d[t],parent,tab)
    print(tab)
    for i in range(len(tab)):
        if len(tab[i])==1:
            return tab[i][0]
    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )