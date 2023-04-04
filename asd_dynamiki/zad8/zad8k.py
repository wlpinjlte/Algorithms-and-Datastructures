from zad8ktesty import runtests 
#f(i,j)-naprawa wyrazu gdzie i to długość s a j długość t
#f(i,j)-jeżeli s[i]==t[j] to min(f(i-1,j-1),f(i-1,j)+1,f(i,j-1)+1) a jak różne to min(f(i-1,j-1)+1,f(i-1,j)+1,f(i,j-1)+1))
def f(i,j,F,s,t):
    if F[i][j]!=10**10:
        return F[i][j]
    if s[i]==t[j]:
        F[i][j]=min(f(i-1,j-1,F,s,t),f(i-1,j,F,s,t)+1,f(i,j-1,F,s,t)+1)
    else:
        F[i][j] = min(f(i - 1, j - 1, F, s, t)+1, f(i - 1, j, F, s, t) + 1, f(i, j - 1, F, s, t) + 1)
    return F[i][j]


def napraw ( s, t ):
    #print(s,t)
    F=[[10**10 for j in range(len(t))]for i in range(len(s))]
    if s[0]==t[0]:
        F[0][0]=0
    else:
        F[0][0]=1
    for i in range(1,len(s)):
        F[i][0]=F[i-1][0]+1
        if s[i]==t[0] and F[i][0]==i+1:
            F[i][0]-=1
    for i in range(1,len(t)):
        F[0][i]=F[0][i-1]+1
        if s[0]==t[i] and F[0][i]==i+1:
            F[0][i]-=1
    return f(len(s)-1,len(t)-1,F,s,t)

runtests ( napraw )