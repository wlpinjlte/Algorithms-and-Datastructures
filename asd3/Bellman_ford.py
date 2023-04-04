d=[]
p=[]
def relax(u,v,w):
    global d,p
    if d[v]>d[u]+w:
        d[v]=d[u]+w
        p[v]=u

def bellman_ford(G,s):
    global d,p
    d=[10*10 for i in range(len(G))]
    p=[None for i in range(len(G))]
    d[s]=0
    #wykonanie
    for i in range(len(G)):
        for j in G[i]:
            relax(i,j[0],j[1])
    #weryfikacje
    #flaga-true nie ma cyklu flaga-false jest cykl
    flag=True
    for i in range(len(G)):
        for j in G[i]:
            if d[i]>d[j[0]]+j[1]:
                flag=False
                break
    return flag,d