from zad1testy import Node, runtests

class node:
    def __init__(self,a=None):
        self.next=None
        self.val=a

def lewo(i):
    return 2*i+1
def prawo(i):
    return 2*i+2
def rodzic(i):
    return (i-1)//2

def heapify(tab,n,i):
    l=lewo(i)
    r=prawo(i)
    ak=i
    if l<n and tab[l].val<tab[ak].val:
        ak=l
    if r<n and tab[r].val<tab[ak].val:
        ak=r
    if ak!=i:
        tab[i],tab[ak]=tab[ak],tab[i]
        heapify(tab,n,ak)


def SortH(first,k):
    tab=[]
    g=node()
    p=g
    for i in range(k+1):
        if first is None:
            k = k-1
            break
        tab.append(first)
        first=first.next
    #print(1)
    for i in range(rodzic(k+1),-1,-1):
        heapify(tab,k+1,i)
    #print(2)
    while first is not None:
        g.next=tab[0]
        tab[0]=first
        heapify(tab,k+1,0)
        g=g.next
        first=first.next
    #print(3)
    for i in range(k,-1,-1):
        g.next=tab[0]
        tab[0],tab[i]=tab[i],tab[0]
        heapify(tab,i,0)
        g=g.next
    g.next=None
    return p.next


runtests( SortH )
