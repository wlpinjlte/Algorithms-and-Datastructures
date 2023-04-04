from kolutesty import runtests


def swaps( disk, depends ):
    graf=[[]for i in range(len(depends))]
    prev=[len(depends[i])for i in range(len(depends))]
    stosA = []
    stosB= []
    for i in range(len(depends)):
        for j in depends[i]:
            graf[j].append(i)
        if len(depends[i])==0 and disk[i]=="A":
            stosA.append(i)
        elif len(depends[i])==0:
            stosB.append(i)
    #u="A" dla a
    #print(graf)
    if len(stosA)!=0:
        counter=0
        while len(stosA)!=0 or len(stosB)!=0:
            while len(stosA)!=0:
                x=stosA.pop()
                for i in graf[x]:
                    prev[i]-=1
                    if prev[i]==0:
                        if disk[i]=='A':
                            stosA.append(i)
                        else:
                            stosB.append(i)
            counter += 1
            if len(stosB)==0:
                break
            while len(stosB)!=0:
                x = stosB.pop()
                for i in graf[x]:
                    prev[i] -= 1
                    if prev[i] == 0:
                        if disk[i] == 'A':
                            stosA.append(i)
                        else:
                            stosB.append(i)
            counter += 1
    else:
        counter=10**10
    #u="B" dla b
    prev = [len(depends[i]) for i in range(len(depends))]
    for i in range(len(depends)):
        if len(depends[i])==0 and disk[i]=="A":
            stosA.append(i)
        elif len(depends[i])==0:
            stosB.append(i)
    counter1 = 0
    if len(stosB)!=0:
        while len(stosA) != 0 or len(stosB) != 0:
            while len(stosB) != 0:
                x = stosB.pop()
                for i in graf[x]:
                    prev[i] -= 1
                    if prev[i] == 0:
                        if disk[i] == 'A':
                            stosA.append(i)
                        else:
                            stosB.append(i)
            counter1+=1
            if len(stosA) == 0:
                break
            while len(stosA) != 0:
                x = stosA.pop()
                for i in graf[x]:
                    prev[i] -= 1
                    if prev[i] == 0:
                        if disk[i] == 'A':
                            stosA.append(i)
                        else:
                            stosB.append(i)
            counter1 += 1
    else:
        counter1=10**10
    return min(counter-1,counter1-1)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( swaps, all_tests = True)