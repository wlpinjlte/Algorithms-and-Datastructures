def find(tab):
    p=0
    k=len(tab)
    while p!=k and k-p!=1:
        s=(p+k)//2
        print(p,k,s)
        if tab[s]!=s:
            k=s
        else:
            p=s
    return k

tab=[0,1,2,3,4,5]
print(find(tab))