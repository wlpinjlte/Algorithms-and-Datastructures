import queue
from queue import PriorityQueue
from math import inf

def relax(a,b,w,d):
    if d[b]>d[a]+w:
        d[b]=d[a]+w
        return 1
    return 0
def dijkstra(G,s,w):
    #print(len(G))
    h=w
    visited=[0 for i in range(len(G)*2+2)]
    d=[10**10 for i in range(len(G)*2+2)]
    #print(d[w*2+1])
    qs=queue.PriorityQueue()
    qs.put(0,s)
    d[s]=0
    while not qs.empty():
        x=qs.get()
        visited[x]=1
        #print(x)
        for i in range(len(G)):
            if G[x//2][i]!=0 and visited[i*2]==0:
                if relax(x,i*2,G[x//2][i],d)==1:
                    qs.put(i*2,d[i*2])
        if x%2==0:
            for i in range(len(G)):
                if G[x // 2][i] != 0 and visited[i * 2] == 0:
                    for j in range(len(G)):
                        if G[i][j] != 0 and visited[j * 2+1] == 0:
                            w=max(G[i][j],G[x//2][i])
                            if relax(x, j * 2+1, w, d) == 1:
                                qs.put(j * 2+1,d[j * 2+1])
    #print(d)
    return min(d[h*2],d[h*2+1])

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