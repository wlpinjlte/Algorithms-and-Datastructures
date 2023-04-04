from zad7ktesty import runtests
#zwykły plecak z dfs(dla kosztów)
#f(i,w)-maks zysk z i-tego zbioru przy wadze w
#f(i,w)=max(f(i-1,w),f(i-1,w-w[i])+Z[i])
def dfs(i,j,T,visited):
    if i<0 or i>=len(T) or j<0 or j>=len(T[0]):
        return 0
    if visited[i][j]==1 or T[i][j]==0:
        return 0
    visited[i][j]=1
    return T[i][j]+dfs(i-1,j,T,visited)+dfs(i+1,j,T,visited)+dfs(i,j-1,T,visited)+dfs(i,j+1,T,visited)
def plecak(i,w,F,k,Z):
    if w<0:
        return -10**10
    if i<0:
        return 0
    if F[i][w]!=-1:
        return F[i][w]
    F[i][w]=max(plecak(i-1,w,F,k,Z),plecak(i-1,w-k[i],F,k,Z)+Z[i])
    return F[i][w]
def ogrodnik (T, D, Z, l):
    visited=[[0 for j in range(len(T[0]))]for i in range(len(T))]
    #print(T)
    k=[0for i in range(len(D))]
    for i in range(len(D)):
        #print(T[D[i]][0])
        k[i]=dfs(0,D[i],T,visited)
    print(k)
    F=[[-1for j in range(l+1)]for i in range(len(D))]
    return plecak(len(D)-1,l,F,k,Z)

runtests(ogrodnik)