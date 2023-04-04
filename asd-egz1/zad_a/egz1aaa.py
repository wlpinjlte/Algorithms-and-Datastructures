from egz1atesty import runtests


def snow( S ):
    S=sorted(S,reverse=True)
    counter=0
    suma=0
    while S[counter]-counter>0:
        suma+=S[counter]-counter
        counter+=1
    return suma

runtests(snow,all_tests=True)