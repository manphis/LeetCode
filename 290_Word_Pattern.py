'''
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.
'''

class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        word = str.split()
        if len(pattern) != len(word):
            return False
        d = dict()
        for i in range(len(pattern)):
            if pattern[i] in d:
                if d[pattern[i]] != word[i]:
                    return False
            else:
                if word[i] in d.values():
                    return False
                else:
                    d[pattern[i]] = word[i]
        return True