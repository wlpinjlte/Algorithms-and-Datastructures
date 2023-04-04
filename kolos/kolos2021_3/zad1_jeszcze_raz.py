from zad1testy import runtests
import queue
def fload_warhall(M):
    od=[[10**10for j in range(len(M))]for i in range(len(M))]
    for i in range(len(M)):
        for j in range(len(M)):
            if i==j:
                od[i][j]=0
                continue
            if M[i][j]!=0:
                od[i][j]=M[i][j]
    for i in range(len(M)):
        for j in range(len(M)):
            for z in range(len(M)):
                if od[i][j]>od[i][z]+od[z][j]:
                    od[i][j] = od[i][z] + od[z][j]
    return od
def keep_distance(M, x, y, d):
    od=fload_warhall(M)
    print(od)
    visited=[[0for j in range(len(M))]for i in range(len(M))]
    parent=[[None for j in range(len(M))]for i in range(len(M))]
    visited[x][y]=1
    qs=queue.Queue()
    qs.put((x,y))
    while not qs.empty():
        a,b=qs.get()
        if a==y and b==x:
            #print("siema")
            break
        for i in range(len(M)):
            if M[a][i]!=0 and od[i][b]>=d and visited[i][b]==0 and od[i][b]>=d and (i,b)!=(a,b):
                visited[i][b]=1
                parent[i][b]=(a,b)
                qs.put((i,b))
            for j in range(len(M)):
                # if a==i and b==j:
                #     continue
                if M[a][i]!=0 and M[b][j]!=0 and od[i][j]>=d and (a,b)!=(j,i) and visited[i][j]==0 and (i,j)!=(a,b):
                    visited[i][j]=1
                    parent[i][j]=(a,b)
                    qs.put((i,j))
                if M[b][j]!=0 and od[a][j]>=d and visited[a][j]==0 and od[a][j]>=d and (a,j)!=(a,b):
                    visited[a][j] = 1
                    parent[a][j]=(a,b)
                    qs.put((a, j))
    tmp=(y,x)
    doc=[]
    #print(parent)
    while tmp!=None:
        #print(tmp)
        doc.append(tmp)
        tmp=parent[tmp[0]][tmp[1]]
    #print(parent)
    return doc[::-1]
runtests(keep_distance)