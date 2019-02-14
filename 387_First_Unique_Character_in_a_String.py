'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
'''

class Solution:
    def firstUniqChar(self, s: 'str') -> 'int':
        d = dict()
        for i in range(len(s)):
            if s[i] in d:
                if d[s[i]] != -2:
                    d[s[i]] = -2
            else:
                d[s[i]] = i
        
        min_v = sys.maxsize
        min_k = ''
        for key, value in d.items():
            if value != -2 and value < min_v:
                min_v = value
                
        if min_v == sys.maxsize:
            return -1
        else:
            return min_v