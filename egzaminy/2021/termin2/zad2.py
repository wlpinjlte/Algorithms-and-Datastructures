from zad2testy import runtests
minn=(10**10,10**10)
def sumy(T):
    suma=0
    #print(T.edges)
    #print(T.weights)
    # if T==None:
    #     return 0
    for i in range(len(T.edges)):
        suma+=(sumy(T.edges[i])+T.weights[i])
    T.summ=suma
    return T.summ
def dfs(T,maks):
    global minn
    #print(T.summ)
    for i in range(len(T.edges)):
        if minn[0]>(abs(maks-2*T.edges[i].summ-T.weights[i])):
            print(abs(maks-2*T.edges[i].summ-T.weights[i]))
            minn=(abs(maks-2*T.edges[i].summ-T.weights[i]),T.ids[i])
        dfs(T.edges[i],maks)
def balance(T):
    global minn
    minn = (10 ** 10, 10 ** 10)
    sumy(T)
    maks=T.summ
    dfs(T,maks)
    #print(minn[0])
    return minn[1]


runtests(balance)

