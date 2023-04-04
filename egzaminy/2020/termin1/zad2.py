from zad2testy import runtests

#f(i,j)-min suma od i do j sumując najkorzystniej
#f(i,j)=max(suma(i,j),min(f(i,k),f(k+1,j)))(k=1...j-1)
def sum(i,j,tab):
    s=0
    for z in range(i,j+1):
        s+=tab[z]
    return abs(s)
def f(i,j,tab,F):

    #print()
    if F[i][j]!=10**10:
        return F[i][j]
    #print(i, j)
    # if i==j:
    #     #print(1)
    #     F[i][j]=tab[i]
    #     return abs(tab[i])
    if i+1==j:
        #print(1)
        F[i][j]=tab[i]+tab[j]
        return abs(tab[i]+tab[j])
    #print(i, j)
    F[i][j]=sum(i,j,tab)
    temp=10**10
    for z in range(i+1,j):
        temp=min(temp,min(f(i,z,tab,F),f(z,j,tab,F)))
    F[i][j]=max(sum(i,j,tab),temp)
    return F[i][j]
def opt_sum(tab):
    F=[[10**10 for i in range(len(tab))]for j in range(len(tab))]

    #print(tab)
    f(0,len(tab)-1,tab,F)
    #print(F)
    return F[0][len(tab)-1]


runtests( opt_sum )
