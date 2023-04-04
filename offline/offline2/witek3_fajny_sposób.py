from zad2testy import runtests

def partition(T, p, r, k):
    x = T[r]
    i = p - 1
    l = (k+1)%2
    for j in range(p,r):
        if T[j][k] < x[k] or T[j][k] == x[k] and T[j][l] > x[l]:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i+1], T[r] = T[r], T[i+1]
    return i+1

def quick_sort(T, p, r, k):
    if p < r:
        q = partition(T, p, r, k)
        quick_sort(T, p, q-1, k)
        quick_sort(T, q+1, r, k)
        #p = q + 1

def depth(L):
    n = len(L)
    quick_sort(L, 0, n-1, 1)
    for i in range(n):
        L[i].append(i)
    quick_sort(L, 0, n-1, 0)
    maks = 0
    for i in range(n):
        k = n - (i + n - L[i][2])
        if maks < k:
            maks = k
    return maks


runtests( depth )