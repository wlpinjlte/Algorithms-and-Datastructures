from zad1testy import Node, runtests
import math

class node:
    def __init__(self,a=None):
        self.next=None
        self.val=a

def scal(first1,first2):
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

def podzial(l):
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

def SortM(l):
    tab=podzial(l)
    tabb=[]
    #print(3)
    #n=len(tab)
    #for i in range(n):
    #    print(tab[i].val)
    while len(tab)!=1:
        n=len(tab)
        for i in range(n//2):
            tabb.append(scal(tab[2*i],tab[2*i+1]))
            #print(tabb[i].val)
        if n%2==1:
            tabb.append(tab[n-1])
        #print(1)
        tabb,tab=tab,tabb
        tabb=[]
    return tab[0]

def add(first,d):
    while first.next is not None and first.next.val<d.val:
        first=first.next
    temp=first.next
    first.next=d
    d.next=temp

def dl(first):
    ile=0
    while first is not None:
        first=first.next
        ile+=1
    return ile

def SortI(first,k):
    sorted=Node()
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

def podzial2(l,k):
    heads=[]
    ile=0
    heads.append(l)
    while l.next and ile<k is not None:
        ile+=1
        if l.val>l.next.val:
            heads.append(l.next)
            t=l
            l = l.next
            t.next=None
        else:
            l=l.next
    p=l.next
    l.next=None
    #print(2)
    return heads,p

def sort_m(l,k):
    x=podzial2(l,k)
    tab=x[0]
    p=x[1]
    #print(tab)
    tabb = []
    # print(3)
    # n=len(tab)
    # for i in range(n):
    #    print(tab[i].val)
    while len(tab) != 1:
        n = len(tab)
        for i in range(n // 2):
            tabb.append(scal(tab[2 * i], tab[2 * i + 1]))
            #print(tabb[i].val)
        if n % 2 == 1:
            tabb.append(tab[n - 1])
        #print(1)
        tab, tabb = tabb, tab
        tabb = []
    print(1)
    return tab[0],p

def SortIl(first,k):
    a=Node()
    p=a
    x=sort_m(first,k)
    first=x[1]
    a.next=x[0]
    #print(first.val)
    while first is not None:
        #print(first.val,first.next.val)
        q=first.next
        first.next=None
        add(a,first)
        first=q
        a = a.next
    return p.next



def SortH(first,k):
    if(k<=10):
        return SortI(first,k)
    n=dl(first)
    if(k>math.log(n)):
        return SortM(first)
    return SortIl(first,k)


runtests( SortH )