from zad3testy import runtests
import math

def buble(tab):
    for i in range(len(tab)):
        for j in range(len(tab)-1-i):
            if tab[j]>tab[j+1]:
                tab[j],tab[j+1]=tab[j+1],tab[j]
    return
def fast_sort(tab, a):
    for i in range(len(tab)):
        tab[i]=math.log(tab[i],a)
    kubelki=[[]for i in range(len(tab)+1)]
    step=1/len(tab)
    for i in range(len(tab)):
        kubelki[int(tab[i]/step)].append(tab[i])
    doc=[]
    for i in kubelki:
        buble(i)
        for j in i:
            doc.append(a**j)
    return doc
runtests(fast_sort)