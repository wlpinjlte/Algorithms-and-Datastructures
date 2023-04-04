import queue as qu
from zad6testy import runtests


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
    print(str(t)+" "+str(vis[t]))

def wypi(par,t,vis):
    if par[t]!=None:
        if vis[t]==1:
            print(str(t) + " " + str(vis[t]) + "    "+str(par[t]))
            return (par[t],t)
        wypi(par,par[t],vis)
    #print(str(t)+" "+str(vis[t])+"    ")

def longer( G, s, t ):
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
                parent[i]=x
    wypi_s(parent,t,visited)
    doc=wypi(parent,t,visited)
    #print(parent)
    return doc

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )