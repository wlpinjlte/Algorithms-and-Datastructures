from kol2btesty import runtests
#f(i,u)-min koszt dojazdu do parkingu i(ze spaniem) przy wykorzystaniu i nie wykorzystaniu bonusu(u)
def f(i,O,F,T,u):
    # if i<0:
    #     return 0
    if F[i][u]!=10**10:
        return F[i][u]
    j=i-1
    while O[i][0]-O[j][0]<=T:
        F[i][u]=min(F[i][u],f(j,O,F,T,u)+O[i][1])
        j-=1
        #print(j)
        if j<0:
            break
    if u==1 and j>=0:
        while O[i][0]-O[j][0]<=2*T:
            F[i][u] = min(F[i][u], f(j, O, F, T, 0)+O[i][1])
            j-=1
            if j < 0:
                break
    return F[i][u]
def min_cost(O,C,T,L):
    for i in range(len(O)):
        O[i]=(O[i],C[i])
    O=sorted(O,key=lambda x:x[0])
    O.append((L,0))
    O.insert(0,(0,0))

    F=[[10**10for j in range(2)]for i in range(len(O))]
    F[0][0]=0
    F[0][1]=0
    return min(f(len(O)-1,O,F,T,1),f(len(O)-1,O,F,T,0))

runtests(min_cost,all_tests = True)