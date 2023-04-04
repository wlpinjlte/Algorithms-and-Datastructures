from zad9ktesty import runtests
#f(i,g,d)-maks aut przy załadunku g gornego podkladu i d dolnego oraz auta i
#f(i,g,d)=max(f(i+1,g-w[i],d)+1,f(i+1,g,d-w[i])+1)
roz=[]
def f(i,g,d,P,F):
    global roz
    if i==len(P):
        return 0
    if g<0 or d<0:
        return -10**10
    if g-P[i]<0 and d-P[i]<0:
        return 0
    if F[i][g][d]!=-1:
        return F[i][g][d]
    if f(i+1,g-P[i],d,P,F)>f(i+1,g,d-P[i],P,F):
        roz[i][g][d]=(g-P[i],d)
    else:
        roz[i][g][d]=(g,d-P[i])
    F[i][g][d] = max(f(i + 1, g - P[i], d, P, F) + 1, f(i + 1, g, d - P[i], P, F) + 1)
    return F[i][g][d]
def prom(P, g, d):
    #print(P)
    global roz
    roz=[[[0for j in range(d+1)]for i in range(g+1)]for z in range(len(P))]
    F=[[[-1for z in range(d+1)]for j in range(g+1)]for i in range(len(P))]
    #print(f(0,g,d,P,F))
    #(roz)
    gg=[]
    dd=[]
    tmp=(g,d)
    i=0
    while i!=f(0,g,d,P,F):
        if roz[i][tmp[0]][tmp[1]][0]==tmp[0]:
            dd.append(i)
        else:
            gg.append(i)
        tmp = roz[i][tmp[0]][tmp[1]]
        #print(tmp)
        i += 1
    i-=1
    if i in dd:
        return dd
    return gg

runtests ( prom)