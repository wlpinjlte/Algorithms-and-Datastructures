from zad11ktesty import runtests
#f(i,w)-min rożnica przy wagdze pojazdu pierwszego do i-tego bagażu
s=0
def f(i,w,F,T):
    global s
    if i==len(T):
        #print(w,s)
        return abs(s-2*w)
    if F[i][w]!=10**10:
        return F[i][w]
    F[i][w]=min(f(i+1,w+T[i],F,T),f(i+1,w,F,T))
    return F[i][w]
def summ(T):
    global s
    for i in T:
        s+=i
    return
def kontenerowiec(T):
    global s
    s=0
    #print(T)
    summ(T)
    #print(s)
    F=[[10**10for j in range(s+1)]for i in range(len(T))]
    return f(0,0,F,T)
runtests(kontenerowiec)