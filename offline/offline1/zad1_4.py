from zad1testy import Node, runtests

class node:
    def __init__(self,a=None):
        self.next=None
        self.val=a

def add(first, el): #dodawanie do listy
    if first is None:
        return el
    p = first
    q = None
    if el.val < p.val:
        first = el
        el.next = p
        return first
    while p is not None and el.val > p.val:
        q=p
        p=p.next
    el.next = p
    q.next = el
    return first

def SortH(first,k):
    p = first
    sorted = None

    while p is not None:
        q = p
        p = p.next
        q.next=None
        sorted = add(sorted, q)

    return sorted


runtests( SortH )