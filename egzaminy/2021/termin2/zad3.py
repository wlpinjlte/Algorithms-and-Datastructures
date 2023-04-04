from zad3testy import runtests


def lamps(n, T):
    tab=[0 for i in range(n)]
    maks=0
    tym = 0
    for i in T:
        for j in range(i[0],i[1]+1):
            tab[j]=(tab[j]+1)%3
            # print(j)
            # print(tab[j])
            # print()
            if tab[j]==2:
                tym+=1
            if tab[j]==0:
                tym-=1
        maks=max(maks,tym)
    return maks


runtests(lamps)

