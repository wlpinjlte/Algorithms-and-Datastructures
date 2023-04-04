def lewo(i):
    return 2*i+1
def prawo(i):
    return 2*i+2
def rodzic(i):
    return (i-1)//2

def heapify(tab,n,i):
    l=lewo(i)
    r=prawo(i)
    ak=i
    if l<n and tab[l]<tab[ak]:
        ak=l
    if r<n and tab[r]<tab[ak]:
        ak=r
    if ak!=i:
        tab[i],tab[ak]=tab[ak],tab[i]
        heapify(tab,n,ak)

tab=[0,1,2,5555,3,4,5,6,9,43,688,6666,778894,768976895789,6548675867876867]
def rek(tab,x,i):
    if i>=len(tab):
        return 0
    if tab[i]>x:
        return 0
    return 1+rek(tab,x,lewo(i))+rek(tab,x,prawo(i))


for i in range(rodzic(len(tab)-1),-1,-1):
    heapify(tab,len(tab)-1,i)
print(tab)
print(rek(tab,50,0))