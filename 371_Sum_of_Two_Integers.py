'''
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
'''

class Solution:
    def getSum(self, a: 'int', b: 'int') -> 'int':
        mask = 0xffffffff
        sum = (a ^ b) & mask
        part = a & b
        while part:
            a = sum
            b = (part << 1) & mask
            sum = (a ^ b) & mask
            part = a & b
        if sum & 0x80000000:
            sum -= 0x100000000
        return sum