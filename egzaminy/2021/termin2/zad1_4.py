from zad1testy import runtests

def binary_visited(vis,s):
    l=0
    p=len(vis)
    i=(l+p)//2
    while vis[i][0]!=s and p-l!=1:
        if vis[i][0]>s:
            p=i
        else:
            l=i
        i=(l+p)//2
    return i


def dfs(G,s,k):
    visited=[]
    z=[]
    for i in G:
        z.append(i[0])
        z.append(i[1])
    z=sorted(z)
    prev=-1
    for i in z:
        if i!=prev:
            visited.append([i,0])
        prev=i
    print(visited)
    def dfss(s,G):
        nonlocal k,visited
        l=0
        p=len(G)
        i=len(G)//2
        while i>0 and G[i][0]!=s and l!=p-1:
            if G[i][0]>s:
                p=i
            else:
                l=i
            i = (l + p) // 2
        while i>0 and G[i][0]==G[i-1][0]:
            i-=1
        #print(i)
        while i<len(G) and G[i][0]==s:
            #print(binary_visited(visited, s), s)
            if G[i][1]==k:
                visited[binary_visited(visited,k)][1]=2
                return 2
            if visited[binary_visited(visited,G[i][1])][1]==0:
                #print(G[i][1])
                visited[binary_visited(visited,G[i][1])][1]=1
                visited[binary_visited(visited,G[i][1])][1]=dfss(G[i][1],G)
            visited[binary_visited(visited,s)][1]=max(visited[binary_visited(visited,s)][1],visited[binary_visited(visited,G[i][1])][1])
            i+=1
        return visited[binary_visited(visited,s)][1]
    #print(binary_visited(visited,3))
    visited[binary_visited(visited,s)][1]=2
    visited[binary_visited(visited,s)][1]=dfss(s,G)
    return visited
def znajdz(G,x,y):
    for i in range(len(G)):
        if G[i][0]==x and G[i][1]==y:
            return i
def makss(I):
    maks=0
    for i in I:
        if i[1]>maks:
            maks=i[1]
    return maks
def intuse(I, x, y):
    G=I.copy()
    # for i in range(len(I)):
    #
    I=sorted(I,key=lambda x:x[1])
    #print(I)
    I=sorted(I,key=lambda x:x[0])
    #print(I)
    visited=dfs(I,x,y)
    print(visited)
    doc=[]
    for i in range(len(G)):
        if visited[binary_visited(visited,G[i][0])][1]==2 and visited[binary_visited(visited,G[i][1])][1]==2:
            doc.append(i)
    #print(visited)
    #doc=[]

    return doc


runtests(intuse)
