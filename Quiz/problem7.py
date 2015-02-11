def McNuggets(n):

    new = n

    if n%20 ==0:
        return True
    else:
        new = new%20
        if new%9 ==0:
            return True
        else:
            new = new%9
            if new%6 ==0:
                return True
        if new %6 == 0:
            return True
    if n%9 == 0:
        return True
    else:
        new =new %9
        if new%6==0:
            return True
    if n%6 ==0:
        return True

    return False


def McNug(n):

    a=0
    b=0
    c=0

    while a*6 < n:
        while b*9 < n:
            while c*20 < n:
                if a*6 + b*9 + c*20 == n:
                    return True
                c+=1
            c=0
            b+=1
        b=0
        a+=1


    return False
