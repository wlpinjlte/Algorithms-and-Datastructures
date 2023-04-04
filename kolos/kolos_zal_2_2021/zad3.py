from zad3testy import runtests
import queue
def relax(a,b,w,d):
    if d[a]>d[b]+w:
        d[a]=d[b]+w
        return 1
    return 0
def spraw(tab,j):
    for i in tab:
        if i[0]==j:
            return i[1]
    return 10**9
def paths(G, s, t):
    qs=queue.PriorityQueue()
    d1=[10**10 for i in range(len(G))]
    d2=[10**10 for j in range(len(G))]
    d1[s]=0
    qs.put(s,0)
    while not qs.empty():
        x=qs.get()
        for i in G[x]:
            if relax(i[0],x,i[1],d1)==1:
                qs.put(i[0],d1[i[0]])
    qs.put(t,0)
    d2[t]=0
    while not qs.empty():
        x=qs.get()
        for i in G[x]:
            if relax(i[0],x,i[1],d2)==1:
                qs.put(i[0],d2[i[0]])
    print(d1,d2)
    ile=0
    # for i in range(len(G)):
    #     for j in range(len(G)):
    #         if d1[i]+d2[j]+spraw(G[i],j)==d1[t]:
    #             ile+=1
    for i in range(len(G)):
        for j in G[i]:
            if d1[i]+j[1]+d2[j[0]]==d1[t]:
                ile+=1
    return ile


runtests(paths)
