from zad1testy import runtests
import queue

def islands(G, A, B):
    d=[[10**10 for i in range(3)]for j in range(len(G))]
    d[A][0]=0
    d[A][1]=0
    d[A][2]=0
    k=[1,5,8]
    ss=[0,0,0,0,0,1,0,0,2]
    qu=queue.PriorityQueue()
    qu.put((0,A,0))
    qu.put((0,A,1))
    qu.put((0,A,2))
    while not qu.empty():
        dd,x,s=qu.get()
        if x==B:
            return dd
        for i in range(len(G)):
            if G[x][i]!=0 and d[i][s]>dd+G[x][i] and G[x][i]!=k[s]:
                d[i][s] = dd + G[x][i]
                #print(dd+G[x][i])
                qu.put((dd+G[x][i],i,ss[G[x][i]]))
    return None

runtests(islands)
