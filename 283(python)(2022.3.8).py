class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        for i in range(len(nums)):
            if nums[i - count] == 0:
                nums.pop(i - count)
                nums.append(0)
                count += 1
