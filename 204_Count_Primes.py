'''
Count the number of prime numbers less than a non-negative number, n.
'''

class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return 0
        lst = [True] * n
        lst[0] = False
        lst[1] = False
        for i in range(2, n):
            if lst[i] == False:
                continue
            else:
                base = 2
                while i * base < n:
                    lst[i*base] = False
                    base += 1
               
        return sum(lst)