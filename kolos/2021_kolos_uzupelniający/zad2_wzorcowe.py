from queue import PriorityQueue
from math import inf

def dijkstra(G,s,w):

    n = len(G)
    d = [[inf]*2 for _ in range(n)]
    d[s][0] = 0
    d[s][1] = 0
    K=PriorityQueue()
    K.put((0, s, 0))
    visited = [[False]*2 for _ in range(n)]
    visited[s][1] = True
    while not K.empty():
        u=K.get()
        if u[1] == w:
            return u[0]
        if visited[u[1]][u[2]] is False:
            visited[u[1]][u[2]] = True
            print(".")
            print(u)
            # isć normalnie możemy zawsze
            for i in range(n):
                if G[u[1]][i] != 0 :
                    if d[i][0] > u[0] + G[u[1]][i]:
                        d[i][0] = u[0] + G[u[1]][i]
                        #p[i] = u[1]
                        K.put((d[i][0], i, 0))
                        #print(d[i][0], i, 0)

            # uzywac dwumilowych butów możemy tylko jak przyszliśmy do wierzchołka normalnie
            # w tym wypadku robiłam troche inaczej niz tlumaczyłam na zajęciach (wydaje mi się że łatwiej)
            # jeżeli jestem w danym weirzchołku i moge użyć dwumilowych butów to odrazu sprawdzam wszystkie
            # możliwości gdzie mogłabym dojść używając ich zaczynając od tego wierzchołka
            if u[2] == 0:
                for i in range(n):
                    if G[u[1]][i] != 0:
                        for j in range(n):
                            if G[i][j] != 0 :
                                x = max(G[u[1]][i],G[i][j])
                                if d[j][1] > u[0] + x:
                                    d[j][1] = u[0] + x
                                    K.put((d[j][1], j, 1))
                                    #print(d[j][1], j, 1)
    return False

'''G = [
    [0,1,0,0,0],
    [1,0,1,0,0],
    [0,1,0,7,0],
    [0,0,7,0,8],
    [0,0,0,8,0],
     ]'''
G=[[0, 1, 200, 200, 200, 200],
 [1, 0, 2, 200, 200, 200],
 [200, 2, 0, 40, 200, 200],
 [200, 200, 40, 0, 40, 200],
 [200, 200, 200, 40, 0, 117],
 [200, 200, 200, 200, 117, 0]]
print(dijkstra(G,0,4))