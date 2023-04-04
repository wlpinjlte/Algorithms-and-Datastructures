from egzP3atesty import runtests
from math import inf
#plecak-standartowy
#f(i,b)-maks zysk wyborocow przy budzecie b i zbiorze i
#f(i,b)=max(f(i+1,b),f(i+1,b-k[i])+z[i])
class Node:
  def __init__(self, wyborcy, koszt, fundusze):
    self.next = None
    self.wyborcy = wyborcy 
    self.koszt = koszt 
    self.fundusze = fundusze 
    self.x = None
def f(i,b,F,ll,n):
    if b<0:
        return -10**10
    if i==n:
        return 0
    if F[i][b]!=-1:
        return F[i][b]
    F[i][b]=max(f(i+1,b-ll.koszt,F,ll.next,n)+ll.wyborcy,f(i+1,b,F,ll.next,n))
    return F[i][b]
def ile(f):
    if f==None:
        return 0
    return ile(f.next)+1
def wybory(T):
    sum=0
    for i in T:
        ii=ile(i)
        F=[[-1for j in range(i.fundusze+1)]for z in range(ii)]
        sum+=f(0,i.fundusze,F,i,ii)
    #print(10**10)
    return sum

runtests(wybory, all_tests = True)