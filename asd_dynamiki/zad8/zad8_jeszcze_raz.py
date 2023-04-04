from zad8ktesty import runtests
#f(i,j)-min zmiany liter z slowa s do i-tej pozycji by uzyskać slowo t do j-tej pozycji
#f(i,j)=f(i-1,j-1)(jeśli s[i]=t[j]) a jeżeli nie to min(f(i-1,j)+1,f(i,j-1)+1)
def f(i,j,s,t,F):
    if F[i][j]!=10**10:
        return F[i][j]
    if s[i]==t[j]:
        F[i][j]=f(i-1,j-1,s,t,F)
    else:
        F[i][j]=min(f(i-1,j,s,t,F)+1,f(i,j-1,s,t,F)+1,f(i-1,j-1,s,t,F)+1)
    return F[i][j]
def napraw ( s, t ):
    F=[[10**10for j in range(len(t))]for i in range(len(s))]
    if s[0]==t[0]:
        F[0][0]=0
    else:
        F[0][0]=1
    for i in range(1,len(s)):
        F[i][0]=F[i-1][0]+1
        if t[0]==s[i] and F[i][0]==i+1:
            F[i][0]-=1
    for i in range(1,len(t)):
        F[0][i]=F[0][i-1]+1
        if s[0]==t[i] and F[0][i]==i+1:
            F[0][i]-=1
    return f(len(s)-1,len(t)-1,s,t,F)
runtests(napraw)