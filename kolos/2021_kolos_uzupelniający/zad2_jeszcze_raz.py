import queue
from queue import PriorityQueue
from math import inf
def relax(d,dd,waga,w,p):
    # print(d)
    # print(d[s][p2])
    if d[w][p]>waga+dd:
        d[w][p]=waga+dd
        return 1
    return 0

def dijkstra(G,s,w):
    d=[[10**10for j in range(2)]for i in range(len(G))]
    d[s][0]=0
    d[s][1]=0
    qs=queue.PriorityQueue()
    qs.put((d[s][0],s,0))
    qs.put((d[s][1],s,1))
    while not qs.empty():
        dd,s,p=qs.get()
        if s==w:
            return dd
        for i in range(len(G)):
            if G[s][i]!=0 and relax(d,dd,G[s][i],i,p)==1:
                qs.put((d[i][p],i,p))
        if p==0:
            for i in range(len(G)):
                if G[s][i]!=0:
                    for j in range(len(G)):
                        if G[i][j]!=0 and relax(d,dd,max(G[s][i],G[i][j]),j,1)==1:
                            qs.put((d[j][1],j,1))
    print(d)
    return min(d[w][0],d[w][1])
G = [
    [0,1,0,0,0],
    [1,0,1,0,0],
    [0,1,0,7,0],
    [0,0,7,0,8],
    [0,0,0,8,0],
     ]
'''G=[[0, 1, 200, 200, 200, 200],
 [1, 0, 2, 200, 200, 200],
 [200, 2, 0, 40, 200, 200],
 [200, 200, 40, 0, 40, 200],
 [200, 200, 200, 40, 0, 117],
 [200, 200, 200, 200, 117, 0]]'''
print(dijkstra(G,0,4))
