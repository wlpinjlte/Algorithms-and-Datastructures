# Dyrektor działu handlowego pewnej firmy odbywa podróż służbową z miasta A do miasta B. W pewnych
# punktach zaplanowanej trasy znajdują się stacje benzynowe. Niestety, ze względu na problemy
# z dostawami surowca, stacje limitują objętość paliwa, którą może zatankować pojedynczy klient.
# Co więcej, z powodu modyfikacji zmierzających do zwiększenia głośności i mocy silnika, samochód
# dyrektora spala aż 1 litr paliwa na 1 kilometr trasy. Dyrektor się spieszy - musi więc tak
# zaplanować podróż, by zatrzymać się na jak najmniejszej liczbie stacji. Jest to o tyle niełatwe, że
# każda stacja ma własny limit litrów paliwa, które można na niej zatankować. Dodatkową przeszkodą
# jest fakt, że w celu zmniejszenia masy pojazdu zmodyfikowano w nim zbiornik paliwa, który obecnie
# mieści jedynie q litrów benzyny. Zaproponuj i zaimplementuj algorytm wskazujący na których stacjach
# dyrektor powinien tankować paliwo (tak, by tankować możliwie najmniejszą liczbę razy). Algorytm
# powinien być możliwie jak najszybszy i zużywać jak najmniej pamięci. Uzasadnij jego poprawność
# i oszacuj złożoność obliczeniową. Algorytm należy zaimplementować jako funkcję:
# def iamlate(T, V, q, l):
#     ...
# która przyjmuje:
# 1. Tablicę liczb naturalnych T z pozycjami stacji benzynowych, wyrażonymi jako kilometry od
# początku trasy. Pierwsza stacja znajduje się na początku trasy, t.j. T[0] = 0. Kolejne stacje
# umieszczone są w T w kolejności odleglości od początku trasy.
# 2. Tablicę dodatnich liczb naturalnych V zawierającą limity paliwa, które może zatankować
# pojedynczy klient. Tak więc V[i] to liczba litrów paliwa, którą można zatankować na stacji
# w pozycji T[i]. Na danej stacji można tankować tylko raz.
# 3. Dodatnią liczbę naturalną q będącą pojemnością baku samochodu (liczba litrów paliwa, które
# mieszczą się w baku). Zakładamy, że przed pierwszym tankowaniem w baku nie ma paliwa.
# 4. Dodatnią liczbę naturalną l będącą długością trasy w kilometrach.
# Funkcja powinna zwrócić listę numerów stacji, na których należy tankować paliwo (w kolejności
# tankowania). Jeśli warunki zadania uniemożliwiają dotarcie do celu, funkcja powinna zwrócić pustą
# listę. Stacje numerujemy od 0. Stacja na początku trasy stanowi część rozwiązania.
from zad3testy import runtests
from math import inf
#odn=[]
#f(i,p)-minimalny dojazd na i-tą stacje z zapasem p paliwa(z zatankowaniem)
#f(i,p)=min(f(i+j,(p+V[i])modq-d[j])+1)(while p-d[j]>=0)
def f(i,p,V,T,q,l,F):
    p += V[i]
    if p > q:
        p = q
    if F[i][p]!=10**10:
        return F[i][p]
    #print(i,p)
    if i==len(T)-1:
        if T[i]+p>=l:
            F[i][p]=1
            return 1
        else:
            F[i][p]=10**9
            return 10**10
    #print(i,len(T))
    if T[i]+p>=l:
        F[i][p]=1
        return 1
    j=i+1
    while p-T[j]+T[i]>=0:
        F[i][p] = min(F[i][p], f(j, p - T[j] + T[i],V,T,q,l,F)+1)
        j+=1
        if j==len(T):
            break
    return F[i][p]
def iamlate(T, V, q, l):
    print(T)
    print(V)
    F=[[10**10 for j in range(q+1)]for i in range(len(T))]
    print(f(0,0,V,T,q,l,F))
    #for i in range(len(T)):

    #print(F)
    return []


runtests(iamlate)