'''
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
'''

class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        '''
        while num / 10 >= 1:
            tmp = 0
            a = num
            while a != 0:
                tmp += a % 10
                a = int((a - (a%10)) / 10)
            num = tmp
        return num
        '''
        if num == 0:
            return 0
        return num % 9 if (num%9 != 0) else 9