from zad1ktesty import runtests
#f(i,j)-największa róźnica od i do j
#f(i,j)=f(i,j-1)+-1(jeżeli S[j]=1 to 1 jeżeli 0 to -1)
def f(i,j,F,S):
    if F[i][j]!=None:
        return F[i][j]
    if i==j:
        if int(S[i])==1:
            F[i][j]=1
        else:
            F[i][j]=-1
        return F[i][j]
    if int(S[j])==1:
        F[i][j]=f(i,j-1,F,S)+1
    else:
        F[i][j] = f(i, j - 1, F, S) -1
    return F[i][j]
def roznica( S ):
    #print(S)
    F=[[None for j in range(len(S))]for i in range(len(S))]
    min=10**10
    for a in range(len(S)):
        for b in range(a+1,len(S)):
            f(a,b,F,S)
            if min>F[a][b]:
                min=F[a][b]
    #print(F[0][len(S)-1],len(S)-1)
    if F[0][len(S)-1]==len(S):
        return -1
    #print(F)

    return abs(min)

runtests ( roznica )