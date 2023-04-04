from zad1testy import runtests
import queue
def bfs(graf,s):
    visited=[0 for i in range(len(graf))]
    d=[10**10 for i in range(len(graf))]
    parent=[None for i in range(len(graf))]
    qs=queue.Queue()
    d[s]=0
    qs.put(s)
    visited[s] = 1
    while not qs.empty():
        x=qs.get()
        for i in graf[x]:
            if visited[i]==0:
                visited[i]=1
                parent[i]=x
                d[i]=d[x]+1
                qs.put(i)
    maks=(0,-1)
    for i in range(len(graf)):
        if maks[0]<d[i]:
            maks=(d[i],i)
    return (maks[1],parent)
def best_root( L ):
    i=bfs(L,0)[0]
    print(i)
    i,parent=bfs(L,i)
    print(i,parent)
    sciezka=[]
    while i!=None:
        sciezka.append(i)
        i=parent[i]
    return sciezka[len(sciezka)//2]


runtests( best_root )
