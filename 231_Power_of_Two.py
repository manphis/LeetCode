'''Given an integer, write a function to determine if it is a power of two.'''

class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        count = 0
        while n != 0:
            if n & 1 == 1:
                count += 1
            n = n >> 1
        result = True if count == 1 else False
        return result