from zad1ktesty import runtests
#f(i,j)-maks roznica do i-tego miejsca do j-tego
#f(i,j)=f(i,j-1)-1(jeśli S[i]==1)or f(i,j-1)+1(jeśli S[i]==0)
def f(S,i,j,F):
    if i==j:
        return 0
    if F[i][j]!=-1:
        return F[i][j]
    if S[j]=="1":
        F[i][j]=f(S,i,j-1,F)-1
    else:
        F[i][j]=f(S,i,j-1,F)+1
    return F[i][j]
def spr(S):
    for i in S:
        if i=="0":
            return 0
    return 1
def roznica(S):
    maks=0
    F=[[-1 for j in range(len(S))]for i in range(len(S))]
    for i in range(len(S)):
        for j in range(i,len(S)):
            maks=max(maks,f(S,i,j,F))
    if spr(S)==1:
        return -1
    return maks

runtests(roznica)