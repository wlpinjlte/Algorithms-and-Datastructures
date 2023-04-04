from zad3testy import runtests

def partition(T, p, r):
    x = T[r]
    i = p-1
    for j in range(p, r):
        if T[j] <= x:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i+1], T[r] = T[r], T[i+1]
    return i+1

def quick_sort(T, p, r):
    if p<r:
        q = partition(T, p, r)
        quick_sort(T, p, q-1)
        quick_sort(T, q, r)

def bucket_sort(T):
    n = len(T)
    A = [[] for _ in range(n)]
    for x in T:
        A[int(x)-1].append(x)
    i = 0
    # for tab in A:
    #     quick_sort(tab, 0, len(tab)-1)
    #     for j in range(len(tab)):
    #         T[i] = tab[j]
    #         i += 1

    for tab in A:
        for k in range(len(tab)):
            minn = n+1
            j_min = -1
            for j in range(k, len(tab)):
                if tab[j] < minn:
                    minn = tab[j]
                    j_min = j
            tab[k], tab[j_min] = tab[j_min], tab[k]
            T[i] = minn
            i += 1

    # j = 0
    # while i < n:
    #     for k in range(len(A[j])):
    #         T[i] = A[j][k]
    #         i += 1
    #     j += 1


def SortTab(T,P):
    bucket_sort(T)
    #quick_sort(T, 0, len(T)-1)
    return T

runtests( SortTab )