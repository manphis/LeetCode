'''
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.
'''

class Solution:
    def reverseString(self, s: 'List[str]') -> 'None':
        """
        Do not return anything, modify s in-place instead.
        """
        l = len(s)
        for i in range(int(l/2)):
            tmp = s[i]
            s[i] = s[l-i-1]
            s[l-i-1] = tmp
        return