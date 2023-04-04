from zad1testy import runtests
import queue
def bfs(L,s):
    d=[10**10for i in range(len(L))]
    visited=[0 for i in range(len(L))]
    parent=[None for i in range(len(L))]
    d[s]=0
    visited[s]=1
    qs=queue.PriorityQueue()
    qs.put((d[s],s))
    while not qs.empty():
        dd,w=qs.get()
        for i in L[w]:
            if visited[i]==0:
                visited[i]=1
                parent[i]=w
                d[i]=dd+1
                qs.put((dd+1,i))
    return d,parent
def best_root( L ):
    d,parent=bfs(L,0)
    maks=(0,0)
    for i in range(len(d)):
        if maks[0]<d[i]:
            maks=(d[i],i)
    d,parent=bfs(L,maks[1])
    maks=(0,0)
    for i in range(len(d)):
        if maks[0]<d[i]:
            maks=(d[i],i)
    ind=d[maks[1]]//2
    i=0
    tmp=maks[1]
    while ind!=i:
        tmp=parent[tmp]
        i+=1
    return tmp
runtests(best_root)