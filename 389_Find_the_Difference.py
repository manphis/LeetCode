'''
Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one more letter at a random position.

Find the letter that was added in t.
'''

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ss = sorted(s)
        st = sorted(t)
        
        for i in range(len(ss)):
            if (ss[i] != st[i]):
                return st[i]
        return st[-1]