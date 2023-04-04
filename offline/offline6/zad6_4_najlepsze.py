#Mateusz Waga
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
            GG[t].remove(par[t])
            if d!=BFS(GG,s,os):
                #print(str(par[t])+" "+str(t))
                b=(par[t],t)
                #print(b)
                return (par[t],t)
        wypi(par,par[t],vis,d,os,G,s)
    #print(str(t)+" "+str(vis[t])+"    ")

def BFS(G,S,w):
    Q = cs.deque()
    inf=10**10
    #print(G)
    m=len(G)
    visited=[0 for _ in range(m)]
    d=[inf for _ in range(m)]
    parent=[None for _ in range(m)]
    d[S]=0
    visited[S]=0
    Q.append(S)
    while Q:
        S=Q.popleft()
        for i in G[S]:
            if visited[i]==0:
                    Q.append(i)
                    visited[i]=1
                    parent[i]=S
                    d[i]=d[S]+1
    return d[w]

def longer( G, s, t ):
    global b
    b=None
    V=len(G)
    Q=cs.deque()
    visited=[0 for i in range(V)]
    parent=[None for i in range(V)]
    d=[10**10 for i in range(V)]
    visited[s]=1
    d[s]=0
    Q.append(s)
    while Q:
        x=Q.popleft()
        for i in G[x]:
            if visited[i]==0:
                d[i]=d[x]+1
                parent[i]=x
                visited[i]+=1
                Q.append(i)
            elif d[i]==d[x]+1:
                visited[i]+=1
                parent[i]=x
    #wypi_s(parent,t,visited)
    doc=wypi(parent,t,visited,d[t],t,G,s)
    if doc is None and b!=None:
        return b
    #print(parent)
    return doc

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )