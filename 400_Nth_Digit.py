'''
Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 231).
'''

class Solution:
    def findNthDigit(self, n: int) -> int:
        ndigit = 1
        num = 9
        while n > ndigit * num:
            n -= ndigit * num
            ndigit += 1
            num *= 10
            
        start = 10 ** (ndigit-1)
        start += int((n-1)/ndigit)
        s = str(start)
        # print(s)
        r = (n-1)%ndigit
        return int(s[r])