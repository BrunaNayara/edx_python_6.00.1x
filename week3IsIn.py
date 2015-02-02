def isIn(char, aStr):

    index = len(aStr)//2

    print (aStr)
    if len(aStr) <=1:
        if ord(char) == ord(aStr[index]):
            return True
        return False

    if ord(char) < ord(aStr[index]):
        print (aStr[index])
        return isIn(char, aStr[:index])
    elif ord(char) > ord(aStr[index]):
        print (aStr[index])
        return isIn(char, aStr[index:])
    elif ord(char) == ord(aStr[index]):
        print (aStr[index])
        return True
    else:
        return False

def semordnilap(str1, str2):

    if len(str1) == len(str2):
        if len(str1) == 0:
            return True
        else:
            if str1[0] == str2[-1]:
                return semordnilap(str1[1:], str2[:-1])
            else:
                return False

    else:
        False



def fibMetered(x):
    global numCalls
    numCalls += 1
    if x == 0 or x == 1:
        return 1
    else:
        return fibMetered(x-1) + fibMetered(x-2)

def testFib(n):
    global numCalls
    numCalls = 0
    for i in range(n+1):
        print('fib of ' + str(i) + ' = ' + str(fibMetered(i)))
        print ('fib called ' + str(numCalls) + ' times')


def biggest(aDict):

    dic = {}

    if len(aDict) ==0:
        return None

    for key in aDict:
        dic[key] = 0
        for item in aDict[key]:
            dic[key] = dic[key] +1

    for key in dic:
        if dic[key] == max(dic.values()):
            return key



