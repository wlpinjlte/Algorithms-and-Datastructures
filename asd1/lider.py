def lider(tab):
    ile=1
    lid=tab[0]
    for i in range(1,len(tab)):
        if tab[i]==lid:
            ile+=1
        elif ile==1:
            lid=tab[i]
        else:
            ile-=1
    return lid

tab=[1,2,2,3,3,3,3,2,2]
print(lider(tab))


