from zad3testy import runtests
import queue
def paths(G, s, t):
    d1=[10**10 for i in range(len(G))]
    d2=[10**10 for i in range(len(G))]
    d1[s]=0
    qs=queue.PriorityQueue()
    qs.put((d1[s],s))
    while not qs.empty():
        d,x=qs.get()
        for i in G[x]:
            if d1[i[0]]>d+i[1]:
                d1[i[0]] = d + i[1]
                qs.put((d1[i[0]],i[0]))
    d2[t]=0
    qs.put((0,t))
    while not qs.empty():
        d,x=qs.get()
        for i in G[x]:
            if d2[i[0]]>d+i[1]:
                d2[i[0]] = d + i[1]
                qs.put((d2[i[0]],i[0]))
    counter=0
    for i in range(len(G)):
        for j in G[i]:
            if i<j[0] and (d1[i]+d2[j[0]]+j[1]==d1[t] or d1[j[0]]+d2[i]+j[1]==d1[t]):
                counter+=1
    return counter


runtests(paths)