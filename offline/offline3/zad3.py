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
        for j in range(len(tab)-i-1):
            if tab[j]>tab[j+1]:
                tab[j],tab[j+1]=tab[j+1],tab[j]
    return

def przydzial(P):
    minn=P[0][0]
    maxx=P[0][1]
    # pr=P[0][2]
    for i in range(1,len(P)):
        if minn>P[i][0]:
            minn=P[i][0]
        if maxx<P[i][1]:
            maxx=P[i][1]
        # if pr<P[i][2]:
        #     pr=P[i][2]
    return minn,maxx#,pr



def SortTab(T,P):
    #quic_sort(T,0,len(T)-1)
    minn,maxx=przydzial(P)
    #print(maxx,minn)
    k=(maxx-minn)//len(T)+1
    doc=[]
    #print(maxx,minn,len(T),k)
    tab=[[]for _ in range(minn,maxx,1)]
    for i in range(len(T)):
        tab[(int(T[i])+1-minn)//k].append(T[i])
    for i in range(len(tab)):
        # if len(tab[i])>1000:
        #     quic_sort(tab[i])
        if len(tab[i])>1:
            #print(len(tab[i]))
            #select(tab[i])
            buble(tab[i])
        # for j in range(len(tab[i])):
        #     doc.append(tab[i][j])
        doc.extend(tab[i])

    #print(tab)

    return doc

runtests( SortTab )