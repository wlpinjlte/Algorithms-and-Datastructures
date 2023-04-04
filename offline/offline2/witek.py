#Witek Strzeboński
from zad2testy import runtests

def partition(T, p, r):
    x = T[r]
    i = p - 1
    for j in range(p,r):
        if T[j][0] < x[0] or (T[j][0] == x[0] and T[j][1] > x[1]):
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i+1], T[r] = T[r], T[i+1]
    return i+1

def quick_sort(T, p, r):
    if p < r:
        q = partition(T, p, r)
        quick_sort(T, p, q-1)
        quick_sort(T, q+1, r)
        #p = q + 1

def depth(L):
    n = len(L)
    quick_sort(L, 0, n-1)
    a = 0
    maks = 0
    flag = True
    while flag:
        if maks > n-a:
            break
        flag = False
        x = a
        k = 0
        for i in range(x+1, n):
            # if L[i][0] > L[x][1]:
            #     break
            if L[i][1] <= L[x][1]:
                k += 1
            elif L[i][0] > L[x][1]:
                break
            elif not flag:
                a = i
                flag = True

        if maks < k:
            maks = k

    return maks


runtests( depth )