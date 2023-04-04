from zad2testy import runtests

def percion(tab,a,b):
    x=tab[b]
    i=a-1
    for j in range(a,b):
        if tab[j]<x:
            i+=1
            tab[j],tab[i]=tab[i],tab[j]

    tab[i+1],tab[b]=tab[b],tab[i+1]

    return i+1


def quciksort(tab,a,b):
    if b-a>0:
        q=percion(tab,a,b)
        #print(q)
        quciksort(tab,q+1,b)
        quciksort(tab,a,q-1)
    return

def depth(L):
    quciksort(L,0,len(L)-1)
    print(L)
    return


#runtests( depth )
tab=[9,1,6,8,4,3,2,0]
quciksort(tab,0,len(tab)-1)
print(tab)