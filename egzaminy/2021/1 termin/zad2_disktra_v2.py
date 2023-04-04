from zad2testy import runtests
import queue

def robot(L, A, B):
    visited=[[[[10**10 for z in range(3)]for g in range(4)]for j in range(len(L[0]))]for i in range(len(L))]
    qs=queue.PriorityQueue()
    ss=[60,40,30]
    ii=[(0,1),(-1,0),(0,-1),(1,0)]
    qs.put((0,0,0,A))
    visited[0][0][0][0]=0
    while not qs.empty():
        d,p,s,P=qs.get()
        #print(P)
        if L[P[1]][P[0]]=="X":
            continue
        if P==B:
            return d
        # if visited[P[1]][P[0]][p][s]!=10**10:
        #     continue
        # visited[P[1]][P[0]][p][s]=d
        if d+45<visited[P[1]][P[0]][(p + 1) % 4][0]:
            visited[P[1]][P[0]][(p + 1) % 4][0]=d+45
            qs.put((d + 45, (p + 1) % 4, 0, P))
        if d+45<visited[P[1]][P[0]][(p - 1) % 4][0]:
            visited[P[1]][P[0]][(p - 1) % 4][0]=d+45
            qs.put((d + 45, (p - 1) % 4, 0, P))
        if d+ss[s]<visited[P[1]+ii[p][0]][P[0]+ii[p][1]][p][min(s+1,2)]:
            visited[P[1] + ii[p][0]][P[0] + ii[p][1]][p][min(s + 1, 2)]=d+ss[s]
            qs.put((d+ss[s],p,min(s+1,2),(P[0]+ii[p][1],P[1]+ii[p][0])))

    return None


runtests(robot)

