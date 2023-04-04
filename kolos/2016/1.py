def spr(a,b):
    x,y=1,1
    while x<a:
        x,y=y,x+y
    return x==a and b==y
def fib(T):
    for i in range(len(T)-2):
        if T[i]+T[i+1]==T[i+2]:
            if(spr(T[i],T[i+1])):
                return True
    return False
def fib_od(T):
    if len(T)==3:
        return False
    for i in range(len(T)):
        #print(i)
        if fib(T[i]):
            return i
T=[[3452,53245,5,6],[3,2,1,4],[4,377,610,987],[5,4,11,412]]
#T=[[3452,53245,5],[3,2,1],[377,610,987]]
print(fib_od(T))
