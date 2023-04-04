import queue as qu
from zad6testy import runtests

def BFS(G,S,w):
    Q=qu.Queue()
    inf=10**10
    #print(G)
    m=maks_w(G)+1
    visited=[0 for _ in range(m)]
    d=[inf for _ in range(m)]
    parent=[None for _ in range(m)]
    d[S]=0
    visited[S]=0
    Q.put(S)
    while not Q.empty():
        S=Q.get()
        for i in G[S]:
            if visited[i]==0:
                    Q.put(i)
                    visited[i]=1
                    parent[i]=S
                    d[i]=d[S]+1
    return d[w]

def maks_w(G):
    v=0
    for i in G:
        for z in i:
            if v<z:
                v=z
    return v

def findd(a,b,G):
    #print(a,b)
    for i in G[a[0]]:
        for bb in b:
            if bb==i:
                return (a[0],bb)
    return None

def longer( G, s, t ):
    E=len(G)
    V=maks_w(G)+1
    Q=qu.Queue()
    visited=[0 for i in range(V)]
    parent=[[] for i in range(E)]
    d=[10**10 for i in range(V)]
    visited[s]=1
    d[s]=0
    parent[d[s]].append(None)
    Q.put(s)
    while not Q.empty():
        x=Q.get()
        for i in G[x]:
            if visited[i]==0:
                d[i]=d[x]+1
                if x not in parent[d[i]]:
                    parent[d[i]].append(x)
                visited[i]+=1
                Q.put(i)
            elif d[i]==d[x]+1:
                visited[i]+=1
                if x not in parent[d[i]]:
                    #print(parent[d[i]],x)
                    parent[d[i]].append(x)
    parent[d[t]+1].append(t)
    #print(parent)
    i=0
    while len(parent[i])!=0:
        if len(parent[i])==1 and parent[i][0]!=None:
            pom=findd(parent[i],parent[i+1],G)
            if pom!=None:
                if pom[0]==0:
                    GG = G.copy()
                    GG[0].remove(pom[1])
                    if d[t] == BFS(GG, s,t):
                        pass
                    else:
                        return pom
                else:
                    return pom
        i+=1
    print(parent)
    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )