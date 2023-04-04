from kolutesty import runtests
def swaps( disk, depends ):
    #print(disk,depends)
    stosA=[]
    stosB=[]
    ile=[len(i) for i in depends]
    graf=[[]for i in range(len(disk))]
    #print(ile)
    for i in range(len(depends)):
        for j in depends[i]:
            graf[j].append(i)
    #print(graf)
    for i in range(len(depends)):
        if len(depends[i])==0 and disk[i]=="A":
            stosA.append(i)
        elif len(depends[i])==0:
            stosB.append(i)
    if len(stosA)==0:
        counter1 = 10**10
    else:
        counter1=0
    while True:
        while len(stosA)!=0:
            x=stosA.pop()
            for i in graf[x]:
                ile[i]-=1
                if ile[i]==0:
                    if disk[i]=="A":
                        stosA.append(i)
                    else:
                        stosB.append(i)
        if len(stosB)==0:
            break
        counter1+=1
        while len(stosB)!=0:
            x = stosB.pop()
            for i in graf[x]:
                ile[i] -= 1
                if ile[i] == 0:
                    if disk[i] == "A":
                        stosA.append(i)
                    else:
                        stosB.append(i)
        if len(stosA)==0:
            break
        counter1+=1
    #spr1
    # for i in ile:
    #     if i!=0:
    #         counter1=10**10
    #         break


    stosA = []
    stosB = []
    ile = [len(i) for i in depends]
    for i in range(len(depends)):
        if len(depends[i])==0 and disk[i]=="B":
            stosB.append(i)
        elif len(depends[i])==0:
            stosA.append(i)
    if len(stosB)==0:
        counter2 = 10**10
    else:
        counter2=0
    while True:
        while len(stosB)!=0:
            x=stosB.pop()
            for i in graf[x]:
                ile[i]-=1
                if ile[i]==0:
                    if disk[i]=="A":
                        stosA.append(i)
                    else:
                        stosB.append(i)
        if len(stosA)==0:
            break
        counter2+=1
        while len(stosA)!=0:
            x=stosA.pop()
            for i in graf[x]:
                ile[i]-=1
                if ile[i]==0:
                    if disk[i]=="A":
                        stosA.append(i)
                    else:
                        stosB.append(i)
        if len(stosB)==0:
            break
        counter2+=1
    #spr2
    # for i in ile:
    #     if i!=0:
    #         counter2=10**10
    #         break


    return min(counter1,counter2)

runtests( swaps, all_tests = True )