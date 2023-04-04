from zad6ktesty import runtests
#f(i)-ilosc mozliwych haseł do i-tej pozycji
flag=False
def f( i,S,F ):
    global flag
    if i<=0:
        return 1
    if F[i]!=-1:
        return F[i]
    x = S[i - 1:i + 1]
    #print(x)
    if x=="00" or (int(x)>=30 and int(x)%10==0):
        print("elo")
        flag=True
    if int(x)==10 or int(x)==20:
        F[i]=f(i-2,S,F)
    elif 10<int(x)<27:
        F[i]=f(i-1,S,F)+f(i-2,S,F)
    else:
        F[i]=f(i-1,S,F)
    return F[i]
def haslo(S):
    global flag
    #print(S)
    flag=False
    F=[-1 for i in range(len(S))]
    f(len(S) - 1, S, F)
    if flag:
        return 0
    else:
        return f(len(S) - 1, S, F)
runtests ( haslo )