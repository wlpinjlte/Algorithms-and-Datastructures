# Witold Strzeboński
# f(i) - minimalna liczba pkt kontrolnych mijanych przez Mariana od 0 do i, przesiadając się w i
# O(nlogn)
from kol2atesty import runtests

def f(i, F,L,n):
    if i >= n:
        return 0
    if F[i] != -1:
        return F[i]
    F[i] = min(f(i+2,F,L,n) + L[i+1]-L[i], f(i+3,F,L,n) + L[i+1]-L[i], f(i+4,F,L,n) + L[i+1]-L[i], f(i+5,F,L,n) + L[i+2]-L[i], f(i+6,F,L,n) + L[i+3]-L[i])
    return F[i]

def drivers( P, B ):
    #P.sort()
    n = len(P)
    Z = []
    K = []
    for i in range(n):
        if P[i][1]:
            Z.append((P[i][0], i))
        else:
            K.append(P[i][0])
    Z.sort()  # tutaj
    K.sort()  # tutaj
    L = [0 for i in range(len(Z)+3)]
    p = 0
    for i in range(len(Z)):
        s = 0
        while p < len(K) and K[p] < Z[i][0]:
            p += 1
            s += 1
        L[i] = s
    L[len(Z)] = max(0, len(K) - p)  # tutaj
    for i in range(1,len(L)):
        L[i] += L[i-1]
    n = len(Z)
    F = [-1 for i in range(n)]
    #print(min(f(0, F, L, n), f(1, F, L, n), f(2, F, L, n)))
    if min(f(0, F, L, n), f(1, F, L, n), f(2, F, L, n)) == f(0, F, L, n): i = 0
    elif min(f(0, F, L, n), f(1, F, L, n), f(2, F, L, n)) == f(1, F, L, n): i = 1
    else: i = 2
    tab = [i]
    tab = [Z[i][1]]  # tutaj aż do końca
    while i < n - 1:
        if min(f(i + 2, F, L, n) + L[i + 1] - L[i], f(i + 3, F, L, n) + L[i + 1] - L[i],
               f(i + 4, F, L, n) + L[i + 1] - L[i], f(i + 5, F, L, n) + L[i + 2] - L[i],
               f(i + 6, F, L, n) + L[i + 3] - L[i]) == f(i + 2, F, L, n) + L[i + 1] - L[i]:
            tab.append(Z[i + 1][1])
            i += 2
        elif min(f(i + 2, F, L, n) + L[i + 1] - L[i], f(i + 3, F, L, n) + L[i + 1] - L[i],
                 f(i + 4, F, L, n) + L[i + 1] - L[i], f(i + 5, F, L, n) + L[i + 2] - L[i],
                 f(i + 6, F, L, n) + L[i + 3] - L[i]) == f(i + 3, F, L, n) + L[i + 1] - L[i]:
            tab.append(Z[i + 1][1])
            i += 3
        elif min(f(i + 2, F, L, n) + L[i + 1] - L[i], f(i + 3, F, L, n) + L[i + 1] - L[i],
                 f(i + 4, F, L, n) + L[i + 1] - L[i], f(i + 5, F, L, n) + L[i + 2] - L[i],
                 f(i + 6, F, L, n) + L[i + 3] - L[i]) == f(i + 4, F, L, n) + L[i + 1] - L[i]:
            tab.append(Z[i + 1][1])
            i += 4
        elif min(f(i + 2, F, L, n) + L[i + 1] - L[i], f(i + 3, F, L, n) + L[i + 1] - L[i],
                 f(i + 4, F, L, n) + L[i + 1] - L[i], f(i + 5, F, L, n) + L[i + 2] - L[i],
                 f(i + 6, F, L, n) + L[i + 3] - L[i]) == f(i + 5, F, L, n) + L[i + 2] - L[i]:
            tab.append(Z[i + 2][1])
            i += 5
        else:
            tab.append(Z[i + 3][1])
            i += 6
        if i < n: tab.append(Z[i][1])
    return tab

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( drivers, all_tests = True )