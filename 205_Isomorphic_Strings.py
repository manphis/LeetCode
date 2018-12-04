'''
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.
'''

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        d = dict()
        result = True
        for i in range(len(s)):
            if s[i] in d:
                if d[s[i]] != t[i]:
                    result = False
                    break
            else:
                if t[i] in d.values():
                    result = False
                    break
                d[s[i]] = t[i]
        
        return result