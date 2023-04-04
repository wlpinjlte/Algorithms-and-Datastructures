#Mateusz Waga program polega na odcienciu każej możliwej krawedzi i sprawdzeniu każego przypadku czy zgadza się z warunkami zadania i sprawdzeniu wyskokosci i sprawdzeniu szerokosc
from egz1btesty import runtests
wynik=(0,0,0)
class Node:
  def __init__( self ):
    self.left = None    # lewe poddrzewo
    self.right = None   # prawe poddrzewo
    self.x = None
def spr(s):
    if s==None:
        return -10**10
    if s.left==None and s.right==None:
        return 0
    return max(spr(s.left)+1,spr(s.right)+1)
def spr2(s):
    if s==None:
        return 10**10
    if s.left==None and s.right==None:
        return 0
    return min(spr(s.left)+1,spr(s.right)+1)
def wys(s):
    if s==None:
        return 0
    return max(wys(s.left)+1,wys(s.right)+1)
def ile_lisci(s):
    if s==None:
        return 0
    if s.right==None and s.left==None:
        return 1
    return ile_lisci(s.left)+ile_lisci(s.right)
def burt(s,i,f):
    if s==None:
        return
    global wynik
    if spr(f)==spr2(f):
        if ile_lisci(f)>wynik[0]:
            #print(1)
            wynik=(ile_lisci(f),wys(f),i)
            print(wynik)
        elif ile_lisci(f)==wynik[0]:
            if wys(f)>wynik[1]:
                #print(1)
                wynik=(ile_lisci(f),wys(f),i)
                print(wynik)
            elif wys(f)==wynik[1] and wynik[2]>i:
                wynik=(ile_lisci(f),wys(f),i)
    burt(s.right,i,f)
    burt(s.left,i,f)
    temp1=s.left
    temp2=s.right
    s.right=None
    i+=1
    if spr(f)==spr2(f):
        if ile_lisci(f)>wynik[0]:
            #print(1)
            wynik=(ile_lisci(f),wys(f),i)
            print(wynik)
        elif ile_lisci(f)==wynik[0]:
            if wys(f)>wynik[1]:
                #print(1)
                wynik=(ile_lisci(f),wys(f),i)
                print(wynik)
            elif wys(f) == wynik[1] and wynik[2] > i:
                wynik=(ile_lisci(f), wys(f), i)
    burt(s.left,i,f)
    s.left=None
    i+=1
    if spr(f)==spr2(f):
        if ile_lisci(f)>wynik[0]:
            wynik=(ile_lisci(f),wys(f),i)
            print(wynik)
        elif ile_lisci(f)==wynik[0]:
            if wys(f)>wynik[1]:
                #print(1)
                wynik=(ile_lisci(f),wys(f),i)
                print(wynik)
            elif wys(f)==wynik[1] and wynik[2]>i:
                wynik=(ile_lisci(f),wys(f),i)
    i-=1
    s.right=temp1
    burt(s.right,i,f)
    i-=1
    s.left=temp2
def wideentall( T ):
    global wynik
    wynik=(0,0,0)
    if spr(T)==spr2(T):
        return 0
    burt(T,0,T)
    #print(wynik)
    return wynik[2]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( wideentall, all_tests = False )