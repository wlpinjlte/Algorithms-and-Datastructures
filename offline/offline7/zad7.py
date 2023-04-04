#Mateusz Waga algorytm polega na przejściu bfs(z powrotami)(zgodnie z warunkami zadania) i szukaniu cykli najpierw od bramy południowej(później od bramy północnej)(od miasta 0) rozczytujemy rozwiązanie w momencie gdy cykl będzie zawierał wszystkie wierzchołki grafu Złożoność O(V!)
from zad7testy import runtests

def odczyt(P, i):
    elo = []
    temp = i
    while temp != None:
        elo.append(temp)
        temp = P[temp]
    return elo


def DFS(G):
    def DFSvisit1(G, S, P,visited,par,il):
        visited[S] = 1
        parent = par.copy()
        vis = visited.copy()
        pom=None
        if par[S] in G[S][1]:
            for u in G[S][0]:
                if visited[u] == 0 and pom==None:
                    par[u] = S
                    #il+=1
                    pom = DFSvisit1(G, u, P,visited,par,il+1)
                    visited=vis.copy()
                    par=parent.copy()
                if u == P and il==len(G):
                    #print(1)
                    return odczyt(parent, S)
                if pom != None:
                    return pom
        else:
            for u in G[S][1]:
                if visited[u] == 0 and pom==None:
                    par[u] = S
                    #il+=1
                    pom = DFSvisit1(G, u, P,visited,par,il+1)
                    visited = vis.copy()
                    par = parent.copy()
                if u == P and il==len(G):
                    #print(1)
                    return odczyt(parent, S)
                if pom != None:
                    return pom
        return None
    def DFSvisit2(G, S, P,visited,par,il):
        visited[S] = 1
        parent = par.copy()
        vis = visited.copy()
        pom=None
        if par[S] in G[S][0]:
            for u in G[S][1]:
                if visited[u] == 0 and pom==None:
                    par[u] = S
                    #il+=1
                    pom = DFSvisit2(G, u, P,visited,par,il+1)
                    visited = vis.copy()
                    par = parent.copy()
                if u == P and il==len(G):
                    #print(1)
                    return odczyt(parent, S)
                if pom != None:
                    return pom
        else:
            for u in G[S][0]:
                if visited[u] == 0 and pom==None:
                    par[u] = S
                    #il+=1
                    pom = DFSvisit2(G, u, P,visited,par,il+1)
                    visited=vis.copy()
                    par=parent.copy()
                if u == P and il==len(G):
                    #print(1)
                    return odczyt(parent, S)
                if pom != None:
                    return pom
        return None
    V = len(G)

    visited = [0 for _ in range(V)]
    par = [None for _ in range(V)]
    visited[0] = 1
    #od południa
    elo = DFSvisit2(G, 0, 0,visited,par,1)
    if elo != None:
        return elo[::-1]
    #od północy
    visited = [0 for _ in range(V)]
    par = [None for _ in range(V)]
    visited[0] = 1
    elo=DFSvisit1(G, 0, 0,visited,par,1)
    if elo != None:
        return elo[::-1]
    return None


def droga(G):
    # global doc
    #doc = None
    return DFS(G)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(droga, all_tests=True)
