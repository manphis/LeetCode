'''
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
'''

class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total = int(n*(n+1)/2)
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            
        return total - sum