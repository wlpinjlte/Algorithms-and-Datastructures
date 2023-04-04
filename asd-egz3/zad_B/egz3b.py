from egz3btesty import runtests
def f(i,j,k,L,lasti):
    #print(i,j,k)
    if i<0 or i==len(L) or j==len(L):
        return -10**10
    if L[i][j]=='#':
        return -10**10
    if i==len(L)-1 and j==len(L)-1:
        return k
    if lasti==i-1:
        return max(f(i + 1, j, k + 1, L, i), f(i, j + 1, k + 1, L, i))
    elif lasti==i+1:
         return max(f(i - 1, j, k + 1, L, i), f(i, j + 1, k + 1, L, i))
    else:
        return max(f(i-1,j,k+1,L,i),f(i+1,j,k+1,L,i),f(i,j+1,k+1,L,i))
def maze( L ):
    #F=[[-10**10 for j in range(len(L))]for i in range(len(L))]
    return f(0,0,0,L,10)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = False )
