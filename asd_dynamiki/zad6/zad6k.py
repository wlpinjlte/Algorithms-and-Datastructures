from zad6ktesty import runtests
T=True
#f(i)-maksymalna ilość możliwych haseł z stringa i
def f(i):
    global T
    if len(i)==0:
        return 1
    if len(i)==1:
        if int(i)!=0:
            return 1
        return 0
    pom=i[-2:]
    if pom=="00" or (int(pom)%10==0 and int(pom)>20):
        #print(pom)
        T=False
    if int(pom)==10 or int(pom)==20:
        return f(i[:-2])
    else:
        s=f(i[:-1])
        if 10<int(pom)<27 and int(pom)!=20:
            #print(1)
            s+=f(i[:-2])
    return s

def haslo ( S ):
    global T
    print(S)
    T=True
    pom=f(S)
    if T:
        return pom
    else:
        return 0

runtests ( haslo )