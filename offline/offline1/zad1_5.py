from zad1testy import Node, runtests

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

def SortH(l,k):
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


runtests( SortH )