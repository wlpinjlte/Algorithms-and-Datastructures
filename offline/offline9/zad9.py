#Mateusz Waga algorytm polega na sprawdzeniu wszystkich możliwych ujść algorytem Edondsa-Karpa(szukający scieżek powiekszających) i zapisuje najlepszy wynik O(V^3*E^2)
import collections
from zad9testy import runtests


def BFS(G, S, a, b, na):
    parent = [None for i in range(len(G))]
    visited = [-1 for i in range(len(G))]
    qs = collections.deque()
    p = None
    visited[S] = 0
    qs.append(S)
    while qs:
        x = qs.popleft()
        # print(x)
        if x == a or x == b:
            if x == a:
                p = a
            else:
                p = b
            break
        for i in range(len(G[x])):
            if na[x][G[x][i]] > 0 and visited[G[x][i]] == -1:
                visited[G[x][i]] = 0
                qs.append(G[x][i])
                parent[G[x][i]] = x
    return (p, parent)


def maks_w(G):
    n = 0
    for i in G:
        if n < i[0] or n < i[1]:
            if n < i[0]:
                n = i[0]
            else:
                n = i[1]
    return n


def graf(G, na, n,wej):
    # n=maks_w(G)
    doc = [[] for i in range(n)]
    for i in G:
        doc[i[0]].append(i[1])
        na[i[0]][i[1]] = i[2]
        wej[i[1]]+=i[2]
        doc[i[1]].append(i[0])
    return doc


def zam(na, parent, s):
    temp=s
    minn=10**10
    while parent[temp]!=None:
        minn=min(na[parent[temp]][temp],minn)
        temp=parent[temp]
    while parent[s] != None:
        na[parent[s]][s] -= minn
        na[s][parent[s]] += minn
        s = parent[s]
    return minn

def maxflow(G, s):
    n = maks_w(G) + 1
    na = [[0 for j in range(n)] for i in range(n)]
    wejscie = [0 for i in range(n)]
    doc = graf(G, na, n,wejscie)
    #nac = copy.deepcopy(na)
    nac=[na[i][:] for i in range(n)]
    #kopiowanie(nac,na)
    # print(na,nac)
    maks = 0
    for i in range(n):
        if i == s:
            i += 1
        for j in range(i + 1, n):
            if j == s or maks>=wejscie[i]+wejscie[j]:
                j += 1
            pom = BFS(doc, s, i, j, na)
            il = 0
            while pom[0] != None:
                il += zam(na, pom[1], pom[0])
                pom = BFS(doc, s, i, j, na)
            if maks < il:
                maks = il
            #kopiowanie(na,nac)
            na = [nac[i][:] for i in range(n)]
    return maks


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(maxflow, all_tests=True)