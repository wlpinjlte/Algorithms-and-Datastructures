from zad1testy import Node, runtests

class node:
    def __init__(self,a=None):
        self.next=None
        self.val=a

def min(first,k):
    ile=0
    f=True
    min=first
    while first.next is not None and ile<k:
        if first.next.val<min.val:
            min=first.next
            f=False
        first=first.next
        ile+=1
    if f:
        return 0
    return min

def SortH(first,k):
    g = first
    while first.next is not None:
        temp = min(first, k)
        #print(temp)
        if (temp == 0):
            first = first.next
        else:
            first.val, temp.val = temp.val, first.val
            first = first.next
    return g


runtests( SortH ) 
