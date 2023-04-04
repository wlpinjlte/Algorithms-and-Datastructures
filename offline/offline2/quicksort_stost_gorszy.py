from zad2testy import runtests

def partiton(tab,p,l):
    x=tab[l]
    i=p-1
    for j in range(p,l):
        if tab[j]<x:
            i += 1
            tab[j],tab[i]=tab[i],tab[j]
    tab[l],tab[i+1]=tab[i+1],tab[l]
    return i+1

def quicsort(tab,p,l):
    tabb=[]
    tabb.append([p,l])
    while len(tabb)>0:
        a,b=tabb.pop()
        if b-a>0:
            q=partiton(tab,a,b)
            tabb.append([q+1,b])
            tabb.append([a,q-1])
# tab=[21345,214,5,223,6,436,2,12]
# quicsort(tab,0,len(tab)-1)
# print(tab)
def depth(L):
    #quicsort(L,0,len(L)-1)
    print(L)
    return


runtests( depth )
