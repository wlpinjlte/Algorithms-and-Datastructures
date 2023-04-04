tab=[0,1,2,3,4,5,6,9,43,688,6666,778894,768976895789,6548675867876867]
def binar(tab,x):
    a=0
    b=len(tab)
    while b-a!=1:
        s=(a+b)//2
        if tab[s]==x:
            return s
        elif tab[s]>x:
            b=s
        else:
            a=s
    return a
print(tab[binar(tab,778894)])
