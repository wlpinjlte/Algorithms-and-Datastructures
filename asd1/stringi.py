def maxx(tab):
    maxxx=len(tab[0])
    for i in range(len(tab)):
        if maxxx<len(tab[i]):
            maxxx=len(tab[i])
    return maxxx
tab=["dsggsd","gdgdfgfd","gdfghfd","ekopa","abbad"]
tabb=[[]for i in range(maxx(tab)+1)]

for i in range(len(tab)):
    tabb[len(tab[i])].append(tab[i])
doc=[]
for i in tabb:
    if len(i)>1:
        for j in range(len(i[0])-1,-1,-1):
            d=[0 for z in range(len(i))]
            c=[0 for z in range(50)]
            for z in range(len(i)):
                c[ord(i[z][j])-ord("a")]+=1
            for z in range(1,len(c)):
                c[z]+=c[z-1]
            for z in range(len(i)-1,-1,-1):
                d[c[ord(i[z][j])-ord("a")]-1]=i[z]
            i,d=d,i
            print(i)
    doc.extend(i)
print(tabb)
print(doc)

