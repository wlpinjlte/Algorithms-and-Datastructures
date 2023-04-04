from zad1testy import runtests
import queue
def floyd_war(M):
    dys=[[10**10 for j in range(len(M[0]))]for i in range(len(M))]
    for i in range(len(M)):
        for j in range(len(M[0])):
            if i==j:
                dys[i][j]=0
            if M[i][j]!=0:
                dys[i][j]=M[i][j]
    for k in range(len(M)):
        for j in range(len(M)):
            for i in range(len(M)):
                if dys[i][k]+dys[k][j]<dys[i][j]:
                    dys[i][j]=dys[i][k]+dys[k][j]
    return dys

def keep_distance(M, x, y, d):
    # M=[
    #     [0,1,1,0],
    #     [1,0,0,1],
    #     [1,0,0,1],
    #     [0,1,1,0]
    # ]
    # dd=2
    # x=0
    # y=3
    dd=d
    dys=floyd_war(M)
    parent=[[None for j in range(len(M))]for i in range(len(M))]
    visited=[[0for j in range(len(M))]for i in range(len(M))]
    d=[[10**10for j in range(len(M))]for i in range(len(M))]
    print(dys)
    qs=queue.Queue()
    qs.put((x,y))
    d[x][y]=0

    while not qs.empty():
        z=qs.get()
        for i in range(len(M)):
            for j in range(len(M)):
                if (M[z[0]][i]!=0 or z[0]==i) and (M[z[1]][j]!=0 or z[1]==j) and dys[i][j]>=dd and visited[i][j]==0 and z!=(j,i):
                    qs.put((i,j))
                    #d[i][j]=d[z[0]][z[1]]+1
                    visited[i][j]=1
                    parent[i][j]=(z[0],z[1])
    doc=[]
    #print(y,z)
    temp=(y,x)
    print(parent)
    while temp!=(x,y):
        #print(temp)
        doc.append(temp)
        temp=parent[temp[0]][temp[1]]
    doc.append((x,y))
    #doc=[(0,5),(1,4),(3,2),(5,0)]
    docc=[]
    for i in range(len(doc)-1,-1,-1):
        docc.append(doc[i])
    return docc


runtests( keep_distance )
