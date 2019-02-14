'''
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
'''
class Solution:
    def isPowerOfFour(self, num: 'int') -> 'bool':
        a = (num & 0x55555555) == num
        b = not(num & (num - 1))
        c = num > 0
        return a and b and c