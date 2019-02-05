'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
'''

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero_index = -1
        for i in range(len(nums)):
            value = nums[i]
            if value == 0:
                if zero_index == -1:
                    zero_index = i
            else:
                if zero_index != -1:
                    self.swap(zero_index, i, nums)
                    zero_index += 1
    
    def swap(self, i, j, nums):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp
        return