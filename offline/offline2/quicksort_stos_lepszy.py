import random
def partiton(tab,p,l):
    pom=random.randint(p,l)
    if tab[p]<tab[pom]<tab[l] or tab[l]<tab[pom]<tab[p]:
        tab[pom],tab[l]=tab[l],tab[pom]
    elif tab[pom]<tab[p]<tab[l] or tab[l]<tab[p]<tab[pom]:
        tab[p],tab[l]=tab[l],tab[p]
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

tab=[9,1,6,8,4,3,2,0]
quicsort(tab,0,len(tab)-1)
print(tab)
