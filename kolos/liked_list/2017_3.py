class Node():
    def __init__(self,val=None):
        self.val=val
        self.next=None

def make_linked_list(tab):
    first=None
    for i in range(len(tab)-1,-1,-1):
        temp=Node(tab[i])
        temp.next=first
        first=temp
    return first


def pol(a,b):
    firsta=a
    firstb=b
    while a.next is not None:
        a=a.next
    while b.next is not None:
        b=b.next
    b.next=Node(1)
    b=b.next
    a.next=b
    b.next=Node(23)
    b=b.next
    b.next=Node(231)
    return firsta,firstb

def print_link(first):
    while first is not None:
        print('->',first.val,end="")
        first=first.next

def odd(a,b):
    guardian=Node()
    guardian.next=b
    firsta=a
    p=b
    prev=guardian
    flag=False
    while a is not None:
        p=b
        prev=guardian
        while p is not None:
            if a is p:
                flag=True
                break
            prev=p
            p=p.next
        if flag:
            break
        a=a.next
    counter=0
    while a is not None:
        counter+=1
        prev.next = Node(a.val)
        prev = prev.next
        a=a.next
    return counter

tab=[1,2,3,4,5]
tab2=[3,2]
firsta,firstb=pol(make_linked_list(tab),make_linked_list(tab2))

print(odd(firsta,firstb))
