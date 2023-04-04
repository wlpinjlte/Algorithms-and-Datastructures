from zad3testy import runtests

def prection(tab,a,b):
    x=tab[b]
    i=a-1
    for j in range(a,b):
        if x>tab[j]:
            i+=1
            tab[j],tab[i]=tab[i],tab[j]
    tab[b],tab[i+1]=tab[i+1],tab[b]
    return i+1

def quic_sort(tab,a,b):
    if b-a>0:
        q=prection(tab,a,b)
        quic_sort(tab,q+1,b)
        quic_sort(tab,a,q-1)

def minn(tab,k):
    minnn=k
    for i in range(k,len(tab)):
        if tab[minnn]>tab[i]:
            minnn=i
    return minnn

def select(tab):
    for i in range(len(tab)):
        min_=minn(tab,i)
        tab[i],tab[min_]=tab[min_],tab[i]
    return

def buble(tab):
    for i in range(len(tab)):
        flag=True
        for j in range(len(tab)-i-1):
            if tab[j]>tab[j+1]:
                tab[j],tab[j+1]=tab[j+1],tab[j]
                flag=False
        if flag:
            return
    return




def SortTab(T,P):
    doc=[]
    tab=[[]for _ in range(1,len(T)+1)]
    for i in range(len(T)):
        tab[int(T[i])].append(T[i])
    for i in range(len(tab)):
        if len(tab[i])>1:
            buble(tab[i])
        doc.extend(tab[i])

    return doc

runtests( SortTab )