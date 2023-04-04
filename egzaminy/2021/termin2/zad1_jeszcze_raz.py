from zad1testy import runtests
#import bisect
def bisect_right(a, x, lo=0, hi=None):
    """Return the index where to insert item x in list a, assuming a is sorted.

    The return value i is such that all e in a[:i] have e <= x, and all e in
    a[i:] have e > x.  So if x already appears in the list, a.insert(x) will
    insert just after the rightmost x already there.

    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """

    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if x < a[mid][1]: hi = mid
        else: lo = mid+1
    return lo
def bisect_left(a, x, lo=0, hi=None):
    """Return the index where to insert item x in list a, assuming a is sorted.

    The return value i is such that all e in a[:i] have e < x, and all e in
    a[i:] have e >= x.  So if x already appears in the list, a.insert(x) will
    insert just before the leftmost x already there.

    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """

    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if a[mid][0] < x: lo = mid+1
        else: hi = mid
    return lo
def dfs_x(graf,s,visited):
    #visited=[0for i in range(len(graf))]
    ind=bisect_left(graf,s)
    while ind<len(graf) and graf[ind][0]==s and visited[ind]==0:
        visited[ind]=1
        dfs_x(graf,graf[ind][1],visited)
        ind+=1
    return
def dfs_y(graf,s,visited):
    #visited = [0 for i in range(len(graf))]
    #print(1)
    ind = bisect_right(graf, s)
    ind=ind-1
    while ind >= 0 and graf[ind][1] == s and visited[ind] == 0:
        visited[ind] = 1
        dfs_y(graf, graf[ind][0],visited)
        ind -= 1
    return
def intuse(I, x, y):
    #II=I.copy()
    for i in range(len(I)):
        I[i]=(I[i][0],I[i][1],i)
    I=sorted(I,key=lambda z:z[0])
    print(I)
    visitedx=[0for i in range(len(I))]
    dfs_x(I,x,visitedx)
    #print(visitedx)
    visitedy=[0for i in range(len(I))]
    I = sorted(I, key=lambda z: z[1])
    #print(I,y)
    dfs_y(I,y,visitedy)
    #print(visitedy)
    docy=[0for i in range(len(I))]
    for i in range(len(I)):
        if visitedy[i]==1:
            docy[I[i][2]]=1
    docx=[0for i in range(len(I))]
    I = sorted(I, key=lambda z: z[0])
    for i in range(len(I)):
        if visitedx[i]==1:
            docx[I[i][2]]=1
    doc=[]
    for i in range(len(I)):
        if docx[i]==1 and docy[i]==1:
            doc.append(i)
    return doc
runtests(intuse)