'''
Given two arrays, write a function to compute their intersection.
'''

class Solution:
    def intersection(self, nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':
        intersect = []
        for i in range(len(nums1)):
            if nums1[i] in nums2 and not nums1[i] in intersect:
                intersect.append(nums1[i])
                
        return intersect