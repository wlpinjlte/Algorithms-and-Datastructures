#Mateusz Waga Rozwiązanie polega na przejściu jednego bfs wyznaczyć ścieżke najkrótszą(dowolną) i zliczenie ilość możliwych dojść do danego wierzchłka w satysfakcjonyjącej liczbie ruchów(d[i] jeżeli jest już wypełnione) zauważam że nasi kandydaci na krawędzie mają visited równe jeden(da się dojść do nich na jeden sposób) każdego kandytata sprawdzam usuwając daną krawędzi i puszczając klasycznego bfs kandytat spełnia warunki jeżeli po usunieciu liczba ruchów z s do t się wydłużyła złożoność to O(E(E+V))
import collections as cs
from zad6testy import runtests

b=None

def wypi_s(par,t,vis):
    if par[t]!=None:
        wypi_s(par,par[t],vis)
    print(str(t)+" "+str(vis[t]))

def wypi(par,t,vis,d,os,G,s):
    global b
    if par[t]!=None:
        if vis[t]==1:
            G[par[t]].remove(t)
            G[t].remove(par[t])
            if d!=BFS(G,s,os):
                b=(par[t],t)
                return (par[t],t)
            G[par[t]].append(t)
            G[t].append(par[t])
        wypi(par,par[t],vis,d,os,G,s)

def BFS(G,S,w):
    Q = cs.deque()
    inf=10**10
    m=len(G)
    visited=[0 for _ in range(m)]
    d=[inf for _ in range(m)]
    d[S]=0
    visited[S]=0
    Q.append(S)
    while Q:
        S=Q.popleft()
        for i in G[S]:
            if visited[i]==0:
                    Q.append(i)
                    visited[i]=1
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
    doc=wypi(parent,t,visited,d[t],t,G,s)
    #wypi_s(parent,t,visited)
    if doc is None and b!=None:
        return b
    return doc

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )