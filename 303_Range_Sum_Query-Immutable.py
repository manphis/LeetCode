'''
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
'''
class NumArray:

    def __init__(self, nums: 'List[int]'):
        self.lst = nums
        for i in range(1, len(self.lst)):
            self.lst[i] += self.lst[i-1]
        

    def sumRange(self, i: 'int', j: 'int') -> 'int':
        if i == 0:
            return self.lst[j]
        else:
            return self.lst[j] - self.lst[i-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)