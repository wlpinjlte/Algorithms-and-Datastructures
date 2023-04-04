#Mateusz Waga algorytm polega na posortowaniu przydziałów względem dolnego indeksu przy czym jak indeksy są takie same to najpierw będzie przydział większym górnym indeksem w kolejnej cześć algorytmu wyzmaczam liderów zbioru i jeżeli mniejsze przydziały się w nim zawierają to zwiększam im liczebność o 1 na samym konicu biore największą wartość z tablicy liczebność liderów(tabi)
from zad2testy import runtests

def bublle_sort(tab,p,l):
    for j in range(l-p-1):
        for i in range(p,l):
            if tab[i][0] < tab[i+1][0]:
                tab[i+1], tab[i] = tab[i], tab[i+1]
            elif tab[i][0] == tab[i+1][0] and tab[i+1][1] > tab[i][1]:
                tab[i + 1], tab[i] = tab[i], tab[i + 1]


def partiton(tab,p,l): #wyznacza q(elemnty na lewo mniejsze niż q a na prawo większe)
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

def quicsort(tab,p,l):  #Quick sort zrobiony na stosie
    #tabb=[[p,l]]
    tabb=[]
    tabb.append([p,l])
    while len(tabb)>0:
        a,b=tabb.pop()
        if b-a>0:
            if b-a<3:
                bublle_sort(tab, a, b)
            else:
                q=partiton(tab,a,b)
                tabb.append([q+1,b])
                tabb.append([a,q-1])

def maxx(tabi): #wyznacza maximum z tablicy
    maxx=0
    for i in range(len(tabi)):
        if(tabi[i]>maxx):
            maxx=tabi[i]
    return maxx

def depth(L):
    quicsort(L,0,len(L)-1)
    print(L)
    tabi=[]
    tab=[]
    z=0
    n=len(L)
    for i in range(n):
        flag=True
        for j in range(z,len(tab),1):
            if tab[j][1]>=L[i][1]:
                tabi[j]+=1
                flag=False
            elif tab[j][1]<L[i][0]: #or tabi[j]<maxx(tabi)-i:
                z+=1
        if flag:
            tabi.append(0)
            tab.append(L[i])

    #print(z)
    return maxx(tabi)


runtests( depth )
