from collections import deque
from kolutesty import runtests

def a(disk, depends):
    n = len(disk)
    ile = 0
    counter = -1
    A = deque()
    B = deque()
    Ile_d = [0 for _ in range(n)]
    D = [[] for _ in range(n)]
    for i in range(n):
        if len(depends[i]) == 0:
            if disk[i] == 'A':
                A.append(i)
            else:
                B.append(i)
        Ile_d[i] = len(depends[i])
        for j in depends[i]:
            D[j].append(i)

    while ile < n:
        counter += 1
        while A:
            x = A.pop()
            ile += 1
            for y in D[x]:
                Ile_d[y] -= 1
                if Ile_d[y] == 0:
                    if disk[y] == 'A':
                        A.append(y)
                    else:
                        B.append(y)

        if ile == n: return counter

        counter += 1
        while B:
            x = B.pop()
            ile += 1
            for y in D[x]:
                Ile_d[y] -= 1
                if Ile_d[y] == 0:
                    if disk[y] == 'A':
                        A.append(y)
                    else:
                        B.append(y)

    return counter

def b(disk, depends):
    n = len(disk)
    ile = 0
    counter = -1
    A = deque()
    B = deque()
    Ile_d = [0 for _ in range(n)]
    D = [[] for _ in range(n)]
    for i in range(n):
        if len(depends[i]) == 0:
            if disk[i] == 'A':
                A.append(i)
            else:
                B.append(i)
        Ile_d[i] = len(depends[i])
        for j in depends[i]:
            D[j].append(i)

    while ile < n:
        counter += 1
        while B:
            x = B.pop()
            ile += 1
            for y in D[x]:
                Ile_d[y] -= 1
                if Ile_d[y] == 0:
                    if disk[y] == 'A':
                        A.append(y)
                    else:
                        B.append(y)

        if ile == n: return counter

        counter += 1
        while A:
            x = A.pop()
            ile += 1
            for y in D[x]:
                Ile_d[y] -= 1
                if Ile_d[y] == 0:
                    if disk[y] == 'A':
                        A.append(y)
                    else:
                        B.append(y)

    return counter



def swaps( disk, depends ):
    return min(a(disk, depends), b(disk, depends))



runtests(swaps, all_tests=True)