maks=0
def pod(t,s=0,i=0,p=0,d=0):
    #print(p)
    global maks
    if len(t)==i:
        if s==p:
            if maks<d:
                maks=d
            #print(d)
            #print(p)
        return
    if p==0:
        pod(t,0,i+1,s+t[i],d+1)
    if s==p:
        return pod(t,t[i],i+1,p,d+1)
    return pod(t,s+t[i],i+1,p,d)
t=[1,2,3,1,5,2,2,2,6]
pod(t)
print(maks)
