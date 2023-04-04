tab1=[]
tab2=[]
for i in range(-len(tab1)+1,len(tab2)+len(tab1)-1):
    for j in range(-len(tab1) + 1, len(tab2) + len(tab1) - 1):
        for z in range(len(tab1)):
            for y in range(len(tab1)):
                if i>-1 and i<len(tab2) and j>-1 and j<len(tab2):
                    wyszystkie += 1
                    if tab1[z][y]==tab2[i+z][j+y]:
                        równe+=1
