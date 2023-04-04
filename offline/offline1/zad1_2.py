from zad1testy import Node, runtests

class node:
    def __init__(self,a=None):
        self.next=None
        self.val=a

def min(first,k):
    ile=0
    f=True
    min=first
    minn=first
    while first.next is not None and ile<k:
        #print(first.next.val,min.val,first.val)
        if first.next.val<min.val:
            min=first.next
            minn=first
            f=False
        first=first.next
        ile+=1
    if f:
        return node(0)
    return minn

def SortH(first,k):
    g=node()
    g.next=first
    p=g
    while first.next is not None:
        #print_l_l(p.next)
        #print()
        #print(first.val)
        temp=min(first,k)
        #print(temp.val)
        if temp.val==0:
            g=g.next
            first=first.next
        else:
            g.next=temp.next
            temp.next=temp.next.next
            g=g.next
            g.next=first
    return p.next


runtests( SortH )