from zad1testy import runtests
import queue


def jak_dojade(G, P, n, a, b):
    dd=[[10**10 for j in range(n+1)]for i in range(len(G))]
    visited=[[0 for j in range(n+1)]for i in range(len(G))]
    parent=[[None for j in range(n+1)]for i in range(len(G))]
    dd[a][n]=0
    qs=queue.PriorityQueue()
    qs.put((0,a,n))
    prev=None
    x=None
    while not qs.empty():
        d,i,p=qs.get()
        #print(i,p)
        visited[i][p]=1
        if i in P:
            prev=p
            p=n
        if i==b:
            x=p
            break
        for j in range(len(G)):
            #print(d[0])
            if G[i][j]!=-1 and p-G[i][j]>=0 and visited[j][p-G[i][j]]==0:
                if prev!=None:
                    parent[j][p-G[i][j]]=(i,prev)
                else:
                    parent[j][p - G[i][j]] = (i, p)
                qs.put((d+G[i][j],j,p-G[i][j]))
        prev=None
    #print(parent)
    if x==None:
        return None
    temp=(b,x)
    doc=[]
    while temp!=(a,n):
        doc.append(temp[0])
        temp=parent[temp[0]][temp[1]]
    doc.append(a)
    docc=[]
    for i in range(len(doc)-1,-1,-1):
        docc.append(doc[i])
    return docc


runtests(jak_dojade)
