from egzP6btesty import runtests 

def jump ( M ):
    skok={'UL':(-1,2),'RD':(2,-1),'UR':(1,2),'RU':(2,1),'DR':(1,-2),"DL":(-1,-2),"LD":(-2,-1),"LU":(-2,1)}#skoki na pola
    dictt={}
    dictt[0]={0:1}#słownik
    licz=1#licznik
    poz=(0,0)
    for i in M:
        poz=(poz[0]+skok[i][0],poz[1]+skok[i][1])#zmiana pozycji za każdym razem
        x=dictt.get(poz[0])#sprawdzenie czy jest klucz od pierwszej pozycji
        if x==None:#jeżeli nie ma to dodajemy taki i tworzymy nowy słownik gdzie dajemy odrazu 2 współrzedną
            dictt[poz[0]]={poz[1]:1}
            licz+=1
        else:
            y=x.get(poz[1])
            if y==None:#sprawdzam czy druga współrzedna jest w drugim słowniku
                dictt[poz[0]][poz[1]]=1#nie ma to dodaje
                licz+=1
            else:#jest to zmieniam wartośc na przeciwną
                if y==1:
                    dictt[poz[0]][poz[1]] = 0
                    licz-=1
                else:
                    dictt[poz[0]][poz[1]] = 1
                    licz += 1
    #print(dictt)#zwracam wynik
    return licz
    
runtests(jump, all_tests = True)