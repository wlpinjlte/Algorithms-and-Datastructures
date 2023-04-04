from egzP4btesty import runtests
tab=[]
def wrzut(T):
    global tab
    if T==None:
        return
    tab.append(T.key)
    wrzut(T.right)
    wrzut(T.left)
def find_ind(T,w):
    p=0
    l=len(T)
    i=(p+l)//2
    while w!=T[i]:
        if T[i]<w:
            p=i
        else:
            l=i
        i=(p+l)//2
    return i
def sol(root, T):
    global tab
    summ=0
    wrzut(root)
    tab=sorted(tab)
    print(tab)
    for i in T:
        ind=find_ind(tab,i.key)
        if tab[ind-1]+tab[ind+1]==tab[ind]*2:
            summ+=tab[ind]
    return summ


runtests(sol, all_tests=False)