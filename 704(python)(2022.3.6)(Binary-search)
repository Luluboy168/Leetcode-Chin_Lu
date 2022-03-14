class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums)
        while i + 1 < j:
            m = (i + j) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                j = m
            else:
                i = m
            
        if nums[(i+j)//2] == target:
            return (i+j)//2
        return -1
