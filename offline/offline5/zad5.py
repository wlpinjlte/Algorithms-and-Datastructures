import queue

from zad5testy import runtests

def plan(T):
    p=T[0]
    a=0
    doc=[0]
    q=queue.PriorityQueue()
    while a+p<len(T)-1:
        if p==0:
            b=q.get()
            p+=-b[0]
            doc.append(b[1])
        if T[a+1]!=0:
            q.put((-T[a+1],a+1))
        a+=1
        p-=1
    doc.sort()
    return doc

runtests( plan, all_tests = True )