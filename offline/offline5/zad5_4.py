from zad5testy import runtests

def plan(T):
    a=0
    p=T[0]
    doc=[0]
    while True:
        print(a,p)
        maks=0
        maksa=0
        if a+p>=len(T)-1:
            break
        for j in range(a+1,a+p+1):
            if maks<p+T[j]-j+a and T[j]!=0:
                maks=p+T[j]-j+a
                maksa=j
        a=maksa
        doc.append(a)
        p=maks

    return doc

runtests( plan, all_tests = True )