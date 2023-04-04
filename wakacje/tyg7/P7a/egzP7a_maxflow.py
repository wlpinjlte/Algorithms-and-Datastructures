from egzP7atesty import runtests
import queue
def b_graf(T):#zbudowanie grafu(pierwsze len(T) to studenci drugie len(T) to pokoje)
    graf=[[0for j in range(2*len(T)+2)]for i in range(2*len(T)+2)]
    for i in range(len(T)):
        for j in T[i]:
            if j==None:
                continue
            graf[i][j+len(T)]=1
    for i in range(len(T)):
        graf[2*len(T)][i]=1
        graf[i+len(T)][2*len(T)+1]=1
    return graf
def bfs(graf,s):#bfs szukający ścieżki powiększającej
    visited=[0for i in range(len(graf))]
    parent=[None for i in range(len(graf))]
    qs=queue.Queue()
    qs.put(s)
    visited[s]=1
    while not qs.empty():
        x=qs.get()
        if visited[len(graf)-1]==1:
            return parent
        for i in range(len(graf)):
            if graf[x][i]==1 and visited[i]==0:
                visited[i]=1
                parent[i]=x
                qs.put(i)
    return None
def zam(graf,parent,s):#zmiana wartość przepływów
    while parent[s]!=None:
        graf[parent[s]][s]-=1
        graf[s][parent[s]]+=1
        s=parent[s]
    return
def akademik( T ):
    graf=b_graf(T)
    parent = bfs(graf, len(graf)-2)
    while parent!=None:#max_flow
        zam(graf,parent,len(graf)-1)
        parent=bfs(graf,len(graf)-2)
    il=0
    for i in range(len(T)):#sprawdzenie ile studentów nie dostało to co chciało
        if graf[len(graf)-2][i]==1:
            if T[i]!=(None,None,None):
                il+=1
    return il
runtests ( akademik,all_tests = True )