from zad2testy import runtests
#f(i,j)-min suma od i do j sumując najkorzystniej
#f(i,j)=max(suma(i,j),min(f(i+1,j),f(i,j-1)))
def sum(i,j,tab):
    s=0
    for z in range(i,j+1):
        s+=tab[z]
    return abs(s)
def f(i,j,tab,F):
    if F[i][j]!=10**10:
        return F[i][j]
    if i+1==j:

        F[i][j]=tab[i]+tab[j]
        return abs(tab[i]+tab[j])
    #print(i, j)
    F[i][j]=sum(i,j,tab)
    F[i][j]=max(sum(i,j,tab),min(f(i+1,j,tab,F),f(i,j-1,tab,F)))
    return F[i][j]
def opt_sum(tab):
    #tab = [ 1, -1, -1, 1]
    F=[[10**10 for i in range(len(tab))]for j in range(len(tab))]

    return f(0,len(tab)-1,tab,F)


runtests( opt_sum )
