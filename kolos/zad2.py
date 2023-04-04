def cutting(s):
    binar=''

    for i in s:
        if i in ["a",'e','i','y','o','u']:
            binar+='1'
        else:
            binar+='0'
    for i in range(len(binar)-1,0,-1):
        if binar[i]=='1':
            binar=binar[:i+1]
            break
    for i in range(len(binar)):
        if binar[i]=='1':
            binar=binar[i:]
            break
    print(binar)
    def rek(binar,i=0,il=0):
        print(il)
        if len(binar)==i:
            if il==1:
                return 1
            return 0
        if il==0:
            #print(2)
            return rek(binar,i+1,il+int(binar[i]))
        if il==1:
            #print(i)
            if binar[i]=='1':
                return rek(binar,i+1,int(binar[i]))
            return rek(binar,i+1,il+int(binar[i]))+rek(binar,i+1,0)
    return rek(binar)
string="sesja"
print(cutting(string))
