from zad4testy import runtests

elo=0
tab=[]

def spr(pod,a,b,T):
    for i in range(len(T)):
        if(pod[i]!=0):
            if(b<T[i][1] or a>T[i][2]):
                # if(a==T[i][2]):
                #
                pass
            else:
                return 0
    return 1


def rek(T,p,pod,i=0,mak=0):
        global elo
        global tab
        if elo<mak:
            elo=mak
            tab=pod.copy()
        if i==len(T):
            return
        # if p==0:
        #     return
        if p-T[i][3]>=0:
            if(spr(pod,T[i][1],T[i][2],T)):
                #print(1)
                pod[i] = 1
                rek(T,p-T[i][3],pod,i+1,mak+(T[i][2]-T[i][1])*T[i][0])
            pod[i]=0
        return rek(T,p,pod,i+1,mak)

def select_buildings(T,p):
    global tab
    pod=[0 for i in range(len(T))]
    rek(T,p,pod)
    doc=[]
    for i in range(len(tab)):
        if(tab[i]!=0):
            doc.append(i)
    return doc

runtests( select_buildings )