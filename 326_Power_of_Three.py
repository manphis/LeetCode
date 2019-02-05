'''
Given an integer, write a function to determine if it is a power of three.
'''

class Solution:
    def isPowerOfThree(self, n: 'int') -> 'bool':
        if n <= 0:
            return False
        
        while n%3 == 0:
            n /= 3
        if n == 1:
            return True
        else:
            return False