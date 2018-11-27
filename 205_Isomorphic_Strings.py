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