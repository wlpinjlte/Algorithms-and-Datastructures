from zad3testy import runtests
import math

def bubble(tab):
    for i in range(len(tab)):
        flag=True
        for j in range(i,len(tab)-1):
            if tab[j]>tab[j+1]:
                flag=False
                tab[j],tab[j+1]=tab[j+1],tab[j]
        if flag:
            return
    return
def fast_sort(tab, a):
    n=len(tab)
    doc=[[]for i in range(n)]

    for i in range(len(tab)):
        temp=math.log(tab[i],a)
        #print(temp//(1/n))
        doc[int(temp//(1/n))].append(temp)
    for i in doc:
        bubble(i)
    docc=[]
    for i in doc:
        for j in i:
            docc.append(a**j)
    return docc


runtests(fast_sort)
