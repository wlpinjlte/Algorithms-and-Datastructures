from zad2testy import runtests
import queue


def robot(L, A, B):
    #print(A)
    ss = [60, 40, 30]
    qs = queue.PriorityQueue()
    visited = [[[[-1 for g in range(3)] for z in range(4)] for j in range(len(L[0]))] for i in range(len(L))]
    ruch = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    qs.put((0, A[0], A[1], 0, 0))
    while not qs.empty():
        d, i, j, p, s = qs.get()
        #print(d)
        if (i,j)==B:
            return d
        if visited[j][i][p][s] != -1 or L[j][i] == 'X':
            continue
        visited[j][i][p][s] =1
        qs.put((d + 45, i, j, (p + 1) % 4, 0))
        qs.put((d + 45, i, j, (p - 1) % 4, 0))
        i += ruch[p][0]
        j += ruch[p][1]
        #if visited
        qs.put((d + ss[s], i, j, p, min(2, 1 + s)))


runtests(robot)