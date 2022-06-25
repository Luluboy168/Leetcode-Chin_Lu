class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        if len(set(nums)) == len(nums):  #set 創建不重複元素集
            return False
        
        for i in range(len(nums)):
            if nums.count(nums[i]) == 1:
                continue
            for j in range(i+1, len(nums)):
                if abs(j - i) > k:
                    break
                if nums[i] == nums[j]:
                    return True
        
        return False
