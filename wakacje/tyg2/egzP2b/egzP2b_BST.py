from egzP2btesty import runtests
from math import log10
wynik=0
#wezły BST
class node:
    def __init__(self):
        self.left=None
        self.right=None
        self.x=(-1,0)
#zbudowanie BST
def build_BST(m):
    G=node()
    def poz(f,p):
        nonlocal m
        if p==m:
            return
        pp=node()
        l=node()
        f.right=pp
        f.left=l
        poz(f.right,p+1)
        poz(f.left,p+1)
    poz(G,0)
    return G
#zaznaczenie gdzie w BST jest sufiks z listy
def QQ(s,f):
    #print(s)
    if s=='':
        #print("eko")
        f.x=(0,f.x[1]+1)
    elif s[-1]=='1':
        #print("elp")
        QQ(s[:-1],f.right)
    else:
        #print("siema")
        QQ(s[:-1], f.left)
    #print(f.x)
#ilość wystąpien każdego sufiksu
def licz(s,f):
    if f.x[0]!=-1:
        #print(f.x[0])
        f.x=(f.x[0]+1,f.x[1])
    if s=='':
        return
    if s[-1]=='1':
        licz(s[:-1],f.right)
    else:
        licz(s[:-1], f.left)
#zliczanie wyniku
def loggg(T):
    global wynik
    if T==None:
        return
    #print(T.x)
    if T.x[0]!=-1:
        #print(T.x)
        if T.x[0]!=0:
            wynik+=log10(T.x[0])*T.x[1]
    loggg(T.right)
    loggg(T.left)
def kryptograf( D, Q ):
    maks=0
    global wynik
    wynik=0
    for i in Q:
        maks=max(maks,len(i))
    #print(maks)
    T=build_BST(maks+1)
    for i in Q:
        QQ(i,T)
    for i in D:
        licz(i[-maks:],T)
    loggg(T)
    return wynik


runtests(kryptograf, all_tests = 3)