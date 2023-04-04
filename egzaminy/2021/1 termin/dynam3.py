from zad3testy import runtests
import queue
global ile
wynik=(0,0)
def rek(A,i,k,p,tab,F):
  global ile,wynik
  if k==ile:
    #print(p[1]-p[0],p[1],p[0])
    if wynik[0]<p[1]-p[0]:
      wynik=(p[1]-p[0],tab.copy())
    #wynik=max(wynik,p[1]-p[0])
    return
  if F[i][k][p[1]]!=10**10:
      return F[i][k][p[1]]
  if i==len(A):
    return
  if A[i][1]<=p[0] or p[1]<=A[i][0]:
    pass
  else:
    tab[i]=1
    F[i][k][p[1]]=rek(A,i+1,k+1,(A[i][0],min(A[i][1],p[1])),tab,F)
    tab[i]=0
  return rek(A,i+1,k,p,tab,F)

def odczyt(tab1,tab2,tab3):
  doc=[]
  for i in range(len(tab3)):
    if tab3[i]==1:
      for j in range(len(tab2)):
        if tab1[i]==tab2[j]:
          doc.append(j)
          break
  return doc

def kintersect( A, k ):
  global ile,wynik
  F=[[[10**10 for z in range(max(key=lambda A:A[1]))]for j in range(len(A))]for i in range(len(A))]
  a=A.copy()
  A=sorted(A,key=lambda x:x[0])
  ile=k
  tab=[0 for i in range(len(A))]
  #for i in range(len(A)-k+1):
  rek(A,0,0,(-1,10**10),tab,F)
  print(wynik)
  wynikk=wynik
  wynik=(0,0)
  return odczyt(A,a,wynikk[1])

runtests( kintersect )
