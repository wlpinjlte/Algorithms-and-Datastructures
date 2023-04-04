from egz1btesty import runtests
class Node:
  def __init__( self ):
    self.left = None    # lewe poddrzewo
    self.right = None   # prawe poddrzewo
    self.x = 0
# def parent(f,p):
#     if f==None:
#         return
#     if p==None:
#         parent(f.right,f)
#         return parent(f.left,f)
#     f.x=p
#     parent(f.right, f)
#     return parent(f.left, f)
def zerowanie_x(f):
    if f==None:
        return
    f.x=0
    zerowanie_x(f.left)
    return zerowanie_x(f.right)
def wys(f):
    if f==None:
        return 0
    return max(wys(f.right)+1,wys(f.left)+1)
def ile(f,p,gdzie):
    if f==None:
        return
    gdzie[p]+=1
    ile(f.right,p+1,gdzie)
    ile(f.left,p+1,gdzie)
def dfs(p,f,a):
    #print(p,f,a)
    #print(f.x)
    if f==None:
        return 0
    if p==a:
        f.x=1
        return f.x
    f.x=max(dfs(p+1,f.right,a),dfs(p+1,f.left,a))
    #print(f.x)
    return f.x
def ciecia(f):
    #print(f.x)
    if f==None:
        return 0
    if f.x==0:
        return 1
    return ciecia(f.right)+ciecia(f.left)
def wideentall( T ):
    h = wys(T)
    gdzie=[0 for i in range(h)]
    ile(T,0,gdzie)
    #parent(T,None)
    maks=(0,0)
    zerowanie_x(T)
    for i in range(len(gdzie)):
        if maks[0]<=gdzie[i]:
            maks=(gdzie[i],i)
    dfs(0,T,maks[1])
    return ciecia(T)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( wideentall, all_tests = False )