# from zad1testy import Node, runtests
#
# class node:
#     def __init__(self,val=None):
#         self.next=None
#         self.val=val
#
# def print_l_l(first):
#     while first is not None:
#         print("->",first.val,end='')
#         first=first.next
#
# def make_l_l(tab):
#     first=None
#     for i in range(len(tab)-1,-1,-1):
#         temp=node(tab[i])
#         temp.next=first
#         first=temp
#     return first
#
#
# def scal(first1,first2):
#     g=node()
#     p=g
#     while first1 is not None and first2 is not None:
#         if first1.val>first2.val:
#             g.next=first2
#             first2=first2.next
#         else:
#             g.next=first1
#             first1=first1.next
#         g=g.next
#
#     if first1 is not None:
#         g.next=first1
#     else:
#         g.next=first2
#
#     return p.next
#
# def scalk(first1,first2,k):
#     g=node()
#     p=g
#     ile=0
#     while first1 is not None and first2 is not None:
#         ile+=1
#         if first1.val>first2.val:
#             g.next=first2
#             first2=first2.next
#         else:
#             g.next=first1
#             first1=first1.next
#         if k is not None and ile==k:
#             q=g.next
#         g=g.next
#     if k is not None and ile == k:
#         q = g
#     if first1 is not None:
#         g.next=first1
#     else:
#         g.next=first2
#     if k is not None:
#         return q
#     return p.next
#
# def podzial(l):
#     heads=[]
#     heads.append(l)
#     while l.next is not None:
#         if l.val>l.next.val:
#             heads.append(l.next)
#             t=l
#             l = l.next
#             t.next=None
#         else:
#             l=l.next
#     #print(2)
#     return heads
#
# def sort_m(tab):
#     tabb=[]
#     while len(tab)!=1:
#         n=len(tab)
#         for i in range(n//2):
#             tabb.append(scal(tab[2*i],tab[2*i+1]))
#         if n%2==1:
#             tabb.append(tab[n-1])
#         tab,tabb=tabb,tab
#         tabb=[]
#     return tab[0]
#
# def SortH(l,k):
#     ile=0
#     head=[]
#     g=l
#     flag=False
#     while ile<k:
#         ile+=1
#         l=l.next
#     if l is None:
#         return sort_m(podzial(g))
#     p=l.next
#     l.next=None
#     head.append(sort_m(podzial(g)))
#     l=p
#     g=l
#     ile=0
#     while l is not None:
#         #print(l.val)
#         ile += 1
#         if ile==k and flag==False:
#             flag=True
#             # print(1)
#             ile = 0
#             p = l.next
#             l.next = None
#             # print(head[0].val,g.val)
#             head[0] = scalk(head[0], sort_m(podzial(g)), k)
#             first=head[0]
#             l = p
#             g = l
#
#         elif ile==k and flag==True:
#             #print(1)
#             ile = 0
#             p = l.next
#             l.next = None
#             #print(head[0].val,g.val)
#             head[0]=scalk(head[0],sort_m(podzial(g)),k)
#             l = p
#             g=l
#         else:
#             l = l.next
#     return first
#
#
# runtests( SortH )



# from zad1testy import Node, runtests
#
# class node:
#     def __init__(self,val=None):
#         self.next=None
#         self.val=val
#
# def print_l_l(first):
#     while first is not None:
#         print("->",first.val,end='')
#         first=first.next
#
# def make_l_l(tab):
#     first=None
#     for i in range(len(tab)-1,-1,-1):
#         temp=node(tab[i])
#         temp.next=first
#         first=temp
#     return first
#
#
# def scal(first1,first2):
#     g=node()
#     p=g
#     while first1 is not None and first2 is not None:
#         if first1.val>first2.val:
#             g.next=first2
#             first2=first2.next
#         else:
#             g.next=first1
#             first1=first1.next
#         g=g.next
#
#     if first1 is not None:
#         g.next=first1
#     else:
#         g.next=first2
#
#     return p.next
#
# def scalk(first1,first2,k):
#     g=node()
#     p=g
#     ile=0
#     while first1 is not None and first2 is not None:
#         ile+=1
#         if first1.val>first2.val:
#             g.next=first2
#             first2=first2.next
#         else:
#             g.next=first1
#             first1=first1.next
#         if k is not None and ile==k:
#             q=g.next
#         g=g.next
#     if k is not None and ile == k:
#         q = g
#     if first1 is not None:
#         g.next=first1
#     else:
#         g.next=first2
#     if k is not None:
#         return q
#     return p.next
#
# def podzial(l):
#     heads=[]
#     heads.append(l)
#     while l.next is not None:
#         if l.val>l.next.val:
#             heads.append(l.next)
#             t=l
#             l = l.next
#             t.next=None
#         else:
#             l=l.next
#     #print(2)
#     return heads
#
# def sort_m(tab):
#     tabb=[]
#     while len(tab)!=1:
#         n=len(tab)
#         for i in range(n//2):
#             tabb.append(scal(tab[2*i],tab[2*i+1]))
#         if n%2==1:
#             tabb.append(tab[n-1])
#         tab,tabb=tabb,tab
#         tabb=[]
#     return tab[0]
#
# def SortH(l,k):
#     ile=0
#     head=[]
#     g=l
#     while ile<k+1:
#         ile+=1
#         l=l.next
#     if l is None:
#         return sort_m(podzial(g))
#     p=l.next
#     l.next=None
#     head.append(sort_m(podzial(g)))
#     first=head[0]
#     if first.val<l.val:
#         temp=first.next
#         first.next = l.next
#         l.next=temp
#     l=p
#     g=l
#     ile=0
#     while l is not None:
#         #print(l.val)
#         ile += 1
#         if ile==k:
#             p=l.next
#             l.next=None
#             head[0]=scal(head[0],sort_m(podzial(g)))
#             l=p
#             g=p
#             ile=0
#         else:
#             l=l.next
#     if ile!=0:
#         head[0] = scal(head[0], sort_m(podzial(g)))
#
#     return first
#
#
# runtests( SortH )

from zad1testy import Node, runtests

class node:
    def __init__(self,val=None):
        self.next=None
        self.val=val



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

def sort_m(tab):
    tabb=[]
    while len(tab)!=1:
        n=len(tab)
        for i in range(n//2):
            tabb.append(scal(tab[2*i],tab[2*i+1]))
        if n%2==1:
            tabb.append(tab[n-1])
        tab,tabb=tabb,tab
        tabb=[]
    return tab[0]

def SortH(l,k):
    ile=0
    head=[]
    g=l
    for i in range(k):
        l=l.next
    if l is None:
        return sort_m(podzial(g))
    p=l.next
    l.next=None
    head.append(sort_m(podzial(g)))
    first=head[0]
    l=p
    g=p

    while l is not None:
        ile+=1
        if ile==k:
            ile = 0
            p = l.next
            l.next = None
            head[0]=scal(head[0],sort_m(podzial(g)))
            for i in range(k):
                head[0]=head[0].next
            l=p
            g=p
        else:
            l=l.next
    print(1)
    if ile!=0:
        head[0] = scal(head[0], sort_m(podzial(g)))
    return first

runtests( SortH )






