from egzP6atesty import runtests 
def ile_liter(s):
    summ=0
    for i in s:
        if 97<=ord(i)<=122:
            summ+=1
    return summ
def partiton(tab,p,l):
    x=tab[l]
    i=p-1
    for j in range(p,l):
        if tab[j]<x:
            i+=1
            tab[j],tab[i]=tab[i],tab[j]
    tab[l],tab[i+1]=tab[i+1],tab[l]
    return i+1
def qs(tab,p,l):
    if l-p>0:
        q=partiton(tab,p,l)
        qs(tab,q+1,l)
        qs(tab,p,q-1)
    return
def google ( H, s ):
    maks=0
    #print(ord("a"))
    #print(ord("z"))
    for i in H:
        maks=max(len(i),maks)
    tab=[[[]for j in range(i+1)]for i in range(maks+1)]#pierwszy wymiar długość drugi wymiar ilość liter
    for i in H:#dodwanie do koszyczków
        tab[len(i)][ile_liter(i)].append(i)
    for i in tab:#
        for j in i:#sortowanie leksykograficzne
            #print(j)
            if len(j)>1:
                #print(len(j))
                qs(j,0,len(j)-1)
        i.reverse()#rivers by się zgadzała kolejność ad2
    #print(tab)
    tab.reverse()#ad2
    #print(tab)
    ind=0#indeks
    for i in tab:#przejscie i zliacznie ile mineliśmy haseł
        for j in i:
            for z in j:
                ind+=1
                if ind==s:
                    return z
    return ""


runtests ( google, all_tests=True )