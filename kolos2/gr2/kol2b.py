from kol2btesty import runtests
#f(i,u)-minimalny koszt dojazdu do parkingu i gdy u==1 z wykorzystanym 2l km gdy u==0 bez wykorzystania bonusu
#f(i,1)=min(f(i-l,1),f(i-g,0))gdzie l(0,L) g(L,2L)(zasięgi kilometrów)
#f(i,0)=min(f(i-l,0))-bez bonusu
def f(i,u,F,T,tab):
    if F[i][u]!=10**10:
        return F[i][u]
    if i<0:
        return 0
    if u==0:
        j=i-1
        #print(j)
        z=tab[j][0]
        while tab[i][0]-z<=T:
            F[i][u]=min(F[i][u],f(j,u,F,T,tab)+tab[i][1])
            j-=1
            if j<0:
                break
            z=tab[j][0]
    else:
        j = i - 1
        #print(j)
        z = tab[j][0]
        while tab[i][0] - z <= T:
            F[i][u] = min(F[i][u], f(j, u, F, T, tab) + tab[i][1])
            j -= 1
            if j<0: break
            z = tab[j][0]
        while tab[i][0]-z<=2*T:
            F[i][u] = min(F[i][u], f(j, 0, F, T, tab) + tab[i][1])
            j-=1
            if j<0:
                break
            z=tab[j][0]
    return F[i][u]

def min_cost( O, C, T, L ):
    #print(O,C,T,L)
    F=[[10**10 for i in range(2)]for i in range(len(O)+2)]
    for i in range(len(O)):
        O[i]=(O[i],C[i])
    O.insert(0,(0,0))
    O.append((L,0))
    O = sorted(O, key=lambda x: x[0])
    #print(O)
    #     for i in range(len(O)):
    # if O[i][0]>=T:
    #         break
    #     F[i][1]=C[i]
    # for i in range(len(O)):
    #     if O[i][0]>=2*T:
    #         break
    #     F[i][0] = C[i]
    #F[0][0]=0
    #F[0][1]=0
    #print(O)
    return f(len(O)-1,1,F,T,O)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( min_cost, all_tests = True )
