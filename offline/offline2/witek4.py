from zad2testy import runtests

def partition(T, p, r):
    x = T[r]
    i = p - 1
    for j in range(p,r):
        if T[j][0] < x[0]:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i+1], T[r] = T[r], T[i+1]
    return i+1

def quick_sort(T, p, r):
    if p < r:
        q = partition(T, p, r)
        quick_sort(T, p, q-1)
        quick_sort(T, q+1, r)

def bubble(T, n):
    for i in range(n-1, 0, -1):
        if T[i][0] == T[i-1][0] and T[i][1] > T[i-1][1]:
            T[i], T[i-1] = T[i-1], T[i]

def depth(L):
    n = len(L)
    quick_sort(L, 0, n-1)
    bubble(L, n)
    a = 0
    maks = 0
    flag = True
    while flag:
        if maks >= n-a:
            break
        flag = False
        x = a
        k = 0
        for i in range(x+1, n):
            if L[i][1] <= L[x][1]:
                k += 1
            elif not flag:
                a = i
                flag = True
            elif L[i][0] > L[x][1]:
                break

        if maks < k:
            maks = k

    return maks

runtests( depth )