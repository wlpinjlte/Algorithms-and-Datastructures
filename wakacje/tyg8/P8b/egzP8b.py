from egzP8btesty import runtests

def b_graf(G):
    graf=[[-1for j in range(len(G))]for i in range(len(G))]
    for i in range(len(G)):
        graf[i][i]=0
        for j in G[i]:
            graf[i][j[0]]=j[1]
    return graf
def fload_warchal(graf):
    od=[[10**10for j in range(len(graf))]for i in range(len(graf))]
    for i in range(len(graf)):
        for j in range(len(graf)):
            if graf[i][j]!=-1:
                od[i][j]=graf[i][j]
    for k in range(len(graf)):
        for i in range(len(graf)):
            for j in range(len(graf)):
                if od[i][j]>od[i][k]+od[k][j]:
                    od[i][j]=od[i][k]+od[k][j]
    return od
def robot( G, P ):
    graf=b_graf(G)
    od=fload_warchal(graf)
    # print(graf)
    # print(od)
    odd=0
    for i in range(len(P)-1):
        odd+=od[P[i]][P[i+1]]
    return odd
    
runtests(robot, all_tests = True)
