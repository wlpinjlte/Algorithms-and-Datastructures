from zad1testy import runtests

def dfs(G,s,k):
    visited=[0 for i in range(makss(G)+1)]
    def dfss(s,G):
        nonlocal k
        i=0
        #print(s)
        while i<len(G) and G[i][0]<s:
            i+=1
            #print(i)
        while i<len(G) and G[i][0]==s:
            if G[i][1]==k:
                visited[k]=2
                return 2
            if visited[G[i][1]]==0:
                visited[G[i][1]]=1
                visited[G[i][1]]=dfss(G[i][1],G)
            visited[s]=max(visited[s],visited[G[i][1]])
            i+=1
        return visited[s]
    visited[s]=2
    visited[s]=dfss(s,G)
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
    I=sorted(I,key=lambda x:x[0])
    visited=dfs(I,x,y)
    #print(visited)
    doc=[]
    for i in range(len(G)):
        if visited[G[i][0]]==2 and visited[G[i][1]]==2:
            doc.append(i)
    #print(visited)
    #doc=[]

    return doc


runtests(intuse)
