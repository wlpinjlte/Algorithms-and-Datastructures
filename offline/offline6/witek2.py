from zad6testy import runtests
import collections

class W:
    def __init__(self):
        self.d = -1
        self.visited = 0
        self.parent = None
def bfs(G,s,t):
    n = len(G)
    q = collections.deque()
    w = [-1 for i in range(n)]
    w[s] = 0
    #w[s].visited = 1
    q.append(s)
    while q:
        u = q.popleft()
        if u == t: break
        for v in G[u]:
            if w[v] == -1:
                #w[v].visited = 1
                w[v] = w[u] + 1
                q.append(v)
    return w[t]

def longer( G, s, t ):
    n = len(G)
    q = collections.deque()
    w = [W() for i in range(n)]
    w[s].d = 0
    w[s].visited = 1
    q.append(s)
    while q:
        u = q.popleft()
        if u == t: break
        for v in G[u]:
            if w[v].visited == 0:
                w[v].visited = 1
                w[v].d = w[u].d + 1
                w[v].parent = u
                q.append(v)
            elif w[u].d + 1 == w[v].d:
                w[v].visited += 1
    if w[t].visited == 0: return None
    x = t
    p = 1
    while x != s:
        if w[x].visited == 1 and p == 1:
            T = G.copy()
            T[x].remove(w[x].parent)
            T[w[x].parent].remove(x)
            d = bfs(T, s, t)
            if d > w[t].d or d == -1 : return w[x].parent, x
        p = w[x].visited
        x = w[x].parent
    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )