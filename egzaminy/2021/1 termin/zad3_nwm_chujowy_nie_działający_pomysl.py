from zad3testy import runtests
import queue



def kintersect(A, k):
    global ile
    A = sorted(A, key=lambda x: x[0])
    print(A)
    qs = queue.PriorityQueue()
    ile = k
    pocz = []
    maxx = 0
    for i in range(len(A)):
        ile += 1
        qs.put(i, A[i][1])
        pocz.append(A[i][0])
        x = qs.get()
        # print(x)
        while A[x][1] <= A[i][0]:
            # print(ile)
            ile -= 1
            pocz.remove(A[x][0])
            if not qs.empty():
                x = qs.get()
            else:
                x = None
                break
        if x != None:
            qs.put(x, A[x][1])
        if k == ile:
            maxx = max(maxx, A[x][1] - max(pocz))
        elif ile > k:
            print("elo")
    print(maxx)
    return [0]