class Node():
    def __init__(self,val=None):
        self.val=val
        self.next=None

def print_node(first):
    while first is not None:
        print('->', first.val, end='')
        first = first.next

def make_linked_list(tab):
    first = None
    n = len(tab)
    for i in range(n - 1, -1, -1):
        tem = Node(tab[i])
        tem.next = first
        first = tem
    return first

def roz(a):
    r=10e10
    prev=a
    a=a.next
    while a is not None:
        if abs(r)>abs(prev.val-a.val):
            r=a.val-prev.val
        prev=a
        a=a.next
    return r

def repair(p):
    first=p
    r=roz(p)
    prev=p
    p=p.next
    cout=0
    while p is not None:
        #print(p.val)
        #print(r)
        if p.val-prev.val!=r:
            cout+=1
            prev.next=Node(prev.val+r)
            prev=prev.next
            prev.next=p
        else:
            prev=p
            p=p.next
    return cout,first

tab=[1,5,6]
print(repair(make_linked_list(tab))[0])