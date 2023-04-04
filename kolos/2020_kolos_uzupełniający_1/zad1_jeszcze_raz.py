from zad1testy import runtests
import queue

def jak_dojade(G, P, n, a, b):
    qs=queue.PriorityQueue()
    d=[[10**10for j in range(n+1)]for i in range(len(G))]
    parent=[[None for j in range(n+1)]for i in range(len(G))]
    d[a][n]=0
    qs.put((0,a,n))
    while not qs.empty():
        dd,x,p=qs.get()
        #print(x)
        # if x in P:
        #     p=n
        if x==b:
            break
        for i in range(len(G)):
            if G[x][i]==-1:
                continue
            if p-G[x][i]>=0:
                if i in P:
                    if d[i][n]>dd+G[x][i]:
                        d[i][n]=dd+G[x][i]
                        parent[i][n]=(x,p)
                        qs.put((dd+G[x][i],i,n))
                else:
                    if d[i][p-G[x][i]]>dd+G[x][i]:
                        d[i][p - G[x][i]] = dd+G[x][i]
                        parent[i][p - G[x][i]] = (x, p)
                        qs.put((dd+G[x][i],i,p - G[x][i]))
    tmp=(x,p)
    doc=[]
    if x!=b:
        return None
    #doc.append(tmp[0])
    while tmp!=None:
        #print(tmp)
        doc.append(tmp[0])
        tmp=parent[tmp[0]][tmp[1]]
    #print(dd,parent)
    #print(doc)
    return doc[::-1]
runtests(jak_dojade)

