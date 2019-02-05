'''
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
'''

class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        flag = True
        while flag:
            if num == 1:
                break;
            elif num % 2 == 0:
                num = num/2
            elif num % 3 == 0:
                num = num/3
            elif num % 5 == 0:
                num = num/5
            else:
                flag = False
                break;
        return flag