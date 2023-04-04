def Floyd_Warshall(G):
    D=[[10*10for j in range(len(G))]for i in range(len(G))]
    #print(len(G))
    #print(G[6][6])
    for i in range(len(G)):
        for j in range(len(G)):
            #print(i,j)
            if i==j:
                D[i][j]=0
            if G[i][j]!=-1:
                D[i][j]=G[i][j]
    for k in range(len(G)):
        for i in range(len(G)):
            for j in range(len(G)):
                D[i][j]=min(D[i][k]+D[k][j],D[i][j])
    return D

G = [
     [-1,4,-1,-1,6,2,-1],
     [4,-1,2,-1,-1,-1,-1],
     [-1,2,-1,2,-1,-1,-1],
     [-1,-1,2,-1,3,1,-1],
     [6,-1,-1,3,-1,5,2],
     [2,-1,-1,1,5,-1,7],
     [-1,-1,-1,2,7,-1,-1]]

print(Floyd_Warshall(G))