#Mateusz Waga algorytm łaczy dwa rodzaje sortowań(insert i merge sort) dla k<=10 robi insert(O(n)=n*k) a dla k>10 merge(O(n)=n*logk+cn)
from zad1testy import Node, runtests

class node:
    def __init__(self,val=None):
        self.next=None
        self.val=val



def scal(first1,first2):    #scala dwie listy
    g=node()
    p=g
    while first1 is not None and first2 is not None:
        if first1.val>first2.val:
            g.next=first2
            first2=first2.next
        else:
            g.next=first1
            first1=first1.next
        g=g.next

    if first1 is not None:
        g.next=first1
    else:
        g.next=first2

    return p.next


def podzial(l): #dzieli na ciągi rosnące
    heads=[]
    heads.append(l)
    while l.next is not None:
        if l.val>l.next.val:
            heads.append(l.next)
            t=l
            l = l.next
            t.next=None
        else:
            l=l.next
    #print(2)
    return heads

def sort_m(tab): #merge sort dla tablic
    tabb=[]
    while len(tab)!=1:
        n=len(tab)
        for i in range(n//2):
            tabb.append(scal(tab[2*i],tab[2*i+1]))
        if n%2==1:
            tabb.append(tab[n-1])
        tab,tabb=tabb,tab
        tabb=[]
    return tab[0]

def SortM(l,k): #merge sort dla k
    ile=0
    head=[]
    g=l
    for i in range(k):
        l=l.next
    if l is None:
        return sort_m(podzial(g))
    p=l.next
    l.next=None
    head.append(sort_m(podzial(g)))
    first=head[0]
    l=p
    g=p

    while l is not None:
        ile+=1
        if ile==k:
            ile = 0
            p = l.next
            l.next = None
            head[0]=scal(head[0],sort_m(podzial(g)))
            for i in range(k):
                head[0]=head[0].next
            l=p
            g=p
        else:
            l=l.next
    #print(1)
    if ile!=0:
        head[0] = scal(head[0], sort_m(podzial(g)))
    return first

def add(first,d): #wstawia element el do l_l
    while first.next is not None and first.next.val<d.val:
        first=first.next
    temp=first.next
    first.next=d
    d.next=temp

def dl(first): #liczy dł l_l
    ile=0
    while first is not None:
        first=first.next
        ile+=1
    return ile

def SortI(first,k): #iner sort
    sorted=node()
    #print(dl(first))
    ile=0
    p=sorted
    while first is not None:
        if ile>k:
            sorted=sorted.next
        ile+=1
        q=first.next
        first.next=None
        add(sorted,first)
        first=q
    return p.next

def SortH(first,k):
    if (k <= 10):
        return SortI(first, k)
    # n = dl(first)
    # if (k > math.log(n)):
    #     return SortM(first,k)
    return SortM(first, k)

runtests( SortH )