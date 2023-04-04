import queue as qu

import collections as cs
from zad6testy import runtests

b=None
def maks_w(G):
    v=0
    for i in G:
        for z in i:
            if v<z:
                v=z
    return v

def wypi_s(par,t,vis):
    if par[t]!=None:
        wypi_s(par,par[t],vis)
    #print(str(t)+" "+str(vis[t]))

def wypi(par,t,vis,d,os,G,s):
    global b

    if par[t]!=None:
        if vis[t]==1:
            GG=G.copy()
            GG[par[t]].remove(t)
            if d!=BFS(GG,s,os):
                #print(str(par[t])+" "+str(t))
                b=(par[t],t)
                #print(b)
                return (par[t],t)
        wypi(par,par[t],vis,d,os,G,s)
    #print(str(t)+" "+str(vis[t])+"    ")

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

def longer( G, s, t ):
    global b
    # G = [[1, 2], [0, 3],[0,3],[1, 2, 4, 5], [3, 6],[3,6], [4, 5]]
    # s = 0
    # t = 6
    b=None
    #E=len(G)
    V=maks_w(G)+1
    Q=qu.Queue()
    visited=[0 for i in range(V)]
    parent=[None for i in range(V)]
    d=[10**10 for i in range(V)]
    #parent[s].append(None)
    visited[s]=1
    d[s]=0
    Q.put(s)
    while not Q.empty():
        x=Q.get()
        for i in G[x]:
            if visited[i]==0:
                d[i]=d[x]+1
                parent[i]=x
                visited[i]+=1
                Q.put(i)
            elif d[i]==d[x]+1:
                visited[i]+=1
                #parent[i]=x
    #wypi_s(parent,t,visited)
    doc=wypi(parent,t,visited,d[t],t,G,s)
    if doc is None and b!=None:
        return b
    #print(parent)
    return doc

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )