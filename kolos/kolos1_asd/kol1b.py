#Mateusz Waga program dziala na zasadzie posortowania do kubełków napisów tej samej długość(przedstawionych jako tablice 27 elementowe) później sortujemy stosujac idea radix sort przy pomocy counting i na sam koniec przechodzimy liniowo tablice w poszukiwaniu maksium zlożoność to n(O(n)=n)
from kol1btesty import runtests

def maxx(T):#max ze długości stringa z tablicy
    maxxx=len(T[0])
    for i in range(1,len(T)):
        if maxxx<len(T[i]):
            maxxx=len(T[i])
    return maxxx

def count_cyfr(s):# zlicza znaki i przedstawia w tablicy 27 licznej
    tab=[0 for i in range(27)]
    for i in range(len(s)):
        tab[ord(s[i])-ord('a')]+=1
    return tab

def counting(tab,z,maxp):#counting sort ze wzgledu na ity element tablicy 27 elementowej
    n=len(tab)
    c=[0for i in range(maxp+1)]
    b=[0for i in range(n)]
    for i in range(len(tab)):
        c[tab[i][z]]+=1
    for i in range(1,len(c)):
        c[i]+=c[i-1]
    for i in range(n-1,-1,-1):
        b[c[tab[i][z]]-1]=tab[i]
        c[tab[i][z]]-=1
    return b
def por(a,b):#porównanie dwóch tablic
    for i in range(len(a)):
        if a[i]!=b[i]:
            return 0
    return 1

def f(T):
    maxp=maxx(T)
    tabb=[[]for _ in range(maxp+1)]
    for i in range(len(T)):#Wrzucenie do bucket
        tabb[len(T[i])].append(count_cyfr(T[i]))
    doc=[]
    for i in tabb:#radix
        if len(i)>=1:
            pomm=i
            for z in range(26,-1,-1):
                #doc.append(counting(i,z,maxp))
                pomm=counting(pomm,z,maxp)
            doc.append(pomm)
    max_=0
    for i in doc:#liczenie maks
        pom_l=1
        pom=i[0]
        for z in range(1,len(i)):
            if por(pom,i[z])==1:
                pom_l+=1
            else:
                if max_<pom_l:
                    max_=pom_l
                pom_l=1
                pom=i[z]
        if max_ < pom_l:
            max_ = pom_l
    return max_





# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( f, all_tests=True)
