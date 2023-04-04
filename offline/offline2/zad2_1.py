from zad2testy import runtests

def partiton(tab,p,l):
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
    tabb=[]
    tabb.append([p,l])
    while len(tabb)>0:
        a,b=tabb.pop()
        if b-a>0:
            q=partiton(tab,a,b)
            tabb.append([q+1,b])
            tabb.append([a,q-1])

def maxx(tabi):
    maxx=0
    for i in range(len(tabi)):
        if(tabi[i]>maxx):
            maxx=tabi[i]
    return maxx

def depth(L):
    quicsort(L,0,len(L)-1)
    #sorted(L)
    tabi=[]
    tab=[]
    #max=0
    for i in range(len(L)):
        flag=True
        for j in range(len(tab)):
            if tab[j][0]<=L[i][0] and tab[j][1]>=L[i][1]:
                tabi[j]+=1
                flag=False
        if flag:
            tabi.append(0)
            tab.append(L[i])
    return maxx(tabi)


    #sorted(L)
    #print(L)


runtests( depth ) 
