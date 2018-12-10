'''
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array
such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
'''
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        lst = {}
        result = False
        for i in range(len(nums)):
            if nums[i] in lst:
                if i - lst[nums[i]] <= k:
                    result = True
                    break
                else:
                    lst[nums[i]] = i
            else:
                lst[nums[i]] = i
                
        return result