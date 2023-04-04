from zad2testy import runtests

def percion(tab,a,b):
    x=tab[b]
    i=a-1
    for j in range(a,b):
        if tab[j][0]<x[0]:
            i+=1
            tab[j],tab[i]=tab[i],tab[j]
        elif tab[j][0]==x[0] and tab[j][1]>x[1]:
            i+=1
            tab[j], tab[i] = tab[i], tab[j]

    tab[i+1],tab[b]=tab[b],tab[i+1]

    return i+1


def quciksort(tab,a,b):
    if b-a>0:
        q=percion(tab,a,b)
        #print(q)
        quciksort(tab,q+1,b)
        quciksort(tab,a,q-1)

def depth(L):
    quciksort(L,0,len(L)-1)
    tab=[]
    tabi=[]
    z=0
    for i in range(len(L)):
        flag=True
        for j in range(z,len(tab),1):
            if tab[j][0]<=L[i][0] and tab[j][1]>=L[i][1]:
                tabi[j]+=1
                flag=False
            elif tab[j][1]<L[i][0]:
                z+=1
        if flag:
            tab.append(L[i])
            tabi.append(0)
    return max(tabi)


runtests( depth )
# tab=[9,1,6,8,4,3,2,0]
# quciksort(tab,0,len(tab)-1)
# print(tab)