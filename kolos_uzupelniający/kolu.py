from kolutesty import runtests

def deleate(disk,x):
    for i in disk:
        for j in i:
            if x==j:
                i.remove(x)
def sprawdz(visited,depends):
    for i in depends:
        if visited[i]==False:
            return 0
    return 1
def swaps( disk, depends ):
    counter=0
    ile=0
    visited=[False for i in range(len(disk))]
    u='A'
    while ile<len(disk):
        if u=="A":
            u="B"
        else:
            u="A"
        if ile==0 and counter==1:
            counter=10**10
            break
        counter+=1
        i=0
        while i<len(disk):
            if visited[i]==False and sprawdz(visited,depends[i])==1:
                if u==disk[i]:
                    visited[i]=True
                    ile+=1
                    i=0
                else:
                    i+=1
            else:
                i+=1
        #print(u)
    ile = 0
    visited = [False for i in range(len(disk))]
    counter1=0
    u = 'B'
    while ile < len(disk):
        if u == "A":
            u = "B"
        else:
            u = "A"
        if ile == 0 and counter1 == 1:
            counter1 = 10 ** 10
            break
        counter1 += 1

        i = 0
        while i < len(disk):
            if visited[i] == False and sprawdz(visited, depends[i]) == 1:
                if u == disk[i]:
                    visited[i] = True
                    ile += 1
                    i = 0
                else:
                    i += 1
            else:
                i += 1
        # print(u)
    return min(counter-1,counter1-1)
# disk = ['A', 'A', 'B', 'B']
# depands=[[2, 3],[],[1, 3],[1]]
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( swaps, all_tests = True )
#print(swaps(disk,depands))

