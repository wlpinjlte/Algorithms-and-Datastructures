from zad1testy import Node, runtests

class node:
    def __init__(self,val=None):
        self.next=None
        self.val=val

def podzial(first):
    tab=[]
    tab.append(first)
    while first.next is not None:
        if first.val>first.next.val:
            tab.append(first.next)
            temp=first.next
            first.next=None
            first=temp
        else:
            first=first.next
    return tab

def scal(first1,first2):
    g=node()
    p=g
    while first1 is not None and first2 is not None:
        if first1.val>first2.val:
            g.next=first2
            first2=first2.next
            g=g.next
        else:
            g.next = first1
            first1 = first1.next
            g = g.next
    if first1 is not None:
        g.next=first1
    else:
        g.next=first2
    return p.next

def merge_sort1(first):
    tab=podzial(first)
    #print(tab)
    while len(tab)>1:
        tabb=[]
        for i in range(len(tab)//2):
            tabb.append(scal(tab[2*i],tab[2*i+1]))
        if(len(tab)%2!=0):
            tabb.append(tab[len(tab)-1])
        tab,tabb=tabb,tab
    #print(tab[0].val)
    return tab[0]

def merge_sort2(first):
    tab=podzial(first)
    while len(tab)>1:
        p1=tab.pop(0)
        p2=tab.pop(0)
        tab.append(scal(p1,p2))
    return tab[0]

def merge_sort3(first):
    tab=podzial(first)
    while len(tab)>1:
        p1=tab[0]
        p2=tab[1]
        tab=tab[2:]
        tab.append(scal(p1,p2))
    return tab[0]

def SortH(l,k):
    return merge_sort1(l)


runtests( SortH )
