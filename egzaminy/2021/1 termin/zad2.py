from zad2testy import runtests
import queue
import sys
sys.setrecursionlimit(3000)
#F[i][j][p][s]=minimalny czas aby dostać się do pola i j z pozycja p oraz szybkoscia s
#F[i][j][p][s]=min(F[i][j][(p+1)%4][0]+45,F[i][j][(p-1)%4][0]+45,F[i][j][p][min(2,s+1)]+60/45/30)
BB=[]
v=[]
def f(i,j,p,s,F,L):
    global BB,v
    #print(i,j)
    if F[j][i][p][s]!=10**10:
        return F[j][i][p][s]
    if BB[0]==i and BB[1]==j:
        F[j][i][p][s]=0
        return 0
    ruch = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    ss = [60, 40, 30]
    if L[j][i]=="X":
        F[j][i][p][s]=10**10
        return 10**10
    F[j][i][p][s]=f(i+ruch[p][0],j+ruch[p][1],p,min(2,s+1),F,L)+ss[s]
    F[j][i][p][s] = min(F[j][i][p][s],min(f(i, j, (p - 1) % 4, 0, F, L) + 45, f(i, j, (p + 1) % 4, 0, F, L) + 45))
    return F[j][i][p][s]
def robot(L, A, B):
    #print((-1%4))
    F=[[[[10**10 for g in range(3)]for z in range(4)]for j in range(len(L[0]))]for i in range(len(L))]
    global BB,v
    BB=[B[0],B[1]]
    f(A[0], A[1], 0, 0, F, L)
    #print(F)
    if F[A[1]][A[0]][0][0]>10**10:
        return None
    return F[A[1]][A[0]][0][0]


runtests(robot)

