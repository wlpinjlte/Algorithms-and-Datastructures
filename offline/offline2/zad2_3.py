from zad2testy import runtests
import random
#do wyjebania
def partiton(tab,p,l):
    pom=random.randint(p,l)
    if tab[p]<tab[pom]<tab[l] or tab[l]<tab[pom]<tab[p]:
        tab[pom],tab[l]=tab[l],tab[pom]
    elif tab[pom]<tab[p]<tab[l] or tab[l]<tab[p]<tab[pom]:
        tab[p],tab[l]=tab[l],tab[p]
    x=tab[l]
    i=p-1
    for j in range(p,l):
        if tab[j][0]<x[0]:
            i += 1
            tab[j],tab[i]=tab[i],tab[j]
        elif tab[j][0]==x[0] and tab[j][1]>x[1]:
            i += 1
            tab[j], tab[i] = tab[i], tab[j]
    tab[l],tab[i+1]=tab[i+1],tab[l]
    return i+1

def quicsort(tab,p,l):
    tabb=[[p,l]]
    while len(tabb)>0:
        a,b=tabb.pop()
        if b-a>0:
            q=partiton(tab,a,b)
            tabb.append([q+1,b])
            tabb.append([a,q-1])

def depth(L):
    quicsort(L,0,len(L)-1)
    tabi=[]
    tab=[]
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
            tabi.append(0)
            tab.append(L[i])
    #print(z)
    return max(tabi)




runtests( depth )