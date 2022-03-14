class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #binary search
        i, j = 0, len(nums)
        while i + 1 < j:
            m = (i + j)//2
            if nums[m] > target:
                j = m;
            else:
                i = m;
        return i + (nums[i] < target)
