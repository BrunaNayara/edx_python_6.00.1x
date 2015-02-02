import unittest
from itertools import count
class AlphabSubsTest(unittest.TestCase):
    def test_alphabetical_subs(self):
        self.assertEqual(alphabetic_subs('abcbcd'), 'abc')
        self.assertEqual(alphabetic_subs('azcbobobegghakl'), 'beggh')

def alphabetic_subs(s):
    max_subs = s[0:0]
#    subs = ''
    for start in range(len(s)-1):
        for end in count(start+len(max_subs) + 1):
            subs = s[start:end]
            if len(subs) != (end - start):
                break
            if sorted(subs) == list(subs):
                max_subs = subs


#        if ord(s[i]) <= ord(s[i+1]):
#            subs += s[i]
#        else:
#            subs+= s[i]
#
#    sub = subs.split()





    return max_subs
