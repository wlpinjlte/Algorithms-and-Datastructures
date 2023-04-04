from zad2testy import runtests
import random
def partiton(tab,p,l):
    x=tab[l]
    i=p-1
    for j in range(p,l):
        if tab[j][0]<x[0]:
            i += 1
            tab[j],tab[i]=tab[i],tab[j]
        elif tab[j][0]==x[0] and tab[j][1]>x[1]:
            i += 1
            tab[j], tab[i] = tab[i], tab[j]
    tab[l],tab[i+1]=tab[i+1],tab[l]
    return i+1

def quicsort(tab,p,l):
    tabb=[]
    tabb.append([p,l])
    while len(tabb)>0:
        a,b=tabb.pop()
        if b-a>0:
            q=partiton(tab,a,b)
            tabb.append([q+1,b])
            tabb.append([a,q-1])

# def bublle_sort(tab,p,l):
#     for j in range(l-p-1):
#         for i in range(p,l):
#             if tab[i][0] < tab[i+1][0]:
#                 tab[i+1], tab[i] = tab[i], tab[i+1]
#             elif tab[i][0] == tab[i+1][0] and tab[i+1][1] > tab[i][1]:
#                 tab[i + 1], tab[i] = tab[i], tab[i + 1]
# tab = [[1, 4],[5, 6],[2, 5],[8, 9],[1, 6],[2,3]]
# quicsort(tab,0,len(tab)-1)
# print(tab)
def depth(L):
    quicsort(L,0,len(L)-1)
    # bublle_sort(L,0,len(L)-1)
    return


runtests( depth )