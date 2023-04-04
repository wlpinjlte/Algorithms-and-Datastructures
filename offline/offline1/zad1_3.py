from zad1testy import Node, runtests

class node:
    def __init__(self,a=None):
        self.next=None
        self.val=a

def add(first,d):
    while first.next is not None and first.next.val<d.val:
        first=first.next
    temp=first.next
    first.next=d
    d.next=temp

def SortH(first,k):
    sorted=Node()
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


runtests( SortH )