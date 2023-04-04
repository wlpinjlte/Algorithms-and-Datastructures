from zad1testy import runtests
sciezki=[]
def odczyt(s,parent):
    doc=[]
    while s!=None:
        doc.append(s)
        s=parent[s]
    return doc
def dfs(G,s,k):
    global sciezki
    def dfss(s,G,tab):
        global sciezki
        nonlocal k
        i=0
        #print(s)
        while i<len(G) and G[i][0]<s:
            i+=1
            #print(i)
        while i<len(G) and G[i][0]==s:
            if G[i][1]==k:
                tab.append(G[i][1])
                sciezki.append(tab.copy())
                tab.remove(G[i][1])
            tab.append(G[i][1])
            dfss(G[i][1],G,tab)
            tab.remove(G[i][1])
            i+=1
    tab=[]
    tab.append(s)
    dfss(s,G,tab)
def znajdz(G,x,y):
    for i in range(len(G)):
        if G[i][0]==x and G[i][1]==y:
            return i
def intuse(I, x, y):
    global sciezki
    G=I.copy()
    I=sorted(I,key=lambda x:x[0])
    dfs(I,x,y)
    doc=[]
    for i in sciezki:
        #print(i)
        for j in range(len(i)-1):
            temp=znajdz(G,i[j],i[j+1])
            if temp not in doc:
                doc.append(temp)
    sciezki=[]
    return doc


runtests(intuse)
