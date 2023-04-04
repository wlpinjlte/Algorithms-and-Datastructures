from egzP2btesty import runtests
from math import log10
import bisect
def kryptograf( D, Q ):
    for i in range(len(D)):
        D[i]=D[i][::-1]
    for i in range(len(Q)):
        Q[i]=Q[i][::-1]
    l=1
    D=sorted(D)
    for i in Q:
        lewo=bisect.bisect_left(D,i)
        prawo=bisect.bisect_right(D,i+"2")
        l*=(prawo-lewo)

    return log10(l)

# Zmień all_test na:
# 0 - Dla małych testów
# 1 - Dla złożoności akceptowalnej
# 2 - Dla złożoności dobrej
# 3 - Dla złożoności wzorcowej
runtests(kryptograf, all_tests = 3)