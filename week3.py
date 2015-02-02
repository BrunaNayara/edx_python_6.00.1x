def gcdRec(a, b):

    if b ==0:
        return a
    else:
        return gcdRec(b, a%b)


def gcdIter(a, b):

    div = min(a,b)

    if max(a, b)%min(a, b) == 0:
        return min(a, b)

    if min(a, b) ==1:
        return min(a, b)

    while div >0:
        if a%div==0 and b%div == 0:
            return div
        div-=1

def lenIter(aStr):
    i=0
    for c in aStr:
        i +=1

    return i

def lenRecur(aStr):

    if aStr == '':
        return 0
    else:
        return 1+lenRecur(aStr[:-1])

