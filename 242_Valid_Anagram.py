'''
Given two strings s and t , write a function to determine if t is an anagram of s.
'''
class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        d = dict()
        for key in s:
            if key in d:
                d[key] += 1
            else:
                d[key] = 1
                
        for key in t:
            if key in d:
                d[key] -= 1
                if d[key] < 0:
                    return False
            else:
                return False
        return True