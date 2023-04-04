from zad3testy import runtests
import queue
from math import inf
#f(i,p)-min ilość tankowań żeby dojechać do pola i z energią p(tankujemy na polu)
roz=[]
def f(i,p,q,T,V,F,l):
    global roz
    # if i==len(T):
    #     return 10**10
    p+=V[i]
    p=min(p,q)
    #print(i,p)
    if l-T[i]-p<=0:
        return 0
    if F[i][p]!=10**10:
        return F[i][p]
    ind=i+1
    if ind == len(T):
        return 10**10
    while T[ind]-T[i]<=p:
        if F[i][p]>f(ind,p-(T[ind]-T[i]),q,T,V,F,l)+1:
            F[i][p]=min(f(ind,p-(T[ind]-T[i]),q,T,V,F,l)+1,F[i][p])
            roz[i][p]=(ind,min(p-(T[ind]-T[i])+V[ind],q))
        ind+=1
        if ind==len(T):
            break
    return F[i][p]

def iamlate(T, V, q, l):
    #q = 2
    global roz
    F=[[10**10 for j in range(q+1)]for i in range(len(T))]
    roz=[[None for j in range(q+1)] for i in range(len(T))]
    doc=[]
    if f(0,0,q,T,V,F,l)+1<10**10:
        #print(roz)
        tmp=(0,min(V[0],q))
        doc.append(tmp[0])
        while roz[tmp[0]][tmp[1]]!=None:
            doc.append(roz[tmp[0]][tmp[1]][0])
            tmp=roz[tmp[0]][tmp[1]]
            #print(tmp)
    return doc

runtests(iamlate)