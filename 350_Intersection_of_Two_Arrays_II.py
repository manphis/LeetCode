'''
Given two arrays, write a function to compute their intersection.
'''

class Solution:
    def intersect(self, nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':
        nums1.sort()
        nums2.sort()
        idx1 = 0
        idx2 = 0
        result = []
        
        while idx1 < len(nums1) and idx2 < len(nums2):
            if nums1[idx1] == nums2[idx2]:
                result.append(nums1[idx1])
                idx1 += 1
                idx2 += 1
            elif nums1[idx1] < nums2[idx2]:
                idx1 += 1
            elif nums1[idx1] > nums2[idx2]:
                idx2 += 1
        return result