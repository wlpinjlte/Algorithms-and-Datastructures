from zad2ktesty import runtests
#f(a,b)-czy z a do b jest palindorom
#f(a,b)=jeżeli S[a]==S[b] to f(a+1,b-1)
def f(i,j,F,S):
    if F[i][j]!=None:
        return F[i][j]
    if i==j:
        F[i][j]=1
        return F[i][j]
    if i+1==j:
        if S[i]==S[j]:
            F[i][j]=1
        else:
            F[i][j]=0
        return F[i][j]
    if S[i] == S[j]:
        F[i][j] = f(i + 1, j - 1, F, S)
        return F[i][j]
    else:
        F[i][j] = 0
        return F[i][j]

def palindrom( S ):
    F=[[None for j in range(len(S))]for i in range(len(S))]
    maks=(0,0,0)
    for a in range(len(S)):
        for b in range(a+1,len(S)):
            f(a,b,F,S)
            if maks[0]<b-a and F[a][b]==1:
                maks=(b-a,a,b)
                #print(maks)
    return S[maks[1]:maks[2]+1]

runtests ( palindrom )