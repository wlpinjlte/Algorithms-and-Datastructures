from egzP2btesty import runtests
from math import log10
import bisect
def kryptograf( D, Q ):
    s=0
    l=1
    #print(len(D))
    for i in Q:
        for j in D:
            if i=='':
                s=len(D)
                continue
            if j[-len(i):]==i:
                s+=1
        if s==0:
            continue
        #print(s)
        l=l*s
        s=0
    #print(D)
    #print(Q)
    #print(l)
    return log10(l)

# Zmień all_test na:
# 0 - Dla małych testów
# 1 - Dla złożoności akceptowalnej
# 2 - Dla złożoności dobrej
# 3 - Dla złożoności wzorcowej
runtests(kryptograf, all_tests = 1)