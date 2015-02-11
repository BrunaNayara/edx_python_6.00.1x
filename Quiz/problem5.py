def laceStrings(s1, s2):

    lace = ''

    if s1 == s2 and s1 == '':
        return lace
    if  s1 == '':
        return s2
    if s2 == '':
        return s1

    for i in range( min(len(s1), len(s2))):
        lace = lace +s1[i] +s2[i]
        print i
        print lace

    if max(len(s1), len(s2)) == len(s1):
        remain = s1
    if max(len(s1), len(s2)) == len(s2):
        remain = s2

    lace = lace + remain[i+1:]


    return lace
