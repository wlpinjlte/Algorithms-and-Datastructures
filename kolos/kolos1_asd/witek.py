from kol1btesty import runtests

def bucket(T):
    maks = 0
    for el in T:
        if maks < len(el):
            maks = len(el)
    A = [[] for _ in range(maks)]
    for el in T:
        A[len(el)-1].append(el)
    return A

def change(A):
    k = 26
    n = len(A)
    C = [0]*k
    p = ord('a')
    for i in range(n):
        C[ord(A[i]) - p] += 1
    word = ""
    for i in range(k):
        while C[i] > 0:
            word += chr(i+p)
            C[i] -= 1
    return word

def counting_sort(A, i):
    k = 26
    n = len(A)
    C = [0]*k
    B = [0]*n
    p = ord('a')
    for x in A:
        C[ord(x[i]) - p] += 1

    for j in range(1,k):
        C[j] = C[j] + C[j-1]

    for j in range(n-1, -1, -1):
        x = ord(A[j][i])-p
        B[C[x]-1] = A[j]
        C[x] -= 1
    # for j in range(n):
    #     A[j] = B[j]
    return B


def f(T):
    # tu prosze wpisac wlasna implementacje
    T = bucket(T)
    n = len(T)
    A = []
    maks=0
    for i in range(n):
        for j in range(len(T[i])):
            T[i][j] = change(T[i][j])
        for j in range(i, -1, -1):
            if len(T[i])>0:
                T[i]=counting_sort(T[i], j)
        counter = 1
        for j in range(len(T[i])-1):
            if T[i][j] == T[i][j+1]:
                counter += 1
            else:
                if maks < counter:
                    maks = counter
                counter = 1
        if maks < counter:
            maks = counter

    return maks


# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( f, all_tests=True )