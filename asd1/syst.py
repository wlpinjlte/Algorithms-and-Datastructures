n=10
tab=[12,34,67,25,77,5,4,3,2,1]
for i in range(n):
    tab[i]=[tab[i]//n,tab[i]%n]
for z in range(len(tab[0])-1,-1,-1):
    c=[0 for g in range(n)]
    d=[0 for g in range(n)]
    for g in range(n):
        c[tab[g][z]]+=1
    for g in range(1,len(c)):
        c[g]+=c[g-1]
    for g in range(n-1,-1,-1):
        d[c[tab[g][z]]-1]=tab[g]
        c[tab[g][z]] -= 1
    tab,d=d,tab
    #print(tab)
    #print(d)
print(tab)