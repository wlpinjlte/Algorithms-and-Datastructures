def Euler(G):
    def dsf_f(S,doc):
        nonlocal G
        for i in G[S]:
            G[S].remove(i)
            G[i].remove(S)
            dsf_f(i, doc)
        doc.append(S)
    doc=[]
    dsf_f(0,doc)
    return doc
tab=[[1,2],[0,3,2,5],[0,1,3,5],[1,2,4,5],[3,5],[1,2,3,4]]
print(Euler(tab))
# def dfs(G):
#     n = len(G)
#     Visited = [[0 for j in range(n)] for i in range(n)]
#     T = []
#     dfs_visit(G, Visited, T, 0)
#     T.reverse()
#     return T
#
#
# def dfs_visit(G, Visited, T, u):
#     for v in G[u]:
#         if not Visited[u][v]:
#             Visited[u][v] = 1
#             Visited[v][u] = 1
#             dfs_visit(G, Visited, T, v)
#     T.append(u)