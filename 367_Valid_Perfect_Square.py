'''
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.
'''

class Solution:
    def isPerfectSquare(self, num: 'int') -> 'bool':
        i = 1
        result = False
        while True:
            a = i * i
            if a == num:
                result = True
                break
            elif a > num:
                break
            i += 1
        return result