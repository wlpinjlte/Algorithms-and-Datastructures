from zad2ktesty import runtests
#f(i,j)-czy od i do j jest palindrom
#f(i,j)=0 jeśli S[i]!=S[j] or f(i,j)=f(i+1,j-1) jeśli S[i]==S[j]
def f(S,i,j,F):
    if F[i][j]!=-1:
        return F[i][j]
    if S[i]==S[j]:
        F[i][j]=f(S,i+1,j-1,F)
    else:
        F[i][j]=0
    return F[i][j]
def palindrom(S):
    F=[[-1for j in range(len(S))]for i in range(len(S))]
    for i in range(len(S)-1):
        F[i][i]=1
        if S[i]==S[i+1]:
            F[i][i+1]=1
    F[len(S)-1][len(S)-1]=1
    maks=(0,(0,0))
    for i in range(len(S)):
        for j in range(i,len(S)):
            if f(S,i,j,F)==1:
                if maks[0]<j-i:
                    maks=(j-i,(i,j))
    return S[maks[1][0]:maks[1][1]+1]



runtests(palindrom)