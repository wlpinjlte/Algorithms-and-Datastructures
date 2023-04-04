from zad1testy import runtests
import queue
def b_graf(G):
    doc=[[]for i in range(3*len(G))]
    for i in range(len(G)):
        for j in range(len(G)):
            if i==j:
                continue
            if G[i][j]!=0:
                if G[i][j]==1:
                    doc[i*3+1].append(j*3)
                    doc[i*3+2].append(j*3)
                elif G[i][j]==5:
                    doc[i*3].append(j*3+1)
                    doc[i*3+2].append(j*3+1)
                elif G[i][j]==8:
                    doc[i*3].append(j*3+2)
                    doc[i*3+1].append(j*3+2)
    print(doc)
    return doc

def relax(a,b,d,w):
    #print(a,b,d[a],d[b],w)
    if d[b]>d[a]+w:
        d[b]=d[a]+w
        return 1
    return 0


def islands(G, A, B):
    graf=b_graf(G)
    qs = queue.PriorityQueue()
    maks = 10**10
    for j in range(3):
        d=[10**10 for i in range(len(graf))]
        d[A*3+j]=0
        qs.put(A*3+j,0)
        while not qs.empty():
            x=qs.get()
            for i in graf[x]:
                if i%3==0:
                    w=1
                elif i%3==1:
                    w=5
                else:
                    w=8
                if relax(x,i,d,w)==1:
                    qs.put(i,d[i])
                #print(i)
        #print(d)
        maks=min(maks,d[B*3],d[B*3+1],d[B*3+2])
    return maks

runtests(islands)
