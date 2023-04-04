from math import inf
def dijkstra(G,s):
    visited=[0 for i in range(len(G))]
    d=[10**10 for i in range(len(G))]
    d[s]=0
    min_ind=(s,0)
    while min_ind!=(None,10**10):
        temp_ind=min_ind[0]
        min_ind=(None,10**10)
        visited[temp_ind]=1
        for i in range(len(G)):
            if visited[i]==1:
                continue
            if G[temp_ind][i]!=-1:
                if d[i]>d[temp_ind]+G[temp_ind][i]:
                    d[i]=d[temp_ind]+G[temp_ind][i]
            if min_ind[1]>d[i]:
                min_ind=(i,d[i])
    return d

G = [
     [-1,4,-1,-1,6,2,-1],
     [4,-1,2,-1,-1,-1,-1],
     [-1,2,-1,2,-1,-1,-1],
     [-1,-1,2,-1,3,1,-1],
     [6,-1,-1,3,-1,5,2],
     [2,-1,-1,1,5,-1,7],
     [-1,-1,-1,2,7,-1]]
print(dijkstra(G,0))