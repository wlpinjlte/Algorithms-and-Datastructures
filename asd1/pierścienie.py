import math
R=1000

def promien(n):
    if n<=1:
        return R/math.sqrt(n)
    return math.sqrt(promien(n-1)+(R**2)/n)

n=10
def index(od):
    return n*od//(R**2)

tab=[[]for i in range(n)]
tabb=[]
def buble(tab):
    for i in range(len(tab)):
        for j in range(len(tab)-i-1):
            if tab[j]<tab[j+1]:
                tab[j],tab[j+1]=tab[j+1],tab[j]
    return

for i in range(n):
    tab[index(tabb[i][0]**tabb[i][0]+tabb[i][1]**tabb[i][1])].append(tabb)
tabb=[]
for i in range(n):
    buble(tab[i])
    tabb.extend(tab[i])
print(tabb)