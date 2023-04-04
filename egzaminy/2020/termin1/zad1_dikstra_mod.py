from zad1testy import runtests
import queue


def islands(G, A, B):
    qs=queue.PriorityQueue()
    #d=[10**10 for i in range((len(G)+1)*3)]
    k=[1,5,8]
    ss=[0,0,0,0,0,1,0,0,2]
    qs.put((0,A,0))
    qs.put((0,A,1))
    qs.put((0,A,2))
    while not qs.empty():
        d,i,s=qs.get()
        if i==B:
            return d
        for j in range(len(G)):
            if G[i][j]!=0 and G[i][j]!=k[s]:
                qs.put((d+G[i][j],j,ss[G[i][j]]))
runtests(islands)
