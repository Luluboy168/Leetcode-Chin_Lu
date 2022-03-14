class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while nums.count(val) != 0:    #while val in nums:
            nums.remove(val)
            
        return len(nums)

"""
l = 0
while l < len(nums):
if nums[l] == val:
nums.pop(l)
else:
l += 1 
"""
