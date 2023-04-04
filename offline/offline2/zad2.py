#Mateusz Waga algorytm polega na posortowaniu przydziałów względem dolnego indeksu przy czym jak indeksy są takie same to najpierw będzie przydział większym górnym indeksem w kolejnej cześć algorytmu wyzmaczam liderów zbioru i jeżeli mniejsze przydziały się w nim zawierają to zwiększam im liczebność o 1 na samym konicu biore największą wartość z tablicy liczebność liderów(tabi) w najgorszym przypadku O(n)=n^2 ale oczekiwana to O(n)=nlogn
from zad2testy import runtests

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
            q=partiton(tab,a,b)
            tabb.append([q+1,b])
            tabb.append([a,q-1])

def maxx(tabi): #wyznacza maximum z tablicy
    maxxx=0
    for i in range(len(tabi)):
        if(tabi[i]>maxxx):
            maxxx=tabi[i]
    return maxxx
def bubble(T, n):
    for i in range(n-1, 0, -1):
        if T[i][0] == T[i-1][0] and T[i][1] > T[i-1][1]:
            T[i], T[i-1] = T[i-1], T[i]

def depth(L):
    quicsort(L,0,len(L)-1)
    #bubble(L,len(L)-1)
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
            elif tab[j][1]<L[i][0]: #or tabi[j]<maxx(tabi)-i: #jeżeli przydział mojego lidera jest mniejszy niż początek bieżącego to nie rozpatruje już tego lidera
                z+=1
        if flag:
            tabi.append(0)
            tab.append(L[i])

    #print(z)
    return maxx(tabi)


runtests( depth )
