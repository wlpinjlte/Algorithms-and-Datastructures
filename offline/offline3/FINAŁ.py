#Mateusz Waga program polega na wytyczeniu właściwych przydziałów z jakiego są liczby po czym stosujemy bucket sort jeżeli w kubełku jest wiecej niż jeden element stosujemy bubble sort(zazwyczaj stosunkowo mało elementów) po czym taka przygotowaną tablice extendujemy do tablicy docelowej złożoność oczekiwana to n a bardzo pesmistyczna n^2
from zad3testy import runtests

def buble(tab):#ulepszony bubble sort
    for i in range(len(tab)):
        flag=True
        for j in range(len(tab)-i-1):
            if tab[j]>tab[j+1]:
                tab[j],tab[j+1]=tab[j+1],tab[j]
                flag=False
        if flag:
            return
    return
def percition(a,b,tab):
    x=tab[b]
    i=a-1
    for j in range(a,b):
        if x>tab[j]:
            i+=1
            tab[j],tab[i]=tab[i],tab[j]
    tab[b],tab[i+1]=tab[i+1],tab[b]
    return i+1

def qucik_sort(tab,a,b):
    if b-a>0:
        q=percition(a,b,tab)
        qucik_sort(tab,a,q-1)
        qucik_sort(tab,q+1,b)
    return

def SortTab(T,P):#właściwy algorytm
    minn=min(P,key=lambda x:x[0])[0]
    maxx=max(P,key=lambda x:x[1])[1]
    #maxx=len(T)
    doc=[]
    tab=[[]for _ in range(maxx-minn+1)]
    for i in range(len(T)):
        tab[int(T[i])-minn].append(T[i])
    for i in range(len(tab)):
        if len(tab[i])>1:
            buble(tab[i])
            #qucik_sort(tab[i],0,len(tab[i])-1)
        doc.extend(tab[i])

    return doc

runtests( SortTab )