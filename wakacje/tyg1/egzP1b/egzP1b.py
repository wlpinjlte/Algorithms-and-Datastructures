from egzP1btesty import runtests 
import queue
def makss(G):
    maks=0
    for i in G:
        maks=max(i[0],i[1],maks)
    return maks
def build_graf(G):
    graf=[[]for i in range(makss(G)+1)]
    for i in G:
        graf[i[0]].append((i[1],i[2]))
        graf[i[1]].append((i[0],i[2]))
    return graf
def turysta( G, D, L ):
    graf=build_graf(G)
    visited=[10**10for i in range(makss(G)*4+4)]
    qs=queue.PriorityQueue()
    qs.put((0,D,0))
    visited[0]=1
    visited[1]=1
    visited[2]=1
    visited[3]=1
    while not qs.empty():
        d,i,p=qs.get()
        #print(d,i,p)
        if p==4 and i==L:
            return d
        if p==4:
            continue
        for j in graf[i]:
            if d+j[1]<visited[j[0] * 4 + p]:
                visited[j[0] * 4 + p]=d+j[1]
                qs.put((d+j[1],j[0],p+1))
    return 0

runtests ( turysta )