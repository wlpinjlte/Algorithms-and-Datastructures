class node:
    def __init__(self,a=None):
        self.next=None
        self.val=a

def print_l_l(first):
    while first is not None:
        print("->",first.val,end='')
        first=first.next

def make_linked_list(tab):
    first=None
    n=len(tab)
    for i in range(n-1,-1,-1):
        tem=node(tab[i])
        tem.next=first
        first=tem
    return first

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


def sort(first,k):
    g=first
    while first.next is not None:
        temp=min(first,k)
        print(temp)
        if(temp==0):
            first=first.next
        else:
            first.val,temp.val=temp.val,first.val
            first=first.next
    return g
tab=[2, 6, 6, 10, 29, 24, 31, 43, 36, 45, 51, 49, 52, 56, 53, 56, 61, 58, 71, 75, 72, 79, 93, 82, 99]
print_l_l(sort(make_linked_list(tab),1))